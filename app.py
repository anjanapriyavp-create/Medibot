import streamlit as st
from symptoms import symptoms_data

st.set_page_config(page_title="Medibot 🏥", page_icon="🏥", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
    
    * { font-family: 'Poppins', sans-serif; }
    
    .main { background-color: #0a0e1a; }
    
    .hero {
        background: linear-gradient(135deg, #00d4aa20, #7b2ff720);
        border: 1px solid #00d4aa40;
        border-radius: 20px;
        padding: 40px 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    .hero-title {
        font-size: 3.5em;
        font-weight: 800;
        background: linear-gradient(90deg, #00d4aa, #7b2ff7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        line-height: 1.2;
    }
    .hero-sub {
        font-size: 1.1em;
        color: #aaa;
        margin-top: 10px;
    }
    .badge {
        display: inline-block;
        background: #00d4aa20;
        color: #00d4aa;
        border: 1px solid #00d4aa50;
        border-radius: 20px;
        padding: 4px 14px;
        font-size: 0.85em;
        margin-top: 10px;
    }
    .symptom-card {
        background: linear-gradient(135deg, #1a1f35, #0f1424);
        border-radius: 16px;
        padding: 25px;
        margin: 15px 0;
        border-left: 4px solid #00d4aa;
        box-shadow: 0 4px 20px rgba(0,212,170,0.1);
    }
    .section-title {
        color: #00d4aa;
        font-size: 1.1em;
        font-weight: 600;
        margin-bottom: 8px;
    }
    .bullet-item {
        background: #ffffff08;
        border-radius: 8px;
        padding: 6px 12px;
        margin: 4px 0;
        color: #ddd;
        font-size: 0.95em;
    }
    .footer {
        text-align: center;
        color: #333;
        font-size: 0.8em;
        margin-top: 60px;
        padding: 20px;
        border-top: 1px solid #1a1f35;
    }
    .stTextInput > div > div > input {
        background-color: #1a1f35 !important;
        border: 1px solid #00d4aa50 !important;
        border-radius: 12px !important;
        color: white !important;
        font-size: 1.1em !important;
        padding: 15px !important;
    }
    .stButton > button {
        background: linear-gradient(90deg, #00d4aa, #7b2ff7) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 12px 30px !important;
        font-size: 1.1em !important;
        font-weight: 600 !important;
        width: 100% !important;
        transition: all 0.3s !important;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <p class="hero-title">🏥 Medibot</p>
        <p class="hero-sub">Your intelligent health companion — understand your symptoms instantly</p>
        <span class="badge">✨ AI-Powered Health Assistant</span>
    </div>
""", unsafe_allow_html=True)

st.warning("⚠️ This app provides general information only. Always consult a qualified doctor for medical advice.")

st.markdown("---")

user_input = st.text_input("",
    placeholder="🔍 Type symptoms here... e.g. fever, headache, cough")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    check = st.button("🔍 Analyse Symptoms", use_container_width=True)

if check:
    if not user_input.strip():
        st.error("⚠️ Please enter at least one symptom!")
    else:
        raw_inputs = user_input.lower().replace(",", " ").split()
        found_any = False
        checked = set()

        two_word_symptoms = []
        for i in range(len(raw_inputs) - 1):
            combo = raw_inputs[i] + " " + raw_inputs[i+1]
            two_word_symptoms.append(combo)

        all_to_check = two_word_symptoms + raw_inputs

        for symptom in all_to_check:
            if symptom in symptoms_data and symptom not in checked:
                checked.add(symptom)
                found_any = True
                info = symptoms_data[symptom]

                st.markdown(f"""
                    <div class="symptom-card">
                        <div class="section-title">📌 {symptom.upper()}</div>
                        <p style="color:#ccc;">{info["description"]}</p>
                    </div>
                """, unsafe_allow_html=True)

                col1, col2 = st.columns(2)

                with col1:
                    st.markdown('<p class="section-title">🔍 Possible Causes</p>', unsafe_allow_html=True)
                    for cause in info["possible_causes"]:
                        st.markdown(f'<div class="bullet-item">• {cause}</div>', unsafe_allow_html=True)

                with col2:
                    st.markdown('<p class="section-title">🌿 Home Remedies</p>', unsafe_allow_html=True)
                    for remedy in info["home_remedies"]:
                        st.markdown(f'<div class="bullet-item">• {remedy}</div>', unsafe_allow_html=True)

                st.error(f"🚨 See a doctor if: {info['see_doctor']}")
                st.markdown("---")

        if not found_any:
            st.error("❌ No matching symptoms found!")
            st.info("💡 Try: fever, headache, cough, cold, stomach pain, back pain, chest pain, fatigue, dizziness, vomiting, diarrhea, sore throat, skin rash, eye irritation, joint pain")

st.markdown('<p class="footer">🏥 Medibot v1.0 — For informational purposes only</p>', unsafe_allow_html=True)