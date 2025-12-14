def medical_diagnosis():
    print("\n============================================")
    print("      SIMPLE MEDICAL DIAGNOSIS SYSTEM")
    print("============================================")
    print("Answer with 'yes' or 'no'. Anything else counts as 'no'.\n")

    # -----------------------------------------
    # 1. COLLECT SYMPTOMS
    # -----------------------------------------
    questions = {
        "fever": "Do you have fever? ",
        "cough": "Do you have cough? ",
        "sore_throat": "Do you have sore throat? ",
        "chills": "Do you have chills? ",
        "sweating": "Do you have sweating? ",
        "headache": "Do you have headache? ",
        "body_pain": "Do you have body pain? ",
        "runny_nose": "Do you have runny nose? ",
        "nausea": "Do you have nausea? ",
        "vomiting": "Do you have vomiting? ",
        "abdominal_pain": "Do you have abdominal pain? ",
        "shortness_breath": "Do you have shortness of breath? ",
        "chest_pain": "Do you have chest pain? ",
        "fatigue": "Do you feel fatigue? ",
    }

    symptoms = {key: (input(text).lower() == "yes") for key, text in questions.items()}

    # -----------------------------------------
    # 2. RULE BASE
    # -----------------------------------------
    rules = [
        {
            "name": "Flu",
            "conditions": ["fever", "cough", "sore_throat"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Classic viral infection triad."
        },
        {
            "name": "Common Cold",
            "conditions": ["runny_nose", "sore_throat", "cough"],
            "severity": "Mild",
            "emergency": False,
            "explanation": "Likely upper respiratory tract infection."
        },
        {
            "name": "Malaria",
            "conditions": ["fever", "chills", "sweating"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "Fever with chills + sweating is typical malarial pattern."
        },
        {
            "name": "Dengue",
            "conditions": ["fever", "headache", "body_pain"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "High fever + severe body ache suggests dengue-like profile."
        },
        {
            "name": "Food Poisoning",
            "conditions": ["nausea", "vomiting", "abdominal_pain"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "GI symptoms indicate food contamination."
        },
        {
            "name": "Heart Attack (Possible)",
            "conditions": ["chest_pain", "shortness_breath", "fatigue"],
            "severity": "Critical",
            "emergency": True,
            "explanation": "Chest pain with breathlessness can signal cardiac emergency."
        },
        {
            "name": "Asthma Attack",
            "conditions": ["shortness_breath", "cough"],
            "severity": "Severe",
            "emergency": True,
            "explanation": "Breathing difficulty with cough suggests airway narrowing."
        },
        {
            "name": "Hypoglycemia",
            "conditions": ["sweating", "headache", "fatigue"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Low blood sugar episode."
        },
        {
            "name": "Dengue Fever",
            "conditions": ["fever", "chills", "body_pain"],
            "severity": "Mild",
            "emergency": False,
            "explanation": "Viral infection with fever, chills, and body pain."
        },
        {
            "name": "Pneumonia",
            "conditions": ["fever", "cough", "shortness_breath", "chest_pain"],
            "severity": "Severe",
            "emergency": True,
            "explanation": "Lung infection requiring medical attention."
        },
        {
            "name": "COVID-19",
            "conditions": ["fever", "cough", "sore_throat", "fatigue", "headache"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "Viral respiratory illness."
        },
        {
            "name": "Gastroenteritis",
            "conditions": ["nausea", "vomiting", "abdominal_pain", "fever"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Stomach flu or food-related illness."
        },
        {
            "name": "Migraine",
            "conditions": ["headache", "nausea", "vomiting", "fatigue"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Severe headache with neurological symptoms."
        },
        {
            "name": "Bronchitis",
            "conditions": ["cough", "sore_throat", "chest_pain", "fatigue"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Inflammation of the bronchial tubes."
        },
        {
            "name": "Typhoid",
            "conditions": ["fever", "headache", "abdominal_pain", "fatigue"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "Bacterial infection affecting the intestines."
        },
        {
            "name": "Tuberculosis",
            "conditions": ["cough", "fever", "sweating", "shortness_breath"],
            "severity": "Severe",
            "emergency": False,
            "explanation": "Bacterial lung infection."
        },
        {
            "name": "Chickenpox",
            "conditions": ["fever", "body_pain", "headache", "fatigue"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Viral infection with characteristic rash."
        },
        {
            "name": "Urinary Tract Infection",
            "conditions": ["abdominal_pain", "nausea", "fever", "fatigue"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Bacterial infection of the urinary system."
        },
        {
            "name": "Appendicitis",
            "conditions": ["abdominal_pain", "nausea", "vomiting", "fever"],
            "severity": "Severe",
            "emergency": True,
            "explanation": "Inflammation of the appendix requiring surgery."
        },
        {
            "name": "Anxiety Attack",
            "conditions": ["shortness_breath", "chest_pain", "sweating", "headache"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Panic or anxiety episode."
        },
        {
            "name": "Diabetes Complication",
            "conditions": ["fatigue", "nausea", "sweating", "headache"],
            "severity": "Moderate",
            "emergency": False,
            "explanation": "Possible hypo/hyperglycemia or related issue."
        }

    ]

    # -----------------------------------------
    # 3. MATCH RULES
    # -----------------------------------------
    matched = []

    for rule in rules:
        if all(symptoms[c] for c in rule["conditions"]):
            matched.append(rule)

    # -----------------------------------------
    # 4. OUTPUT RESULTS
    # -----------------------------------------
    print("\n============================================")

    if not matched:
        print("No clear rule-based diagnosis. Symptoms don’t match known patterns.")
        print("Consider seeking medical consultation.")
        return

    print("Possible Diagnoses:\n")

    for m in matched:
        print(f"🔹 {m['name']}")
        print(f"   • Severity: {m['severity']}")
        print(f"   • Emergency: {'YES' if m['emergency'] else 'No'}")
        print(f"   • Reason: {m['explanation']}\n")

    if any(m["emergency"] for m in matched):
        print("⚠️ WARNING: Some detected conditions require immediate medical attention.\n")

    print("============================================\n")

medical_diagnosis()