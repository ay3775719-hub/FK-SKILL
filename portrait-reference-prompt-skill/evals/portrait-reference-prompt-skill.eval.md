# 文字输出检查

本技能为交互式视觉写作流程，没有确定性的自动识图命令，因此不声明自动 rollout。
三个 reference.md 是助手按明确文字设定编排的格式样例，不是用户认可的真实图片结果。
这些命令只验证格式和词句，不能判断真实人脸、妆容、姿势、机位或图像相似度。
用户已批准保留固定负面词、净化正向词、缺图不猜及原样封装。
视觉检查在用户提供真实参考图后进行，不用样例中的关键词替代。

```json
{
  "skill": "portrait-reference-prompt-skill",
  "criteria": [
    {
      "id": "ten-independent",
      "text": "十张按顺序编号，逐张正负分段，含前置自检与3:4竖版说明",
      "type": "command",
      "cmd": "python scripts/check_output.py {output} --check format"
    },
    {
      "id": "fixed-negative",
      "text": "每张负面词与用户原文完全一致",
      "type": "command",
      "cmd": "python scripts/check_output.py {output} --check negative"
    },
    {
      "id": "clean-positive",
      "text": "正向段无已知规则话术、不依赖同上、不整段重复",
      "type": "command",
      "cmd": "python scripts/check_output.py {output} --check clean"
    }
  ],
  "golden": [
    {
      "id": "three-poses",
      "input": "golden/three-poses/input.txt",
      "expected": "golden/three-poses/reference.md",
      "split": "val"
    },
    {
      "id": "specified-scene",
      "input": "golden/specified-scene/input.txt",
      "expected": "golden/specified-scene/reference.md",
      "split": "val"
    },
    {
      "id": "makeup-holdout",
      "input": "golden/makeup-holdout/input.txt",
      "expected": "golden/makeup-holdout/reference.md",
      "split": "test"
    }
  ]
}
```
