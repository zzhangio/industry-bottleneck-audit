# Industry Bottleneck Audit

这个 Skill 用于分析行业窄口、议价权、技术冲击和结构迁移。用户只需要选择两种深度之一：

- **快速版（默认）：** 首次了解行业、判断一项新技术可能改变什么，或用一条新证据更新旧结论。
- **完整版：** 需要可审计报告、可复用数据、正式验证、版本重建或冲突裁决。

行业优先、技术冲击、时间更新和公司捕获属于内部分析路线，不需要用户提前分类。

## 安装

在本目录运行幂等安装脚本；首次安装和重复升级都会复制目录内容，并校验 SHA-256，不会生成嵌套的 skill 目录：

```powershell
.\scripts\install_skill.ps1
```

macOS 或 Linux（在本 Skill 目录运行）：

```bash
mkdir -p ~/.codex/skills/industry-bottleneck-audit
cp -R ./. ~/.codex/skills/industry-bottleneck-audit/
```

也可以在代理任务中直接附加本目录的 `SKILL.md` 及其 `references/`、`schemas/` 和 `scripts/`。复制后重新开始任务，使代理重新发现 Skill。

快速版不需要 Python 依赖。完整版若要校验 canonical audit bundle，安装 Draft 2020-12 Schema 校验依赖：

```bash
python -m pip install -r requirements.txt
```

## 使用

快速版示例：

```text
使用 $industry-bottleneck-audit 快速分析 AI 短剧行业：生成成本下降后，议价权会迁移到哪里？
```

完整版示例：

```text
使用 $industry-bottleneck-audit 完整审计先进封装产业链，保留来源、公司映射、反例、证伪条件和后续更新触发器。
```

如果未指定深度，默认先做快速版。明确要求深度、正式或可审计交付时，直接进入完整版。

## 可视化预览

快速版可直接在 Markdown 中生成一张小型 Mermaid 控制图。完整版或需要半年后复查的案例，先校验 canonical bundle，再生成单文件交互式 HTML：

```powershell
python scripts/validate_audit_bundle.py examples/minimal-audit-bundle.json
python scripts/render_audit_visual.py examples/minimal-audit-bundle.json output/audit-preview.html
```

HTML 不依赖外部前端库，可离线打开；节点可点击查看 Gate/Leverage 机制、公司映射、证据、未知项、证伪条件和复查触发器。图只是同一审计 bundle 的视图，不维护第二套结论。

交互式 HTML 使用与 `SKILL.md` 和 `references/visualization.md` 一致的制作与验收流程：优先由独立代理负责视觉制作，主代理核对事实、证据和结论边界，并完成浏览器、交互、移动端和溢出检查。`gpt-6-astra`、`medium` reasoning 是推荐配置，不是运行依赖；其他模型执行相同检查，并记录实际配置。没有独立代理时可分阶段自检，但须披露并非独立复核。检查未完成的 HTML 只能标为 `draft_visual_review_pending`，不得称已验收；过程记录在 HTML 同目录的 `visual-review.md`。详见 [可视化规范](references/visualization.md)。

## 搜索与云端环境

AnySearch 不是运行依赖，也不随仓库分发。代理可以使用当前环境允许的搜索工具，也可以使用用户提供的、可追溯的来源包。

如果云端没有 AnySearch：

1. 使用环境已有的网页搜索或专业数据连接器，并记录实际使用的来源。
2. 没有任何搜索能力时，要求或读取用户提供的证据包。
3. 证据仍不足时，只输出范围、候选路径、未知项和调查计划，标记为 `tool_blocked` 或证据不足；不要声称已经完成当前行业审计。

不要把 API key、`.env`、本地认证配置、私有日志或个人绝对路径提交到仓库。

## 验证

在公开仓库根目录运行（不是本 Skill 目录）：

```bash
python skill/industry-bottleneck-audit/scripts/validate_audit_bundle.py --self-test
python -m unittest skill/industry-bottleneck-audit/scripts/test_validate_audit_bundle.py
python -m unittest skill/industry-bottleneck-audit/scripts/test_render_audit_visual.py
python skill/industry-bottleneck-audit/scripts/validate_audit_bundle.py skill/industry-bottleneck-audit/examples/minimal-audit-bundle.json skill/industry-bottleneck-audit/examples/minimal-non-cone-bundle.json skill/industry-bottleneck-audit/examples/minimal-unresolved-bundle.json
```

Windows PowerShell 安装脚本测试（仅在有 PowerShell 的环境运行）：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File skill/industry-bottleneck-audit/scripts/test_install_skill.ps1
```

Schema `1.0-draft.3` 拒绝非整数值的小数伪精度（数值 `2` 与 `2.0` 一致接受），支持带解释的 `point/range/unknown/not_applicable` 分值，并要求新 bundle 为节点记录 Gate/Leverage 机制与相对激活条件。组织型冲击可记录 capability scope、adoption position 和管辖权迁移；事件驱动研究还可记录从发散网络到收敛候选或成形聚类的 `topology_transitions`，以及替代松动、互补激活、接口收敛、需求扩张/市场剪枝机制。旧 `1.0-draft` 至 `1.0-draft.2` 暂时兼容但会进入迁移路径；新 bundle 应使用 `1.0-draft.3`。验证 PASS 只说明结构和交叉引用满足机器契约，不说明事实、因果或预测正确。

封存快照会检查直接证据及其 claim 引用的**精确假设版本**的支持证据。未来预测、无证据的待验证推断和未被旧快照引用的新资料可以保留；后验验证用新事件/版本记录，不回填旧版本的当时依据。未知来源日期会警告，不能据此声称历史一致性已验证。详见 `references/temporal-validation.md`。带解释的评分不接受纯空白解释。

旧 bundle 迁移时不要改写原始时间切片。创建派生版本，并做三类显式归一化：把叙事式或多重分类拆成一个合法 `classification`，其余判断放入 `alternatives/largest_unknowns`；把自定义来源类型映射到 Schema 的 `official/regulatory/company/paper/market_data/industry/media/other`；若旧快照引用了截止日后的材料，保留旧文件并重建新的快照边界或证据集合，不得倒填发布日期。

可用 `scripts/migrate_bundle_v012.py SOURCE TARGET` 创建不覆盖原件的机械迁移草稿。它只补齐未知评分、Gate/Leverage 占位、来源类型、规模平衡和 v0.12 容器；历史证据污染、复合 claim 与快照边界仍必须人工切分并重新验证。

可选：若本机安装了 Codex `skill-creator`，可另用其 `quick_validate.py` 检查 Skill 元数据；它不是公开包的运行依赖。公开 beta 的能力边界、示例与反馈方式见仓库根 `README.md`；私有评测记录不随公开包分发。
