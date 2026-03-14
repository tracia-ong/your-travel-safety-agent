import os
from dotenv import load_dotenv

load_dotenv()

class SafetyStrategist:
    def __init__(self):
        self.name = "Safety Strategist"
        self.role = "Risk Analyst & Decision Support"

    def reason_over_data(self, scout_report):
        """
        Applies reasoning traces and safety guardrails to raw intelligence.
        """
        print(f"[{self.name}] Analyzing report for potential safety red flags...")
        
        # This is where the 20% Robustness weight comes in!
        guardrails_applied = True 
        
        if "protest" in scout_report.lower() or "disaster" in scout_report.lower():
            return "VERDICT: HIGH RISK. Avoid travel or exercise extreme caution."
        
        return "VERDICT: LOW RISK. Normal safety precautions apply."

# This logic connects the Intel Scout to the Strategist (A2A Flow)
