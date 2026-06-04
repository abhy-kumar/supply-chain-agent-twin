from typing import TypedDict, Annotated, List
import operator

class SupplyChainState(TypedDict):
    telemetry_event: str
    extracted_sku: str
    anomaly_type: str
    impact_analysis: str
    mitigation_plan: str
    errors: Annotated[List[str], operator.add]