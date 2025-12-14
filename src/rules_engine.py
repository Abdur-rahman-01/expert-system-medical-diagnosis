"""
Rule-based inference engine. Rules can be loaded from JSON or defined inline.
Each rule is a dict with: name, conditions (list), severity, emergency, explanation.
"""

from typing import Dict, List

DEFAULT_RULES = [
    {"name": "Flu", "conditions": ["fever","cough","sore_throat"], "severity":"Moderate", "emergency":False, "explanation":"Viral respiratory infection"},
    {"name": "Common Cold", "conditions": ["runny_nose","sore_throat","cough"], "severity":"Mild", "emergency":False, "explanation":"Upper respiratory infection"},
    {"name": "Malaria", "conditions": ["fever","chills","sweating"], "severity":"Severe", "emergency":False, "explanation":"Parasitic infection — check malaria test"},
    {"name": "Dengue", "conditions": ["fever","headache","body_pain"], "severity":"Severe", "emergency":False, "explanation":"Consider dengue — test platelet counts"},
    {"name": "Heart Attack (Possible)", "conditions":["chest_pain","shortness_breath","fatigue"], "severity":"Critical", "emergency":True, "explanation":"Possible cardiac event — immediate attention"},
    {"name": "Food Poisoning", "conditions":["nausea","vomiting","abdominal_pain"], "severity":"Moderate", "emergency":False, "explanation":"Gastrointestinal infection"},
    {"name": "Asthma Attack", "conditions":["shortness_breath","cough"], "severity":"Severe", "emergency":True, "explanation":"Respiratory distress requiring prompt care"},
    {"name": "Hypoglycemia", "conditions":["sweating","headache","fatigue"], "severity":"Moderate", "emergency":False, "explanation":"Low blood sugar episode"},
    {"name": "Dengue Fever", "conditions":["fever","chills","body_pain"], "severity":"Mild", "emergency":False, "explanation":"Likely due to fluid loss"},
    {"name": "Pneumonia", "conditions": ["fever","cough","shortness_breath","chest_pain"], "severity":"Severe", "emergency":True, "explanation":"Lung infection requiring medical attention"},
    {"name": "COVID-19", "conditions": ["fever","cough","sore_throat","fatigue","headache"], "severity":"Severe", "emergency":False, "explanation":"Viral respiratory illness"},
    {"name": "Gastroenteritis", "conditions": ["nausea","vomiting","abdominal_pain","fever"], "severity":"Moderate", "emergency":False, "explanation":"Stomach flu or food-related illness"},
    {"name": "Migraine", "conditions": ["headache","nausea","vomiting","fatigue"], "severity":"Moderate", "emergency":False, "explanation":"Severe headache with neurological symptoms"},
    {"name": "Bronchitis", "conditions": ["cough","sore_throat","chest_pain","fatigue"], "severity":"Moderate", "emergency":False, "explanation":"Inflammation of the bronchial tubes"},
    {"name": "Typhoid", "conditions": ["fever","headache","abdominal_pain","fatigue"], "severity":"Severe", "emergency":False, "explanation":"Bacterial infection affecting the intestines"},
    {"name": "Tuberculosis", "conditions": ["cough","fever","sweating","shortness_breath"], "severity":"Severe", "emergency":False, "explanation":"Bacterial lung infection"},
    {"name": "Chickenpox", "conditions": ["fever","body_pain","headache","fatigue"], "severity":"Moderate", "emergency":False, "explanation":"Viral infection with characteristic rash"},
    {"name": "Urinary Tract Infection", "conditions": ["abdominal_pain","nausea","fever","fatigue"], "severity":"Moderate", "emergency":False, "explanation":"Bacterial infection of the urinary system"},
    {"name": "Appendicitis", "conditions": ["abdominal_pain","nausea","vomiting","fever"], "severity":"Severe", "emergency":True, "explanation":"Inflammation of the appendix requiring surgery"},
    {"name": "Anxiety Attack", "conditions": ["shortness_breath","chest_pain","sweating","headache"], "severity":"Moderate", "emergency":False, "explanation":"Panic or anxiety episode"},
    {"name": "Diabetes Complication", "conditions": ["fatigue","nausea","sweating","headache"], "severity":"Moderate", "emergency":False, "explanation":"Possible hypo/hyperglycemia or related issue"}
]

class RuleEngine:
    def __init__(self, rules: List[dict] = None):
        self.rules = rules or DEFAULT_RULES

    def evaluate(self, facts: Dict[str, bool]) -> List[dict]:
        """
        facts: mapping of symptom -> boolean
        """
        matched = []
        for r in self.rules:
            if all(facts.get(cond, False) for cond in r["conditions"]):
                matched.append(r)
        return matched
