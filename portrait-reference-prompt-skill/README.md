# 人像参考图提示词

一个个人使用的完整 skill，保留原框架，不拆分。

上传第 1 张主图和至少 1 张姿势参考图后，说：

> 使用人像参考图提示词 skill，按我的框架出十条，场景是咖啡馆，只输出提示词。

也可调用 `/portrait-reference-prompt-skill`。

默认交付前置自检和绑定表，再交付十条独立 3:4 竖版照片的正向提示词及逐张固定负面词；不自动生成图片。
没有参考图时先指出缺图。主图非拼接图时按实际可见内容识别，不强套分区。

## 开始前先上传什么

1. **主参考图放第一张：** 建议将清晰大头特写与全身穿搭放在一张拼接图中，脸妆要清楚，全身尽量包含鞋包及配饰。单张照片能看清脸和穿搭也可以，不强制拼图。
2. **后面放姿势图，至少一张：** 只参考动作、神态和拍法，不采用其人物长相、妆容或穿搭。不足十张会同场景延伸；要十张逐一复刻，就提供十张姿势图。
3. **可选：** 场景、道具、禁用元素或指定妆容。不指定场景就按穿搭匹配；保留某张姿势图背景时请明确图号。

脸部和穿搭图也可以分开上传，但请标明“脸妆主图”和“穿搭主图”，以免被误作姿势图。
直接说“使用这个 skill”还没上传图片时，助手会先给准备清单；已上传齐全时直接执行，缺什么只补问什么。

## 本次优化

- 原文逐字节保留，完整执行版沿用原文顺序。
- 妆容与肤色默认按主图实际细节；“冷艳女团妆”只作为可选预设。
- 来源分工与规则放入自检，正向词改成具体画面。
- 补上缺图、区域不清、不可见鞋包、无姿势图的处理。
- 固定负面词每张原样附带一次。

读取 `references/framework.md` 查看完整执行版；原文在 `assets/original-framework.txt`。

## 检查与修改

日常无需命令。可直接告诉助手：“修改这个 skill：……”并描述实际问题。
若将输出存为 Markdown，运行 `python scripts/check_output.py 输出.md` 检查数量、格式与负面词。
需要记录维护建议时，运行 `python scripts/evolve.py --correct "具体问题"`。
格式检查不能证明识图正确或生图身份一致；详见 `VERIFICATION.md` 的实际验证范围。

## 安装

当前已由助手安装到用户 Codex 技能目录。下一轮对话即可调用。
迁移时将本文件夹整体复制到目标技能目录；Codex 可用 `~/.codex/skills/` 或 `~/.agents/skills/`，
Claude Code 为 `~/.claude/skills/`，Copilot 为 `~/.copilot/skills/`，Gemini 为 `~/.gemini/skills/`，
OpenCode 为 `~/.config/opencode/skills/`。这些是路径声明，未逐个平台实测。
Claude Code 也可用 `/plugin marketplace add <本文件夹路径>` 后安装同名插件。

## Verification

[VERIFICATION.md](VERIFICATION.md) records the latest generation-time gate and eval evidence.
