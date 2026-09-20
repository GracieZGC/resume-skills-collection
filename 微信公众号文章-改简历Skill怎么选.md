# 改简历的 Skill 太多了，到底该装哪个？一篇文章帮你选对

最近很多人开始用 AI 改简历，但很快就会遇到一个新问题：

GitHub 上的简历 Skill 越来越多，名字看起来都差不多，介绍也都写着“优化简历”“提高匹配度”“支持 ATS”。到底该装哪个？是不是装得越多越好？

其实，改简历不是一个单一动作。你可能是没有材料、不知道哪些经历值得写；也可能已经有简历，只是表达空泛；或者简历内容没问题，但投递某个岗位时不知道怎么针对性修改。

所以，选 Skill 之前，先别看它能不能“改简历”，而要先看：它主要帮你解决哪一种问题。

<!-- 配图：01-分类总表.png（本地文件夹：/Users/guanchenzhan/Desktop/AI改简历skill） -->

## 一、信息整合：我根本不知道简历从哪里开始写

如果你手里没有完整简历，只有一些工作流水账、项目文档，甚至只是“我做过运营、写过文章、参加过活动”这样的零散描述，优先看信息整合类 Skill。

代表工具是 [resume-builder-skill](https://github.com/Jichengyuuuuu/resume-builder-skill)。它的重点不是把现成简历润色得更漂亮，而是先帮你收集和整理材料：你可以提供旧简历、岗位 JD、工作记录或项目文档，它再通过模板和必要追问，把这些信息整理成一份简历初稿。

这类 Skill 适合解决的是：

> “我想找工作，但我甚至不知道自己做过的哪些事情值得写。”

如果你正处在从零开始的阶段，直接让普通 AI“帮我写一份简历”，很容易得到一份看起来完整、但内容非常泛的模板。先把材料收集完整，通常比先追求措辞高级更重要。

## 二、岗位定制：我的经历不少，但不知道怎么投这个岗位

如果你已经有一份主简历，现在要投某个具体岗位，就应该看岗位定制类 Skill。

比较典型的有 [resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill) 和 [resume-tailor](https://github.com/nuin/resume-tailor)。它们的工作方式通常是：先分析 JD，提取岗位需要的能力、经验和关键词，再从你的真实经历中挑选相关内容，重新组织成一版更贴合岗位的简历。

这和普通的“润色”不一样。普通润色可能只把“负责活动运营”改成更专业的句子；岗位定制则会进一步思考：这个岗位更看重用户增长、活动转化，还是数据分析？你的哪段经历最能证明这些能力？应该把哪一段放在前面？

如果现有经历写得不清楚，这类 Skill 也可能继续追问，比如：你具体负责了什么？服务了多少用户？最后产生了什么结果？但要注意，它只能帮你把已有经历问清楚，不能替你凭空创造经历和数据。

## 三、内容诊断与重写：简历有了，但看起来很普通

很多人并不是没有简历，而是简历里的内容全是“负责、参与、协助”，读完之后看不出个人贡献，也不知道哪些地方最需要修改。

这时可以看 [resume-optimizer-claude-skill](https://github.com/Sumukhmg/resume-optimizer-claude-skill)。它更像一次偏 HR 视角的内容体检：检查结构是否清楚、表达是否具体、成果是否突出，并根据现有事实重写薄弱部分。

它的重点是“内容质量”，包括：

- 工作经历是不是只写了职责，没有写结果；
- 项目描述能不能看出你的个人作用；
- 重要经历有没有被放在合适的位置；
- 语言是否重复、空泛或过度包装；
- 缺少数据的地方，是否明确标记出来让你补充。

它也可能追问经历，所以它和信息整合类 Skill 会有重叠。但两者的主要用途不同：前者更偏“把已有简历诊断并重写”，后者更偏“把零散材料整理成简历”。

## 四、ATS 检查：我担心简历根本没有被系统正确读到

有些公司会先用招聘系统处理简历。如果你担心关键词覆盖、文件结构或解析效果，可以看 [resume-ats-optimizer](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/career/resume-ats-optimizer/SKILL.md)。

它主要检查：

- 目标岗位的重要关键词是否覆盖；
- 栏目结构是否清楚、标准；
- 文件中是否有表格、图片、文本框等解析风险；
- 招聘系统能不能正确识别你的联系方式、经历和教育背景。

它和内容诊断类 Skill 也会重叠，但关注点不同：

> `resume-optimizer` 更关心 HR 看起来顺不顺；`resume-ats-optimizer` 更关心招聘系统读不读得懂。

ATS 检查并不等于“通过了就一定能获得面试”。它只能帮助你减少格式和关键词层面的损耗，真正的岗位匹配仍然要回到经历本身。

## 五、排版导出：内容已经确定，只差一份能投的 PDF

如果简历内容已经确认，只是 Word 排版混乱、分页不好看，或者想把 Markdown 稳定地转换成 PDF，可以看 [resume-md-skill](https://github.com/beholder91/resume-md-skill)。

它更像一个排版和渲染工具，重点处理字体、层级、分页、留白和 PDF 导出，而不是帮你重新发明经历。

这类工具适合放在流程的最后。内容还没确定时就急着调整字号和间距，往往是在排版上反复折腾，最后内容一改又要重新排。

## 六、想一次拿到多个模块：模块化工具箱

如果你既想改写，又想做 ATS 检查、量化成果、岗位定制和版本管理，可以看看 [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)。

它更像一套模块化工具箱，里面包含多个独立功能。它的价值不在于“所有步骤必须一起跑”，而在于你可以根据需要调用不同模块：缺内容就用内容相关功能，要匹配 JD 就调用岗位定制，要检查格式就调用 ATS 或排版模块。

<!-- 配图：08-ResumeSkills.png（本地文件夹：/Users/guanchenzhan/Desktop/AI改简历skill） -->

模块化工具箱适合已经知道自己缺什么的人。如果你还没判断问题，就把所有模块一起运行，反而可能得到一份很长的报告，消耗更多时间和 Token。

## 推荐的使用顺序

如果你需要从零开始，可以参考这个顺序：

1. 先用 `resume-builder` 整理零散经历，形成主简历；
2. 用 `resume-optimizer` 做内容诊断和重写；
3. 针对具体岗位，用 `resume-tailoring` 或 `resume-tailor` 定制版本；
4. 用 `resume-ats-optimizer` 检查关键词和解析风险；
5. 最后用 `resume-md` 排版并导出 PDF。

<!-- 配图：02-推荐顺序.png（本地文件夹：/Users/guanchenzhan/Desktop/AI改简历skill） -->

但这不是强制流程。如果你已经有一份内容成熟的简历，就不需要重新从 `resume-builder` 开始；如果你只是想针对一个岗位投递，也不必先把所有工具都装一遍。

## 最后：不要按“能不能改简历”来选

这些 Skill 的功能确实会重叠。能追问经历的不一定就是素材整理工具，能输出诊断报告的也不一定只做 ATS 检查。更准确的判断方式是看它的主要输入、主要输出和主要评价标准：

- 输入是零散材料，输出是完整简历，通常偏信息整合；
- 输入是简历和 JD，输出是岗位版本，通常偏岗位定制；
- 输入是现有简历，输出是问题报告和重写稿，通常偏内容诊断；
- 输入是简历文件，输出是关键词和格式检查，通常偏 ATS；
- 输入是确定内容，输出是 PDF，通常偏排版渲染。

先判断自己缺哪一块，再选对应的套餐。工具装得少一点，问题反而更容易看清楚。

> 说明：Skill 的功能和安装方式可能随项目更新。使用前请查看对应仓库最新的 README 和 `SKILL.md`，不要让 AI 编造经历、数据或技能。

## 相关项目

- [resume-builder-skill](https://github.com/Jichengyuuuuu/resume-builder-skill)
- [resume-tailoring-skill](https://github.com/varunr89/resume-tailoring-skill)
- [resume-optimizer-claude-skill](https://github.com/Sumukhmg/resume-optimizer-claude-skill)
- [resume-ats-optimizer](https://github.com/davila7/claude-code-templates/blob/main/cli-tool/components/skills/career/resume-ats-optimizer/SKILL.md)
- [resume-md-skill](https://github.com/beholder91/resume-md-skill)
- [resume-tailor](https://github.com/nuin/resume-tailor)
- [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills)
