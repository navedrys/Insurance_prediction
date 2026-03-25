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

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7f8c8d;
        text-align: center;
        margin-bottom: 2rem;
    }
    .prediction-box {
        background-color: #f0f2f6;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .contact {
        text-align: center;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e0e0e0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🏥 Insurance Cost Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Estimate your annual medical charges based on personal details</div>', unsafe_allow_html=True)

# Input fields
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=18, max_value=100, value=30, step=1,
                          help="Your age in years")
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1,
                          help="Body Mass Index (weight in kg / (height in m)^2)")

with col2:
    children = st.number_input("Number of Children", min_value=0, max_value=10, value=0, step=1,
                               help="Number of dependents covered by the insurance")
    smoker = st.selectbox("Smoker", options=["No", "Yes"], index=0,
                          help="Do you smoke?")

# Convert smoker to binary (1 for Yes, 0 for No)
smoker_binary = 1 if smoker == "Yes" else 0

# Prediction button
if st.button("Predict Charges", type="primary", use_container_width=True):
    # Create input DataFrame
    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "children": [children],
        "smoker_yes": [smoker_binary]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.markdown('<div class="prediction-box">', unsafe_allow_html=True)
    st.metric(label="Estimated Annual Medical Charges", value=f"${prediction:,.2f}")
    st.markdown('</div>', unsafe_allow_html=True)

# Additional info
st.info("This prediction is based on a linear regression model trained on a dataset of 1,338 insurance records. The model accounts for age, BMI, number of children, and smoking status.")

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
