# This is our "knowledge base" — like a dictionary of symptoms
# In Python, a dictionary stores data as key:value pairs
# Key = symptom name, Value = information about it

symptoms_data = {
    "fever": {
        "description": "Fever is a temporary rise in body temperature.",
        "possible_causes": ["Infection", "Flu", "COVID-19", "Malaria"],
        "home_remedies": ["Rest well", "Drink plenty of water", "Take paracetamol"],
        "see_doctor": "If fever is above 103°F or lasts more than 3 days"
    },
    "headache": {
        "description": "Pain or discomfort in the head or neck region.",
        "possible_causes": ["Stress", "Dehydration", "Migraine", "Lack of sleep"],
        "home_remedies": ["Drink water", "Rest in dark room", "Apply cold compress"],
        "see_doctor": "If headache is sudden and severe or comes with vomiting"
    },
    "cough": {
        "description": "A reflex action to clear the airways of irritants.",
        "possible_causes": ["Cold", "Allergies", "Asthma", "Throat infection"],
        "home_remedies": ["Honey with warm water", "Steam inhalation", "Ginger tea"],
        "see_doctor": "If cough lasts more than 2 weeks or has blood"
    },
    "stomach pain": {
        "description": "Pain or discomfort felt in the abdominal area.",
        "possible_causes": ["Indigestion", "Gas", "Food poisoning", "Appendicitis"],
        "home_remedies": ["Drink warm water", "Avoid spicy food", "Rest"],
        "see_doctor": "If pain is severe or comes with vomiting and fever"
    },
    "cold": {
        "description": "A viral infection affecting nose and throat.",
        "possible_causes": ["Rhinovirus", "Weather change", "Weak immunity"],
        "home_remedies": ["Steam inhalation", "Warm soups", "Rest", "Vitamin C"],
        "see_doctor": "If symptoms last more than 10 days"
    },
    "vomiting": {
        "description": "Forceful expulsion of stomach contents through the mouth.",
        "possible_causes": ["Food poisoning", "Gastritis", "Motion sickness", "Pregnancy"],
        "home_remedies": ["Sip cold water slowly", "Eat bland food like rice", "Rest", "Ginger tea"],
        "see_doctor": "If vomiting lasts more than 2 days or has blood"
    },
    "diarrhea": {
        "description": "Loose or watery stools occurring frequently.",
        "possible_causes": ["Food poisoning", "Viral infection", "IBS", "Contaminated water"],
        "home_remedies": ["Drink ORS", "Eat bananas and rice", "Avoid dairy", "Stay hydrated"],
        "see_doctor": "If diarrhea lasts more than 3 days or has blood"
    },
    "back pain": {
        "description": "Pain felt in the upper, middle or lower back region.",
        "possible_causes": ["Poor posture", "Muscle strain", "Kidney issues", "Sitting too long"],
        "home_remedies": ["Hot compress", "Gentle stretching", "Rest", "Maintain good posture"],
        "see_doctor": "If pain radiates to legs or comes with numbness"
    },
    "sore throat": {
        "description": "Pain, scratchiness or irritation of the throat.",
        "possible_causes": ["Viral infection", "Strep throat", "Allergies", "Dry air"],
        "home_remedies": ["Gargle warm salt water", "Honey with ginger", "Stay hydrated", "Steam"],
        "see_doctor": "If sore throat lasts more than a week or causes difficulty swallowing"
    },
    "fatigue": {
        "description": "Extreme tiredness that doesn't go away with rest.",
        "possible_causes": ["Anaemia", "Poor sleep", "Thyroid issues", "Stress", "Diabetes"],
        "home_remedies": ["Sleep 7-8 hours", "Eat iron rich foods", "Exercise lightly", "Stay hydrated"],
        "see_doctor": "If fatigue is persistent for weeks with no clear reason"
    },
    "dizziness": {
        "description": "Feeling of being unsteady, lightheaded or off balance.",
        "possible_causes": ["Low blood pressure", "Dehydration", "Anaemia", "Inner ear problem"],
        "home_remedies": ["Sit or lie down immediately", "Drink water", "Avoid sudden movements"],
        "see_doctor": "If dizziness comes with chest pain, fainting or vision problems"
    },
    "chest pain": {
        "description": "Pain or pressure felt in the chest area.",
        "possible_causes": ["Heart issues", "Acid reflux", "Anxiety", "Muscle strain"],
        "home_remedies": ["Rest", "Drink water", "Avoid heavy meals"],
        "see_doctor": "If chest pain is severe or comes with shortness of breath"
    },
    "skin rash": {
        "description": "Change in skin color or texture causing irritation.",
        "possible_causes": ["Allergy", "Eczema", "Heat rash", "Fungal infection", "Insect bite"],
        "home_remedies": ["Apply aloe vera", "Avoid scratching", "Use cold compress", "Keep area clean"],
        "see_doctor": "If rash spreads rapidly or comes with fever and breathing difficulty"
    },
    "eye irritation": {
        "description": "Redness, itching or discomfort in the eyes.",
        "possible_causes": ["Conjunctivitis", "Allergy", "Dust", "Screen time", "Dry eyes"],
        "home_remedies": ["Wash eyes with clean water", "Reduce screen time", "Use cold compress"],
        "see_doctor": "If vision is affected or discharge is yellow/green"
    },
    "joint pain": {
        "description": "Pain, aching or soreness in any of the body joints.",
        "possible_causes": ["Arthritis", "Injury", "Dengue fever", "Vitamin D deficiency"],
        "home_remedies": ["Warm compress", "Gentle exercise", "Turmeric milk", "Rest the joint"],
        "see_doctor": "If joint is swollen, red or pain is severe and persistent"
    },
}