# 改简历 Skill 分类与来源

## 口播文案

朋友（语音条）：

“现在改简历的 Skill 也太多了吧？每个都说自己能改简历，我到底该用哪个？”

博主：

别急着装。简历优化可不是一个问题，可能是好几个问题。先搞清楚自己到底卡在哪儿，才能对症下药，不然装了一堆 Skill，最后还是病急乱投医。

其实改简历的 Skill，就像咱们日常体检的套餐。每个套餐里可能都有一些基础检查，但主打的内容不一样。

第一种，是“信息整合套餐”。

如果你没有完整简历，手里只有一些工作流水账，甚至不知道自己做过的事情哪些值得写，可以看 `resume-builder`。

它主打从零收集和整理材料：通过模板、信息收集和必要的追问，把你的经历整理成一份完整简历。

它解决的是：

“我想找工作，但根本不知道简历从哪里开始写。”

第二种，是“岗位定制套餐”。

如果你已经有简历，现在想投某个具体岗位，可以看 `resume-tailoring` 或 `resume-tailor`。

它会先分析 JD，看这个岗位需要什么能力，再从你的真实经历中挑选相关内容，改成更匹配这个岗位的版本。

如果经历写得不清楚，它也可能继续追问，比如你具体负责什么、做出了什么结果、有没有数据。

它解决的是：

“我的经历不少，但不知道怎么改才能更像这个岗位要的人。”

第三种，是“检查诊断套餐”。

如果你已经有一份简历，但不知道问题出在哪，可以看 `resume-optimizer` 或 `resume-ats-optimizer`。

这两个 Skill 都会帮你做简历诊断、出报告，但侧重点不同。

`resume-optimizer` 有点像基础又全面一些的体检套餐，更像 HR 视角，看的更全面，关注整体可读性、结构和表达，它输出的是一份重写后的完整简历加结构化评估报告。

`resume-ats-optimizer` 更像招聘系统体检，重点看你的简历对于目标岗位是否有足够的关键词能匹配上，格式是否标准、文件类型有没有解析风险，系统能不能正确识别你的内容。

简单说：

一个更关心 HR 看起来顺不顺，一个更关心招聘系统读不读得懂。

第四种，是“排版导出套餐”。

如果内容已经确定，只是 Word 排版很乱，或者你想把 Markdown、DOCX 重新渲染成清晰的 PDF，可以看 `resume-md`。

它主打字体、分页、排版和 PDF 导出，不会主动帮你做简历诊断，也不会主动润色内容。

总结一下，这些 Skill 的功能会重叠，但每个套餐主打的东西不同。所以你可以根据自己的情况选择。我个人建议的使用顺序是：信息收集、简历诊断、岗位匹配、格式检查，最后输出 PDF。

如果你觉得一个个去找麻烦，`ResumeSkills` 这种模块化工具箱也可以一次解决。它把质检、改写、成果量化、JD 定制、排版和版本管理拆成独立模块，可以单独使用，也可以整包安装、按需调用。

具体模块和安装方式我已经替你整理好了，直接把提示词丢给你常用的 AI，就能一键安装。

评论区留下“改简历”，我安排给你。

## 快速选择表

| 你现在的问题 | 适合的套餐 / Skill | 主要解决什么 |
|---|---|---|
| 没有完整简历，材料很零散 | `resume-builder` | 从信息收集到完整简历 |
| 已有简历，想投具体岗位 | `resume-tailoring` / `resume-tailor` | 分析目标 JD，生成岗位定制版 |
| 简历内容空泛，不知道哪里需要改 | `resume-optimizer` | 从 HR 视角重写和诊断 |
| 检查目标岗位关键词匹配度和格式 | `resume-ats-optimizer` | 检查关键词、格式和 ATS 识别 |
| 内容已经确定，只想排版导出 | `resume-md` | Markdown、DOCX 到 PDF 的稳定渲染 |
| 上面的问题都有，想一次安装多个模块 | `ResumeSkills` | 按需调用一整套简历工具 |

## 项目来源

以下链接均为对应项目的公开 GitHub 仓库：

1. [Jichengyuuuuu/resume-builder-skill](https://github.com/Jichengyuuuuu/resume-builder-skill) — 中文简历生成、HTML / DOCX 输出、ATS 和岗位定制。
2. [varunr89/resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill) — 根据 JD 定制简历，支持经历发现和岗位匹配。
3. [Sumukhmg/resume-optimizer-claude-skill](https://github.com/Sumukhmg/resume-optimizer-claude-skill) — 简历审阅、重写、评分和 ATS 优化。
4. [davila7/claude-code-templates — resume-ats-optimizer](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/career/resume-ats-optimizer/SKILL.md) — ATS 检查与关键词优化。
5. [Paramchoudhary/ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills) — 模块化简历与求职工具箱，包含改写、量化、排版和版本管理等功能。
6. [beholder91/resume-md-skill](https://github.com/beholder91/resume-md-skill) — 中文优先的 Markdown 简历转换与本地 PDF 渲染。
7. [nuin/resume-tailor](https://github.com/nuin/resume-tailor) — 另一套独立的岗位定制 Skill，适合与 `resume-tailoring` 区分查看。

## 使用顺序说明

这里的顺序是推荐工作流，不是强制调用顺序：

1. 先用 `resume-builder` 整理零散经历，或准备一份主简历。
2. 用 `resume-optimizer` / `resume-ats-optimizer` 做内容和格式诊断。
3. 针对具体 JD 使用 `resume-tailoring` / `resume-tailor`。
4. 内容确认后，用 `resume-md` 做排版和 PDF 导出。

不同 Skill 的功能存在重叠，使用时应以项目当前版本的 README、SKILL.md 和实际输出为准。星标数量会变化，视频录制时请以 GitHub 页面当天显示的数据为准。
