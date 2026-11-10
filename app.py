import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Set page title and layout
st.set_page_config(page_title="Student Group Classifier", layout="centered")

st.title("🎓 Student Profile & Group Classifier")
st.write("""
Enter student details below to classify them into their respective performance and structural profiles using our trained machine learning pipeline.
""")

# Load the saved pipeline
@st.cache_resource
def load_model():
    return joblib.load('student_classification_pipeline.joblib')

try:
    pipeline = load_model()
    model_loaded = True
except Exception as e:
    st.error(f"Failed to load the pipeline model: {e}. Make sure 'student_classification_pipeline.joblib' is in the same directory.")
    model_loaded = False

if model_loaded:
    st.subheader("Enter Student Details:")
    
    # Input widgets representing our numeric columns schema
    student_cgpa = st.number_input("Student CGPA", min_value=0.0, max_value=4.0, value=3.0, step=0.01)
    student_semester = st.slider("Current Semester", min_value=1, max_value=8, value=4, step=1)
    marks = st.slider("Marks (Course Performance)", min_value=0, max_value=100, value=75, step=1)
    fee_amount = st.number_input("Tuition / Fee Amount (PKR)", min_value=0.0, value=50000.0, step=1000.0)

    if st.button("Classify Student Profile"):
        # Construct a DataFrame matching the training feature schema exactly
        input_data = pd.DataFrame([{
            'student_cgpa': student_cgpa,
            'student_semester': student_semester,
            'marks': marks,
            'fee_amount': fee_amount
        }])
        
        # Predict
        try:
            prediction = pipeline.predict(input_data)[0]
            
            # Interpret cluster groups based on characteristics
            profile_descriptions = {
                0: "🏆 High-Performing Senior: Outstanding CGPA, moderate-to-high marks, advanced semester, paid fee profile.",
                1: "🚀 Active Mid-Career Achiever: Strong marks and CGPA, advanced semesters, premium enrollment segment.",
                2: "📝 Budding Junior: Good core performance, early semester student, balanced financial segment.",
                3: "🔍 High-Potential Advanced Student: High semesters, standard tuition tier, solid performance background."
            }
            
            st.success(f"### Assigned Profile Group: Cluster {prediction}")
            st.info(profile_descriptions.get(prediction, "Custom profile characterized by balanced performance metrics."))
            
        except Exception as err:
            st.error(f"An error occurred during prediction: {err}")
