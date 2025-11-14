def medical_diagnosis():
    print("Simple Medical Diagnosis Expert System")
    print("Answer with yes or no. If answered with anything else, it will be taken as no.\n")

    symptoms = {}

    symptoms["fever"] = input("Do you have fever? ").lower() == "yes"
    symptoms["cough"] = input("Do you have cough? ").lower() == "yes"
    symptoms["sore_throat"] = input("Do you have sore throat? ").lower() == "yes"
    symptoms["chills"] = input("Do you have chills? ").lower() == "yes"
    symptoms["sweating"] = input("Do you have sweating? ").lower() == "yes"
    symptoms["headache"] = input("Do you have headache? ").lower() == "yes"
    symptoms["body_pain"] = input("Do you have body pain? ").lower() == "yes"
    symptoms["runny_nose"] = input("Do you have runny nose? ").lower() == "yes"
    symptoms["nausea"] = input("Do you have nausea? ").lower() == "yes"
    symptoms["vomiting"] = input("Do you have vomiting? ").lower() == "yes"
    symptoms["abdominal_pain"] = input("Do you have abdominal pain? ").lower() == "yes"

    diagnosis = []

    if symptoms["fever"] and symptoms["cough"] and symptoms["sore_throat"]:
        diagnosis.append("Flu")

    if symptoms["fever"] and symptoms["headache"] and symptoms["body_pain"]:
        diagnosis.append("Dengue")

    if symptoms["fever"] and symptoms["chills"] and symptoms["sweating"]:
        diagnosis.append("Malaria")

    if symptoms["runny_nose"] and symptoms["sore_throat"] and symptoms["cough"]:
        diagnosis.append("Common Cold")

    if symptoms["nausea"] and symptoms["vomiting"] and symptoms["abdominal_pain"]:
        diagnosis.append("Food Poisoning")

    if len(diagnosis) == 0:
        print("\nNo clear diagnosis. Please consult a doctor.")
    else:
        print("\nPossible Diagnosis:")
        for d in diagnosis:
            print("-", d)


medical_diagnosis()
