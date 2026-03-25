# 🏥 Insurance Cost Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insuranceprediction-naved.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

👤 **Naved Shaikh** — [GitHub](https://github.com/navedrys) · [LinkedIn](https://linkedin.com/in/naved-shaikh-784776280) · navedrys@gmail.com · +91 7414991107

---

A simple web application that predicts annual medical charges based on personal details like age, BMI, number of children, and smoking status. Built with **Streamlit** and a **Linear Regression** model trained on real‑world insurance data.

👉 **Try it live:** [insuranceprediction-naved.streamlit.app](https://insuranceprediction-naved.streamlit.app/)

---

## 📌 Project Overview

This project demonstrates how machine learning can be used to estimate insurance costs.  
The app takes four inputs from the user:

- **Age** – the person’s age (18–100)  
- **BMI** – Body Mass Index (10–50)  
- **Children** – number of dependents covered  
- **Smoker** – whether the person smokes (Yes/No)

Based on these, it predicts the **annual medical charges** using a trained Linear Regression model.

---

## 🧠 How It Works (Interactive Flow Diagram)

```mermaid
graph TD
    A[User inputs: Age, BMI, Children, Smoker] --> B[Streamlit Web App]
    B --> C["Linear Regression Model (model.pkl)"]
    C --> D[Predicted Annual Insurance Cost]
    D --> E[Displayed to User]

    style A fill:#ff9999,stroke:#333,stroke-width:2px,color:#000
    style B fill:#99ff99,stroke:#333,stroke-width:2px,color:#000
    style C fill:#ffcc99,stroke:#333,stroke-width:2px,color:#000
    style D fill:#99ccff,stroke:#333,stroke-width:2px,color:#000
    style E fill:#cccc99,stroke:#333,stroke-width:2px,color:#000
