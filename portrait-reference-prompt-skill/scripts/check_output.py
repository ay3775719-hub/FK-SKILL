#!/usr/bin/env python3
"""Check a completed ten-photo Markdown response without inspecting source images.

Run: python scripts/check_output.py output.md [--check format|negative|clean|all]
This reads local text only. It does not generate images or assess face similarity.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PHOTO = re.compile(r'^\s*(?:#{1,6}\s*)?照片\s*(\d+)\s*[：:]\s*$', re.MULTILINE)
LABEL = r'^\s*(?:#{{1,6}}\s*)?{name}\s*[：:]\s*$'
RULE_WORDS = ('严格复刻', '只参考', '唯一来源', 'SOP', '审核说明', '失败修正',
              '禁止', '不得', '不允许', '同上', '同前', '同上一张', '沿用上一张',
              '见上文', '参考图绑定', '主参考图大头', '--no')


def inspect_output(text: str, check: str = 'all') -> list[str]:
    """Return structural and lexical failures; visual/semantic quality is out of scope."""
    errors: list[str] = []
    expected_negative = (ROOT / 'assets/negative-prompt.txt').read_text(encoding='utf-8').strip()
    matches = list(PHOTO.finditer(text))
    if [int(item.group(1)) for item in matches] != list(range(1, 11)):
        errors.append('需要按顺序提供照片 1～10，共十条独立照片。')
    positives: list[str] = []
    for index, match in enumerate(matches):
        number = match.group(1)
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        block = text[match.end():end].strip()
        pos = list(re.finditer(LABEL.format(name='正向提示词'), block, re.MULTILINE))
        neg = list(re.finditer(LABEL.format(name='负面提示词'), block, re.MULTILINE))
        if len(pos) != 1 or len(neg) != 1 or (pos and neg and pos[0].start() >= neg[0].start()):
            errors.append(f'照片 {number}：需要一个正向标题和一个在其后的负面标题。')
            continue
        positive = block[pos[0].end():neg[0].start()].strip()
        negative = block[neg[0].end():].strip()
        if negative.endswith('\n---'):
            negative = negative[:-4].rstrip()
        positives.append(positive)
        if not positive:
            errors.append(f'照片 {number}：正向提示词为空。')
        if check in ('all', 'format'):
            if '3:4' not in positive and '3：4' not in positive:
                errors.append(f'照片 {number}：缺少 3:4 画幅。')
            if '单张' not in positive or '竖版' not in positive:
                errors.append(f'照片 {number}：缺少单张、竖版说明。')
        if check in ('all', 'negative') and negative != expected_negative:
            errors.append(f'照片 {number}：固定负面词遗漏、改变或附有额外正文。')
        if check in ('all', 'clean'):
            found = [word for word in RULE_WORDS if word in positive]
            if found:
                errors.append(f'照片 {number}：正向段残留规则或依赖前文：{", ".join(found)}')
    if check in ('all', 'clean') and len(set(positives)) != len(positives):
        errors.append('存在完全重复的正向提示词。')
    if check in ('all', 'format'):
        prefix = text[:matches[0].start()] if matches else text
        for term in ('主参考图识别', '最终场景', '十张绑定表', '色彩自检'):
            if term not in prefix:
                errors.append(f'照片提示词之前缺少“{term}”。')
    return errors


def main() -> int:
    """Validate one UTF-8 file and return a machine-readable result."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('--check', choices=('all', 'format', 'negative', 'clean'), default='all')
    args = parser.parse_args()
    try:
        errors = inspect_output(args.output.read_text(encoding='utf-8-sig'), args.check)
    except (OSError, UnicodeError) as exc:
        print(json.dumps({'passed': False, 'error_type': 'input', 'message': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps({'passed': not errors, 'scope': 'text-structure-only', 'errors': errors}, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
