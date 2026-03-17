# 重症科研多智能体系统 - v1.0.0

这是项目第一版可执行范围定义目录。

长期愿景仍保留在 `../Guideline/`，这里不碰愿景层，只建设第一步真正能落地、能审计、能逐步实现的系统骨架。

## v1 定位

`v1.0.0` 是一个聚焦的重症医学数据库科研助手，不是全自动科研实验室。

它的边界是刻意收窄的：
- 领域边界：急诊、ICU、重症数据库研究
- 任务边界：结构化临床数据库分析
- 输出边界：研究问题结构化、分析计划、可复现代码、结果表图、保守解释
- 安全边界：所有正式结论都必须能回溯到数据、代码、执行、验证与审计
- 交互边界：允许提出旁支想法，但默认只做结构化总结，不自动深挖执行

## 目录结构

- `docs/` - 范围、架构、工作流、状态机、审批规则、handoff、traceability、audit、验收与复核规范
- `agents/` - v1 角色定义
- `schemas/` - 结构化对象 schema 与 Pydantic 模型
- `scripts/` - 机器可执行工作流骨架与后续 orchestration glue
- `examples/` - 示例输入输出占位
- `outputs/` - 未来任务运行产物目录

## 工作流骨架入口

v1 第一版“机器版骨架”现在已经补上，核心入口如下：

- `default_pipeline.json` - 机器可读的默认流程顺序、状态流转、审批闸口、回退节点、发布要求
- `docs/workflow_state_machine.md` - 文档版状态机说明，与 `default_pipeline.json` 一一对应
- `docs/policy_engine_rules.yaml` - guardrails / policy engine 规则骨架，对齐 `docs/approval_matrix.md`
- `docs/handoff_contracts.md` - agent 间结构化交接契约
- `run_manifest.json` - 每个 task 的运行清单模板，承载状态、trace 指针、audit 路径
- `scripts/run_backend.py` - 最小可执行骨架：初始化任务、检查状态、校验状态迁移是否合法

## 第二阶段补齐的审计与可复现层

- `docs/traceability_spec.md`
- `docs/audit_log_spec.md`
- `docs/artifact_store_layout.md`
- `docs/success_criteria.md`
- `docs/acceptance_criteria_v1.md`
- `docs/review_checklist.md`
- `run_manifest.json`

## 一个最小用法

```bash
python scripts/run_backend.py init \
  --task-id task_demo_001 \
  --task-mode clinical_db_analysis \
  --title "ICU vasopressor exposure and 28-day mortality"

python scripts/run_backend.py inspect --task-id task_demo_001
python scripts/run_backend.py transition --task-id task_demo_001 --next-state intake_ready --actor orchestrator-agent --note "Question intake completed"
```

## 当前含义

现在这个目录已经具备：
- 愿景与执行分层
- 规则层、气质层、角色层、对象层、审批层
- 机器流程层初版骨架
- 审计与可复现层初版规范

但仍未进入：
- 真正运行时编排实现
- skill 复用与窄化包装
- 黄金样例贯通演练
- 真实数据跑通与回归测试

## 关系说明

- 长期战略北极星：`../Guideline/`
- 当前执行骨架：`v1.0.0/`
- 上游数据底座参考：`D:\Database\FRAMEWORK_v4_COMPLETE.md`

这个目录的目标不是“看起来很强”，而是先把第一版骨架做得清楚、保守、能审计、能继续实现。
