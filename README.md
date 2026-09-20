# 简历 Skills Collection

这是一份改简历 Skill 的分类、对比和安装资料，适合用来快速判断：自己现在应该使用哪一类工具。

## 先按问题选 Skill

改简历不是一个单一动作。不同 Skill 往往会有功能重叠，但通常各有一个主要用途：

| 你现在卡在哪里 | 主要用途 | 推荐 Skill | 适合解决的问题 |
|---|---|---|---|
| 没有完整简历，只有流水账或零散材料 | 信息整合 | [`resume-builder`](https://github.com/Jichengyuuuuu/resume-builder-skill) | 收集经历、整理材料、生成简历初稿 |
| 已有简历，想投某个具体岗位 | 岗位定制 | [`resume-tailoring`](https://github.com/varunr89/resume-tailoring-skill) / [`resume-tailor`](https://github.com/nuin/resume-tailor) | 分析 JD，从真实经历中挑选并改写匹配内容 |
| 简历内容空泛，不知道哪里需要改 | 内容诊断与重写 | [`resume-optimizer`](https://github.com/Sumukhmg/resume-optimizer-claude-skill) | 从 HR 阅读角度检查结构、表达和成果，并输出重写建议 |
| 担心关键词、格式或招聘系统识别 | ATS 诊断 | [`resume-ats-optimizer`](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/career/resume-ats-optimizer/SKILL.md) | 检查关键词匹配、文件解析和 ATS 兼容风险 |
| 内容已经确定，只想排版和导出 | 排版渲染 | [`resume-md`](https://github.com/beholder91/resume-md-skill) | 将 Markdown、DOCX 等材料整理并导出为结构清晰的 PDF |
| 想一次获得多个简历相关模块 | 模块化工具箱 | [`ResumeSkills`](https://github.com/Paramchoudhary/ResumeSkills) | 将质检、改写、量化、JD 定制、排版和版本管理拆成独立模块，按需调用 |

## 怎么选择

可以把它们理解成不同侧重的套餐：

1. 材料还没整理好，先用 `resume-builder`。
2. 已经有简历但表达弱，用 `resume-optimizer` 做内容诊断和重写。
3. 有目标岗位，再用 `resume-tailoring` 或 `resume-tailor` 做 JD 定制。
4. 担心招聘系统读不懂，用 `resume-ats-optimizer` 做 ATS 检查。
5. 内容确认后，再用 `resume-md` 排版和导出 PDF。

这不是强制流程。已经有哪部分，就从下一步开始；不同 Skill 的功能会重叠，应以对应项目当前的 README、`SKILL.md` 和实际输出为准。

## 项目来源与说明

- [`resume-builder-skill`](https://github.com/Jichengyuuuuu/resume-builder-skill)：中文简历生成、HTML / DOCX 输出、ATS 和岗位定制。
- [`resume-tailoring-skill`](https://github.com/varunr89/resume-tailoring-skill)：根据 JD 定制简历，并通过追问补充岗位相关经历。
- [`resume-optimizer-claude-skill`](https://github.com/Sumukhmg/resume-optimizer-claude-skill)：简历审阅、重写、评分和 ATS 优化。
- [`resume-ats-optimizer`](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/career/resume-ats-optimizer/SKILL.md)：ATS 检查与关键词优化。
- [`ResumeSkills`](https://github.com/Paramchoudhary/ResumeSkills)：模块化简历与求职工具箱，可按需调用不同功能。
- [`resume-md-skill`](https://github.com/beholder91/resume-md-skill)：Markdown 简历转换和本地 PDF 渲染。
- [`resume-tailor`](https://github.com/nuin/resume-tailor)：另一套独立的岗位定制 Skill。

完整口播稿、详细分类说明和安装提示见[《简历 Skill 分类与来源》](./简历Skill分类与来源.md)。相关项目文件统一放在[`简历Skills/`](./简历Skills/)目录中。

> 提醒：Skill 的功能、安装方式和仓库内容可能更新。使用前请查看对应项目的最新说明；不要让 AI 编造经历、数据或技能。
