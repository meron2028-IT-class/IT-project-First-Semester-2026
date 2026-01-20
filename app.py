from flask import Flask, render_template, request
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Your data structures will go here
# diseases = {}
# recommendations = {}

# Your functions will go here
# def calculate_disease_probability(selected_symptoms):
#     pass

@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize variables
    Result = {}
    results = {}
    Percentages = set()
    Top_Three = []
    Diseases = {
        "Common Cold": ["runny_nose", "sneezing", "cough", "sore_throat", "mild_fever"],
"Flu": ["high_fever", "body_aches", "fatigue", "dry_cough", "headache"],
"COVID-19": ["fever", "dry_cough", "loss_of_taste", "fatigue", "shortness_of_breath"],
"Pneumonia": ["chest_pain", "cough", "fever", "shortness_of_breath", "fatigue"],
"Asthma": ["wheezing", "shortness_of_breath", "chest_tightness", "cough", "fatigue"],
"Bronchitis": ["cough", "mucus", "fatigue", "chest_discomfort", "shortness_of_breath"],
"Tuberculosis": ["persistent_cough", "weight_loss", "night_sweats", "fever", "chest_pain"],
"Sinusitis": ["facial_pain", "nasal_congestion", "headache", "runny_nose", "fever"],
"Allergic Rhinitis": ["sneezing", "itchy_nose", "runny_nose", "watery_eyes", "nasal_congestion"],
"Laryngitis": ["hoarseness", "sore_throat", "dry_cough", "voice_loss", "throat_irritation"],
"Gastritis": ["stomach_pain", "nausea", "vomiting", "bloating", "loss_of_appetite"],
"GERD": ["heartburn", "chest_pain", "acid_reflux", "difficulty_swallowing", "dry_cough"],
"Peptic Ulcer": ["burning_pain", "nausea", "bloating", "heartburn", "vomiting"],
"Diarrhea": ["loose_stools", "abdominal_cramps", "dehydration", "nausea", "fever"],
"Constipation": ["hard_stool", "abdominal_pain", "bloating", "straining", "infrequent_bowel_movements"],
"Irritable Bowel Syndrome": ["abdominal_pain", "bloating", "diarrhea", "constipation", "gas"],
"Hepatitis": ["fatigue", "jaundice", "dark_urine", "abdominal_pain", "nausea"],
"Gallstones": ["upper_abdominal_pain", "nausea", "vomiting", "fever", "back_pain"],
"Appendicitis": ["lower_right_abdominal_pain", "nausea", "vomiting", "fever", "loss_of_appetite"],
"Food Poisoning": ["vomiting", "diarrhea", "stomach_cramps", "fever", "nausea"],
"Hypertension": ["headache", "dizziness", "chest_pain", "blurred_vision", "fatigue"],
"Heart Attack": ["chest_pain", "shortness_of_breath", "nausea", "sweating", "arm_pain"],
"Stroke": ["face_drooping", "speech_difficulty", "arm_weakness", "confusion", "vision_problems"],
"Arrhythmia": ["irregular_heartbeat", "palpitations", "dizziness", "fatigue", "shortness_of_breath"],
"Heart Failure": ["shortness_of_breath", "swelling", "fatigue", "rapid_heartbeat", "persistent_cough"],
"Diabetes Type 1": ["frequent_urination", "excessive_thirst", "fatigue", "weight_loss", "blurred_vision"],
"Diabetes Type 2": ["fatigue", "slow_healing_wounds", "frequent_urination", "blurred_vision", "increased_hunger"],
"Hypothyroidism": ["weight_gain", "fatigue", "cold_intolerance", "dry_skin", "depression"],
"Hyperthyroidism": ["weight_loss", "rapid_heartbeat", "sweating", "anxiety", "tremors"],
"Obesity": ["weight_gain", "fatigue", "joint_pain", "shortness_of_breath", "low_energy"],
"Malaria": ["fever", "chills", "sweating", "headache", "nausea"],
"Dengue": ["high_fever", "joint_pain", "rash", "headache", "muscle_pain"],
"Typhoid": ["fever", "weakness", "abdominal_pain", "diarrhea", "loss_of_appetite"],
"Cholera": ["severe_diarrhea", "dehydration", "vomiting", "muscle_cramps", "weakness"],
"Measles": ["rash", "fever", "runny_nose", "red_eyes", "cough"],
"Mumps": ["swollen_glands", "fever", "headache", "fatigue", "jaw_pain"],
"Chickenpox": ["itchy_rash", "fever", "fatigue", "headache", "loss_of_appetite"],
"HIV/AIDS": ["fatigue", "weight_loss", "fever", "night_sweats", "recurrent_infections"],
"Ringworm": ["itching", "red_rash", "scaly_skin", "hair_loss", "burning_sensation"],
"Scabies": ["itching", "rash", "skin_sores", "red_bumps", "blisters"],
"Migraine": ["severe_headache", "nausea", "light_sensitivity", "vomiting", "blurred_vision"],
"Epilepsy": ["seizures", "confusion", "loss_of_consciousness", "muscle_spasms", "staring_spells"],
"Parkinsons Disease": ["tremors", "slow_movement", "muscle_stiffness", "balance_problems", "speech_changes"],
"Alzheimers Disease": ["memory_loss", "confusion", "behavior_changes", "difficulty_speaking", "disorientation"],
"Multiple Sclerosis": ["fatigue", "numbness", "vision_loss", "muscle_weakness", "coordination_problems"],
"Arthritis": ["joint_pain", "stiffness", "swelling", "reduced_motion", "redness"],
"Osteoporosis": ["bone_weakness", "fractures", "back_pain", "height_loss", "stooped_posture"],
"Gout": ["joint_pain", "swelling", "redness", "warmth", "limited_movement"],
"Sciatica": ["leg_pain", "lower_back_pain", "numbness", "tingling", "muscle_weakness"],
"Muscle Strain": ["pain", "swelling", "muscle_spasm", "limited_movement", "bruising"],
"Acne": ["pimples", "oily_skin", "blackheads", "whiteheads", "skin_inflammation"],
"Eczema": ["itching", "dry_skin", "red_rash", "cracked_skin", "swelling"],
"Psoriasis": ["thick_skin_patches", "itching", "redness", "dry_skin", "scaling"],
"Rosacea": ["facial_redness", "visible_blood_vessels", "burning_sensation", "bumps", "eye_irritation"],
"Hives": ["itchy_welts", "redness", "swelling", "burning", "skin_irritation"],
"Depression": ["sadness", "loss_of_interest", "fatigue", "sleep_problems", "hopelessness"],
"Anxiety Disorder": ["nervousness", "rapid_heartbeat", "sweating", "restlessness", "fear"],
"Bipolar Disorder": ["mood_swings", "energy_changes", "impulsiveness", "sleep_changes", "irritability"],
"Schizophrenia": ["hallucinations", "delusions", "confusion", "withdrawal", "speech_problems"],
"PTSD": ["flashbacks", "nightmares", "anxiety", "emotional_numbness", "hypervigilance"]

    }
    recommendations = {
"Common Cold": "Drink plenty of fluids, rest well, and use warm saltwater gargles for throat relief.",
"Flu": "Rest at home, stay hydrated, and consult a doctor if symptoms become severe.",
"COVID-19": "Isolate yourself, get tested, monitor oxygen levels, and seek medical care if breathing difficulty occurs.",
"Pneumonia": "Seek medical attention immediately and complete prescribed antibiotic or antiviral treatment.",
"Asthma": "Use prescribed inhalers regularly and avoid known triggers such as dust and smoke.",
"Bronchitis": "Rest, drink warm fluids, and consult a healthcare provider if coughing persists.",
"Tuberculosis": "Follow the full course of prescribed TB medication under medical supervision.",
"Sinusitis": "Use steam inhalation, nasal sprays, and consult a doctor if symptoms persist.",
"Allergic Rhinitis": "Avoid allergens and use antihistamines or nasal sprays as recommended.",
"Laryngitis": "Rest your voice, stay hydrated, and avoid smoking or cold drinks.",
"Gastritis": "Avoid spicy foods, alcohol, and take prescribed antacids or medication.",
"GERD": "Eat smaller meals, avoid lying down after eating, and use acid-reducing medication.",
"Peptic Ulcer": "Follow doctor-prescribed treatment and avoid NSAIDs and alcohol.",
"Diarrhea": "Drink oral rehydration solutions and eat light foods until recovery.",
"Constipation": "Increase fiber intake, drink more water, and stay physically active.",
"Irritable Bowel Syndrome": "Manage stress, adjust diet, and follow medical advice for symptom control.",
"Hepatitis": "Avoid alcohol completely and follow medical treatment plans strictly.",
"Gallstones": "Seek medical evaluation and consider surgical treatment if pain is severe.",
"Appendicitis": "Seek emergency medical care immediately.",
"Food Poisoning": "Stay hydrated and seek medical help if symptoms worsen.",
"Hypertension": "Reduce salt intake, exercise regularly, manage stress, and take prescribed medications.",
"Heart Attack": "Call emergency services immediately and seek urgent medical treatment.",
"Stroke": "Seek emergency care immediately and begin rehabilitation therapy afterward.",
"Arrhythmia": "Follow doctor-prescribed medication and avoid caffeine and alcohol.",
"Heart Failure": "Limit salt intake, take medications regularly, and monitor fluid levels.",
"Diabetes Type 1": "Use insulin as prescribed and monitor blood sugar levels daily.",
"Diabetes Type 2": "Maintain a healthy diet, exercise regularly, and take prescribed medications.",
"Hypothyroidism": "Take thyroid hormone replacement therapy as prescribed.",
"Hyperthyroidism": "Follow medical treatment plans and attend regular doctor checkups.",
"Obesity": "Adopt a healthy diet, exercise regularly, and seek professional guidance if needed.",
"Malaria": "Seek immediate medical treatment and complete the full medication course.",
"Dengue": "Rest, drink fluids, avoid painkillers like aspirin, and monitor symptoms closely.",
"Typhoid": "Take prescribed antibiotics and maintain proper hygiene.",
"Cholera": "Seek urgent rehydration therapy and medical treatment.",
"Measles": "Isolate the patient and provide supportive care such as hydration and fever control.",
"Mumps": "Rest, isolate the patient, and manage pain with medical advice.",
"Chickenpox": "Avoid scratching, use soothing lotions, and isolate until recovery.",
"HIV/AIDS": "Take antiretroviral therapy regularly and attend routine medical follow-ups.",
"Ringworm": "Use antifungal medication and keep the affected area clean and dry.",
"Scabies": "Apply prescribed medicated creams and wash clothing and bedding thoroughly.",
"Migraine": "Avoid triggers, rest in a dark room, and take prescribed pain medication.",
"Epilepsy": "Take anti-seizure medication regularly and avoid known triggers.",
"Parkinsons Disease": "Follow medication schedules and attend physical therapy sessions.",
"Alzheimers Disease": "Provide cognitive support, maintain routine, and seek specialized medical care.",
"Multiple Sclerosis": "Follow disease-modifying treatments and engage in physical therapy.",
"Arthritis": "Use pain-relief medication, exercise gently, and apply hot or cold therapy.",
"Osteoporosis": "Increase calcium and vitamin D intake and perform weight-bearing exercises.",
"Gout": "Avoid purine-rich foods and take prescribed medication.",
"Sciatica": "Use physical therapy, proper posture, and pain management techniques.",
"Muscle Strain": "Rest the affected muscle and apply ice and compression.",
"Acne": "Wash skin gently and use dermatologist-recommended treatments.",
"Eczema": "Moisturize regularly and avoid skin irritants.",
"Psoriasis": "Use medicated creams and follow dermatologist advice.",
"Rosacea": "Avoid triggers such as spicy foods and use prescribed topical treatments.",
"Hives": "Use antihistamines and avoid known allergens.",
"Depression": "Seek professional counseling and follow prescribed treatment plans.",
"Anxiety Disorder": "Practice relaxation techniques and consider therapy or medication.",
"Bipolar Disorder": "Follow mood-stabilizing treatment and maintain regular routines.",
"Schizophrenia": "Take prescribed medication and attend therapy sessions regularly.",
"PTSD": "Seek trauma-focused therapy and mental health support."
}
    current_date = datetime.now().strftime("%B %d, %Y at %I:%M %p")
    
    if request.method == "POST":
        # Get selected symptoms from form
        selected_symptoms = request.form.getlist("symptoms")

        for disease in Diseases:
            Symptom_Count = 0
            for symptom in selected_symptoms:
                if symptom in Diseases[disease]:
                    Symptom_Count = Symptom_Count + 1
            results[disease] = (((Symptom_Count)/(5)) * (100))
            Percentages.append(results[disease])
        if len(Percentages) > 3:
            for i in range(3):
                Max = max(Percentages)
                Top_Three.append(Max))
                Percentages.remove(Max)
        else:
            for i in Percentages:
                Top_Three.append(i)
        for j in Top_Three:
            for i in results:
                if results[i] == j:
                    Results[i] = [i, j, recommendations[i]]
    # Render template with results
    return render_template("index.html", 
                         results=results, 
                         recommendation=recommendation,
                         date=current_date)

# Run the app
if __name__ == "__main__":

    app.run(debug=True, port=5000)
