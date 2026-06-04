import json
from google import genai
from pydantic import BaseModel
from src.state import SupplyChainState
from src.tools import query_inventory

client = genai.Client()

class TelemetryExtraction(BaseModel):
    sku: str
    anomaly_type: str

def telemetry_node(state: SupplyChainState) -> dict:
    event = state["telemetry_event"]
    
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=f"Extract the primary SKU and the exact nature of the disruption from this event log: {event}",
        config={
            "response_mime_type": "application/json",
            "response_schema": TelemetryExtraction,
        },
    )
    
    parsed = json.loads(response.text)
    return {
        "extracted_sku": parsed.get("sku"), 
        "anomaly_type": parsed.get("anomaly_type")
    }

def diagnostic_node(state: SupplyChainState) -> dict:
    sku = state["extracted_sku"]
    inventory_data = query_inventory(sku)
    
    impact_context = (
        f"Inventory State for {sku}: {json.dumps(inventory_data)}. "
        f"Active Anomaly: {state['anomaly_type']}"
    )
    return {"impact_analysis": impact_context}

def strategist_node(state: SupplyChainState) -> dict:
    impact = state["impact_analysis"]
    
    prompt = (
        "You are an industrial operations strategist. Based on the following impact analysis, "
        "output a strict, three-step operational mitigation plan to prevent a stockout or production halt. "
        f"Data: {impact}"
    )
    
    response = client.models.generate_content(
        model='gemini-3.5-flash',
        contents=prompt
    )
    
    return {"mitigation_plan": response.text}