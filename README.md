# FK-SKILL

完整的人像参考图提示词 Skill，版本 **1.0.1**。保留整套框架作为一个技能执行，包含上传引导、参考图区域分工、人物与妆容锁定、姿势绑定、同场景延伸及逐张正负提示词输出。

## 完整 Skill

技能目录：[portrait-reference-prompt-skill](portrait-reference-prompt-skill/)

- [SKILL.md](portrait-reference-prompt-skill/SKILL.md)：技能入口、上传引导与执行顺序。
- [完整执行框架](portrait-reference-prompt-skill/references/framework.md)：全部创作规则。
- [原始框架](portrait-reference-prompt-skill/assets/original-framework.txt)：保留的用户原文。
- [固定负面词](portrait-reference-prompt-skill/assets/negative-prompt.txt)：每张提示词单独附带。
- `scripts/`、`evals/`：文本格式检查、维护工具与评估样例。
- `install.ps1`、`install.sh`、`.claude-plugin/`：安装脚本与插件配置。
- [验证记录](portrait-reference-prompt-skill/VERIFICATION.md)：已完成检查及适用范围。

## 安装

下载本仓库后，将整个 `portrait-reference-prompt-skill` 文件夹复制到所用工具的技能目录。请保留内部目录结构，不要只复制入口文件。

Codex 用户可放入 `~/.codex/skills/portrait-reference-prompt-skill/`，随后在新对话中调用。

也可以在克隆本仓库后，使用附带安装脚本：

```powershell
# Windows PowerShell，先预览安装位置
.\portrait-reference-prompt-skill\install.ps1 -Platform codex -DryRun
# 执行安装
.\portrait-reference-prompt-skill\install.ps1 -Platform codex
```

安装脚本会替换目标目录已有的同名技能；有自定义修改时请先备份。其他平台入口见技能目录内的说明，跨平台兼容性尚未逐一实测。

## 使用前上传什么

1. **第一张主参考图**：看清人物脸妆和全身穿搭，建议使用“大头特写＋全身”的拼接图，全身尽量包含鞋包与配饰；单张照片足够清晰也可以。
2. **后续姿势参考图，至少一张**：只参考动作、神态和拍法，不采用其中的人物长相或穿搭。少于十张时同场景延伸补齐。
3. **可选补充**：场景、道具、不要出现的元素或指定妆容。

上传后说：

> 使用人像参考图提示词 skill，第一张锁人物与造型，后面参考拍法，按完整流程出十条提示词。

默认交付来源识别、场景、十张绑定表、色彩自检，以及十条独立 3:4 竖版照片提示词，每条分别包含完整正向词与固定负面词。默认不生成图片。智能体需要支持查看参考图。

## 许可

原框架及整理内容保留原包的个人使用许可，见 [LICENSE](portrait-reference-prompt-skill/LICENSE)；配套第三方工具的许可见 [THIRD_PARTY_LICENSE.txt](portrait-reference-prompt-skill/THIRD_PARTY_LICENSE.txt)。
