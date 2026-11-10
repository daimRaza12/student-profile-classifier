# 🎓 Student Profile & Group Classifier

An end-to-end Machine Learning project that aggregates mock student data records using SQLite, identifies distinct behavioral/academic profiles with K-Means clustering, trains an optimized classification model, and provides a production-ready interactive web application built with Streamlit.

---

## 📂 Project Directory Structure
```
├── app.py                             # Streamlit Web App Entrypoint
├── requirements.txt                   # App Dependencies
├── student_classification_pipeline.joblib # Trained ML Pipeline (Scaler + RF Model)
├── README.md                          # Project Documentation
└── [optional] students.xlsx / faculty.xlsx / admin_records.xlsx # Datasets
```

---

## 🛠️ Machine Learning Pipeline Highlights
1. **Data Engineering & Preprocessing:**
   - Consolidated relational datasets using SQLite in-memory tables and robust JOIN queries.
   - Cleaned missing entries, converted fields, and preprocessed numeric features (`student_cgpa`, `student_semester`, `marks`, `fee_amount`).
2. **Clustering & Target Definition:**
   - Tuned K-Means and DBSCAN using Silhouette analysis to discover 4 distinct student performance profiles.
   - Assigned these optimal cluster labels as prediction targets.
3. **Classification & Tuning:**
   - Trained Baseline Random Forest and Gradient Boosting Classifiers.
   - Fine-tuned the dominant Random Forest Classifier using `GridSearchCV` to achieve **~97.6% accuracy**.
4. **Serialization & Validation:**
   - Exported standard scaling and the tuned classifier together as a single unified `Pipeline` to eliminate training-serving skew.
   - Built custom data type and schema input validation helpers.

---

## 🚀 Getting Started locally

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/student-profile-classifier.git
cd student-profile-classifier
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit Application
```bash
streamlit run app.py
```

---

## 🌐 Deploy to Streamlit Community Cloud
1. Push this project folder directly onto **GitHub**.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io/) and authorize with your GitHub account.
3. Click **Deploy an App**, select this repository, target branch, and set your Main File Path as `app.py`.
4. Click **Deploy!** Your cloud application will be ready in minutes.
