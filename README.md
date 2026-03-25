# 🏥 Insurance Cost Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insuranceprediction-naved.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#ffb,stroke:#333,stroke-width:2px
    style E fill:#fbb,stroke:#333,stroke-width:2px
