# Verification: portrait-reference-prompt-skill

<!-- agent-skill-verification: {"clean": true, "commit": "uncommitted", "fingerprint": "a0deac673322edbb44f0466009db60fc5ef714898908a81df48fb25426eefa6d", "version": "1.0.1"} -->

Generated: 2026-09-06T03:08:01Z

## Release evidence

- Run type: representative
- Recorded execution environments: codex
- Cross-environment compatibility: not established by this report
- Static text-sample checks: 6 passed, 0 failed, 0 errored, 0 regressed

## Gates

- PASS — specification
- PASS — security
- PASS — skill graph

## Interpretation

This report records only the checks completed at generation time. It does not prove
future live data, model output, other agent runtimes, or production user outcomes.
Run `python3 scripts/evolve.py` after a correction or material dependency change.

## 1.0.1 上传引导更新

本轮更新的是入口引导：未上传时列出主图、姿势图及可选场景信息；部分上传时只补问缺项；材料齐全直接执行；后续修改不反复索图。
静态技能检查通过；原有文字样例检查 6 项通过。本轮没有重新生成图片或进行独立模型视觉测试。
用户在本次对话反馈原有技能实际使用“效果挺不错”，此次按要求补上传说明，未改动原有固定负面词和编排逻辑。
人工审阅覆盖无图、只有主图、材料齐全、继续上一组四种入口情形；不是自动运行的独立模型测试。
