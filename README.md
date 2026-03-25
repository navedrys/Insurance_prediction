# 🏥 Insurance Cost Predictor

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://insuranceprediction-naved.streamlit.app/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple web application that predicts annual medical charges based on personal details like age, BMI, number of children, and smoking status. Built with **Streamlit** and a **Linear Regression** model trained on real‑world insurance data.

👉 **Try it live:** [insuranceprediction-naved.streamlit.app](https://insuranceprediction-naved.streamlit.app/)  
👉 **Click the badge above** or the link to launch the app!

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

## 🧠 How It Works (A Simple Flow)

```plaintext
┌─────────────────────────┐
│   User inputs data      │
│  (age, bmi, children,   │
│         smoker)         │
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│  App (Streamlit)        │
│  collects inputs and    │
│  sends them to the      │
│  trained model          │
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│  Linear Regression      │
│  Model (model.pkl)      │
│  – learned from         │
│    historical data      │
└───────────┬─────────────┘
            ▼
┌─────────────────────────┐
│  Predicted annual       │
│  insurance cost         │
│  displayed to user      │
└─────────────────────────┘
