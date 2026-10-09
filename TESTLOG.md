# TESTLOG — skill-forge 的"事故 → 规则"证据链

每一条规则都由一次真实测试失败驱动，不是设计出来的。映射如下：

| 版本 | 测试 | 事故/发现 | 回灌规则 |
|---|---|---|---|
| v0.1 | code-quality-guard 试用 | 自评路由分虚高；无 e2e 证据；问题无预算 | B 轴用户确认、e2e trial 必做、10 问预算 + 爆炸半径排序、凭据一级护栏 |
| v0.3 | wxarticle 双轨对决 | 官方版产出更锐但**编造 47% 数据** | B5a 受众 / B5b 断言溯源 / B5c craft 笔记（E 轴 30 分） |
| v0.3.2 | 多话题（4 个）盲测 | "反直觉角度"规则在客户汇报话题上**无处可违反** | craft 笔记必须带降级路径，否则 E 轴 0 分 |
| v0.4 | port docx/brave/browser-tools | docx 是 Anthropic **专有授权**却整件搬运（事故级）；隐式依赖 defusedxml 首跑即炸；原版漏文档 1 个脚本 | B0 license gate、依赖清单 grep 得出、脚本覆盖 1:1（D 轴 +5）、porting 模式 |
| v0.5 | port webapp-testing/frontend-design/doc-coauthoring | 黑盒 helper"别读源码"无原因；纯 craft 无脚本怎么算可执行；交互门无出口条件 | 上下文卫生规则、E 轴可检查锚点、B11 交互门分支、依赖清单到二进制层 |
| v0.6 | port claude-api 路由层 + mcp-builder | 异构 provider 污染（拿 Anthropic 调用改 openai 文件）；训练先验过期（budget_tokens 直接 400）；裸 subcommand 被当 prose | 污染门、防漂移表、subcommand 表面（B12 分支） |
| v0.7 | 作品集对决（port 规则 vs 官方规则） | 两版都命中“中间点 meta”指纹而**视觉自审都没拦住** | craft skill 必须带可执行 audit step：产物完成后逐条交叉核对 tells 清单并出命中记录（frontend-design-port 已落地） |
| v0.8 | 野生库审计（dv360/google/meta/tiktok 五件套） | dv360：45 个外部工具无注册检查、脚本路径指向不存在的目录、微秒/毫秒单位陷阱、无限审批轮询、删/改预算无确认门；google-ads：参数表摆出 token | **野生审计模式**（四项确定性检查：外部面前置门/路径真实性/领域陷阱/无界循环与破坏性门）；已 patch dv360 + google-ads 本体 |
| v0.9 | 触发率自动回归（harness 落地） | 官方 run_eval.py 绑死 claude -p 不可移植；手写探针标注错（把别的 skill 的正路由误标成 NO_SKILL，虚报了 2 个 FP） | **工具无关三件套**：`tests/<skill>/prompts.json`（≥10 探针）+ agent 新会话路由判定 + `scripts/trigger_score.py`（P/R/F1 + 基线 delta）；B 轴改为“数字基线 + 用户拍板”；wxarticle 首发基线 F1=1.0 已落盘 |
| v1.0 | **docx 盲建对决**（skill-forge 从零造 docx-forge vs 官方 docx，同工件 8 步） | 官方 0/8 闭环：docx-js “预装”不实、comment.py 在本机无任何可用 Python（3.9 语法炸/3.12 缺 defusedxml）、soffice/pandoc 缺失；同时官方胜在触发面 + 12 条领域纵深 gotcha；自检修件又抓出一个自检器命名空间 bug 误报 | ① B5c 加 provenance 标签（measured/upstream/user，传闻降分）② 环境假设三件套（探测+安装+降级，未探测断言 E 轴 0 分）③ 交付型 skill 必须带 exit-code 自检且自检器自身先过单测；docx-forge 本体（双脚本+自检+试金石）留在本地 |
| v1.1 | **第二遍密度回补**（同一 docx-forge 开 provenance 规则追平官方） | 上游文本里一次性挖出 7 条本 skill 缺的 gotcha（run 碎片/外部 docx symlink 安全/tracked changes 机制/空 bullet 假象/表格双宽度/tab leader/样式名）；f-string 反斜杠在 py3.9 炸（老代码假设 3.12+） | **领域密度 floor**（E 轴：对标 skill 必须按 gotcha 类别 match-or-declare，缺类需声明“未实现·文档位”）；探索先挖本地来源（官方 gotcha 文本即现成上游） |

## 当前形态覆盖

脚本重资产 / 轻脚本工具集 / 纯 craft / 多门交互流 / 巨型参考路由层 / 脚手架+评测 / **野生单文件（五件套，含 2 个已 patch）** / **触发回归 harness（wxarticle 基线 F1=1.0）** —— 八类全有对照、审计或基线。
