from typing import Any, Literal

from pydantic import BaseModel, Field


class TimeWindow(BaseModel):
    start_minutes: int
    end_minutes: int


class PopulationSpec(BaseModel):
    description: str
    inclusion_criteria: list[str] = Field(default_factory=list)
    exclusion_criteria: list[str] = Field(default_factory=list)


class OutcomeSpec(BaseModel):
    name: str
    definition: str | None = None


class ResearchQuestion(BaseModel):
    question_id: str
    version: str
    study_id: str
    study_title: str
    question_class: Literal[
        "descriptive",
        "association",
        "prediction",
        "time-to-event",
        "longitudinal repeated-measure",
        "subgroup analysis",
        "sensitivity analysis",
    ]
    clinical_context: str
    study_mode: Literal["confirmatory", "exploratory"]
    unit_of_analysis: Literal["patient", "hospital_admission", "icu_stay"]
    population: PopulationSpec
    exposure: dict[str, Any] | None = None
    comparator: dict[str, Any] | None = None
    primary_outcome: OutcomeSpec
    secondary_outcomes: list[OutcomeSpec] = Field(default_factory=list)
    time_zero: str
    baseline_window: TimeWindow
    followup_window: TimeWindow
    key_confounders: list[str] = Field(default_factory=list)
    estimand: dict[str, Any]


class VariableMappingItem(BaseModel):
    analysis_variable: str
    variable_class: Literal[
        "exposure",
        "comparator",
        "primary_outcome",
        "secondary_outcome",
        "baseline_covariate",
        "stratification",
        "sensitivity",
        "derived",
    ]
    status: Literal["mapped", "missing", "proposed"]
    source_layer: str | None = None
    source_location: str | None = None
    source_field: str | None = None
    standard_variable_name: str | None = None
    unit: str | None = None
    derivation_rule: str | None = None
    time_window: TimeWindow | None = None
    notes: str | None = None


class VariableMapping(BaseModel):
    mapping_id: str
    version: str
    study_id: str
    question_id: str
    variables: list[VariableMappingItem]
    missing_variable_report: list[dict[str, Any]] = Field(default_factory=list)


class AnalysisPlan(BaseModel):
    plan_id: str
    version: str
    study_id: str
    question_id: str
    question_class: str
    unit_of_analysis: str
    time_zero: str
    primary_endpoint: dict[str, Any]
    secondary_endpoints: list[str] = Field(default_factory=list)
    exposure: dict[str, Any] | None = None
    covariates: dict[str, Any] = Field(default_factory=dict)
    primary_analysis: dict[str, Any]
    secondary_analyses: list[dict[str, Any]] = Field(default_factory=list)
    subgroup_analyses: list[dict[str, Any]] = Field(default_factory=list)
    sensitivity_analyses: list[dict[str, Any]] = Field(default_factory=list)
    missing_data: dict[str, Any]
    model_diagnostics: list[str] = Field(default_factory=list)
    multiplicity: dict[str, Any] = Field(default_factory=dict)
    outputs: dict[str, Any] = Field(default_factory=dict)
    interpretation_boundary: dict[str, Any]


class CodeArtifact(BaseModel):
    code_artifact_id: str
    version: str
    study_id: str
    plan_id: str
    language: Literal["python", "r", "sql", "mixed"]
    entrypoint: str
    generated_files: list[str]
    dependencies: list[str] = Field(default_factory=list)
    input_datasets: list[str] = Field(default_factory=list)
    planned_outputs: list[str] = Field(default_factory=list)
    code_hash: str | None = None
    notes: str | None = None


class ResultArtifact(BaseModel):
    result_artifact_id: str
    version: str
    study_id: str
    plan_id: str
    run_id: str
    artifact_type: Literal["table", "figure", "metric", "model_output", "validation_report"]
    label: str
    path: str | None = None
    source_code_artifact_id: str
    dataset_version: str | None = None
    statistical_summary: dict[str, Any] = Field(default_factory=dict)
    validation_status: Literal["pending", "passed", "failed"] = "pending"


class InterpretationClaim(BaseModel):
    claim_id: str
    claim_type: Literal["fact", "statistical_result", "interpretation", "hypothesis"]
    text: str
    supported_result_artifact_ids: list[str]
    confidence_note: str | None = None


class Interpretation(BaseModel):
    interpretation_id: str
    version: str
    study_id: str
    plan_id: str
    claims: list[InterpretationClaim]
    limitations: list[str] = Field(default_factory=list)
    forbidden_claim_check: str | None = None


class TraceBundle(BaseModel):
    trace_bundle_id: str
    version: str
    study_id: str
    question_id: str
    plan_id: str
    dataset_version: str
    code_artifact_ids: list[str]
    result_artifact_ids: list[str]
    interpretation_id: str | None = None
    decision_log_ids: list[str]
    run_ids: list[str] = Field(default_factory=list)
    approval_nodes: list[str] = Field(default_factory=list)


class IdeaSummary(BaseModel):
    idea_id: str
    version: str
    study_id: str
    title: str
    category: Literal["near-scope extension", "future analysis candidate", "out-of-scope idea"]
    summary: str
    rationale: str | None = None
    promotion_condition: str | None = None
    execution_status: Literal["summary_only", "pending_approval", "promoted"]
