import os
from dotenv import load_dotenv

# 1. Load secrets into system memory FIRST
load_dotenv()

# 2. Execute local imports dependent on those secrets
from langgraph.graph import StateGraph, END
from src.state import SupplyChainState
from src.agents import telemetry_node, diagnostic_node, strategist_node

# Initialize the state machine
workflow = StateGraph(SupplyChainState)

# Register functional nodes
workflow.add_node("telemetry", telemetry_node)
workflow.add_node("diagnostic", diagnostic_node)
workflow.add_node("strategist", strategist_node)

# Define the deterministic execution graph
workflow.set_entry_point("telemetry")
workflow.add_edge("telemetry", "diagnostic")
workflow.add_edge("diagnostic", "strategist")
workflow.add_edge("strategist", END)

# Compile into an executable application
app = workflow.compile()

# Test Payload Execution
if __name__ == "__main__":
    initial_state = {
        "telemetry_event": "CRITICAL ALARM: Thermal sensor malfunction on assembly line B. Expected throughput delay of 48 hours. Affected component: SKU-77A.",
        "errors": []
    }
    
    print("Executing Graph Workflow...\n")
    result = app.invoke(initial_state)
    
    print("--- State Updates ---")
    print(f"Extracted SKU: {result.get('extracted_sku')}")
    print(f"Anomaly: {result.get('anomaly_type')}")
    print(f"Impact: {result.get('impact_analysis')}\n")
    
    print("--- Final Mitigation Plan ---")
    print(result.get("mitigation_plan"))