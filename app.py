import streamlit as st
import pandas as pd
import pickle

# Load the trained model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

model = load_model()

# Page configuration
st.set_page_config(
    page_title="Insurance Cost Predictor",
    page_icon="💰",
    layout="centered"
)

# Background image (replace URL with your own image or upload to GitHub and use raw link)
background_image_url = "https://images.unsplash.com/photo-1579684385127-1ef15d5089a3?ixlib=rb-4.0.3&auto=format&fit=crop&w=1350&q=80"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main-header {{
        font-size: 2.5rem;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}
    .sub-header {{
        font-size: 1.2rem;
        color: #f0f0f0;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }}
    .prediction-box {{
        background-color: rgba(255,255,255,0.9);
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        backdrop-filter: blur(2px);
    }}
    .contact {{
        background-color: rgba(0,0,0,0.6);
        text-align: center;
        margin-top: 40px;
        padding: 20px;
        border-radius: 10px;
        color: white;
    }}
    .contact a {{
        color: #ffd700;
        text-decoration: none;
    }}
    .stSlider > div {{
        background-color: rgba(255,255,255,0.8);
        border-radius: 5px;
        padding: 10px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="main-header">🏥 Insurance Cost Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Adjust the values below to see your estimated annual medical charges</div>', unsafe_allow_html=True)

# Input widgets
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", min_value=18, max_value=100, value=30, step=1,
                    help="Your age in years")
    bmi = st.slider("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1,
                    help="Body Mass Index (weight in kg / (height in m)^2)")

with col2:
    children = st.slider("Number of Children", min_value=0, max_value=10, value=0, step=1,
                         help="Number of dependents covered by the insurance")
    smoker = st.selectbox("Smoker", options=["No", "Yes"], index=0,
                          help="Do you smoke?")

# Convert smoker to binary (1 for Yes, 0 for No)
smoker_binary = 1 if smoker == "Yes" else 0

# Live prediction as user changes inputs
input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "smoker_yes": [smoker_binary]
})

prediction = model.predict(input_data)[0]

# Display live prediction
st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
st.metric(label="💰 Estimated Annual Medical Charges", value=f"${prediction:,.2f}")
st.markdown('</div>', unsafe_allow_html=True)

# Contact information
st.markdown('<div class="contact">', unsafe_allow_html=True)
st.markdown("### 📬 Contact Me")
st.markdown("""
- **GitHub**: [navedrys](https://github.com/navedrys)
- **LinkedIn**: [Naved Shaikh](https://linkedin.com/in/naved-shaikh-784776280)
- **Email**: navedrys@gmail.com
- **Phone**: +91 7414991107
""")
st.markdown('</div>', unsafe_allow_html=True)
