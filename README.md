# Task 9 – End-to-End Data Science Project

## Problem Statement:
Diabetes is a chronic disease where early detection can significantly improve outcomes. The goal is to build a complete data science pipeline — from raw data to a deployed web app — that predicts whether a patient is at risk of diabetes based on clinical inputs.

## Dataset:
- **Name:** Pima Indians Diabetes Dataset
- **Source:** Kaggle
- **Size:** 768 rows × 9 columns
- **Target:** Outcome — 1 (Diabetic), 0 (Non-Diabetic)
- **Features:** Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age

## Approach:
- Replaced biologically invalid zero values in Glucose, BloodPressure, SkinThickness, Insulin, and BMI with NaN, then filled with column medians
- Performed EDA: feature distributions, correlation heatmap, class balance check
- Trained a Random Forest Classifier (100 estimators, 80/20 train-test split)
- Saved the trained model as diabetes_model.pkl
- Built and deployed a Streamlit web app where users enter patient details via sliders and receive a prediction with confidence score

## Results:
- Model achieved ~76–80% accuracy on the test set
- Deployed as a Streamlit app with a clean UI — user inputs 8 clinical values and gets an instant High Risk / Low Risk prediction with confidence percentage
- https://synent-task9-datascienceproject-hem-ywx2cfzykaptmsrnwnbsem.streamlit.app/
