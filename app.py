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

# Remove default Streamlit header and dividers (white/black lines)
st.markdown("""
    <style>
        header {visibility: hidden;}
        .stApp header {display: none;}
        hr {display: none;}
        .block-container {padding-top: 1rem;}
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🏥 Insurance Cost Predictor")
st.markdown("Adjust the values below and click **Predict** to see your estimated annual medical charges.")

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

# Convert smoker to binary
smoker_binary = 1 if smoker == "Yes" else 0

# Prediction button
if st.button("Predict", type="primary", use_container_width=True):
    # Create input DataFrame
    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "smoker_yes": [smoker_binary]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Estimated Annual Medical Charges: **${prediction:,.2f}**")

# Contact information
st.markdown("---")
st.markdown("### 📬 Contact Me")
st.markdown("""
- **GitHub**: [navedrys](https://github.com/navedrys)
- **LinkedIn**: [Naved Shaikh](https://linkedin.com/in/naved-shaikh-784776280)
- **Email**: navedrys@gmail.com
- **Phone**: +91 7414991107
""")
