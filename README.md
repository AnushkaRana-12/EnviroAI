🌍 EnviroAI — AI-Based Environmental Risk Intelligence & AQI Prediction System












📌 Project Overview

EnviroAI is an AI-powered environmental intelligence and air pollution forecasting system that predicts PM2.5 levels and Air Quality Index (AQI) using environmental, weather, and satellite (NDVI) data.

The system combines Machine Learning, Explainable AI (SHAP), and Interactive Dashboard Visualization to provide environmental risk insights and decision support.

The dashboard provides:

📊 PM2.5 and AQI prediction
⏳ 6-hour AQI forecast
🌦 Environmental factor monitoring
🧠 AI-generated insights
⚠️ Health risk recommendations
📍 City location mapping
🏆 City AQI ranking
🔍 Explainable AI using SHAP
🎯 Problem Statement

Air pollution prediction involves complex and non-linear relationships between environmental factors such as temperature, humidity, wind speed, pollutant levels, and vegetation indices.

Traditional statistical models fail to capture these relationships effectively.

This project develops an AI-based predictive and decision support system that improves both prediction accuracy and interpretability using Explainable AI techniques.

🧠 Objectives
Predict PM2.5 levels using Machine Learning
Calculate Air Quality Index (AQI)
Forecast future AQI (6-hour prediction)
Analyze environmental risk factors
Provide AI-generated insights and health recommendations
Use Explainable AI (SHAP) to interpret model predictions
Develop an interactive dashboard for visualization
🛠️ Tech Stack
Category	Tools
Language	Python
ML Model	Random Forest Regression
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Plotly
Dashboard	Streamlit
Explainable AI	SHAP
API	Open-Meteo API
Environment	Jupyter Notebook / Google Colab
⚙️ System Workflow
Data Collection & Integration
Data Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Model Training (Random Forest Regression)
Model Evaluation (MAE, RMSE, R²)
Explainable AI using SHAP
AQI Prediction
AQI Forecasting
Dashboard Visualization
AI Insights & Health Recommendations
📊 Dashboard Features
Feature	Description
Live AQI Prediction	Predicts AQI using ML model
6-Hour Forecast	Predicts future AQI
AQI Meter	Shows AQI severity
Pollution Trend	Historical PM2.5 & PM10
AI Insights	Environmental risk explanation
Health Recommendation	Safety advice
Environmental Factors	Temperature, Humidity, Wind, NDVI
Explainable AI	SHAP Feature Importance
City Map	Location visualization
City Ranking	AQI comparison

🌍 EnviroAI — AI-Based Environmental Risk Intelligence & AQI Prediction System












📌 Project Overview

EnviroAI is an AI-powered environmental intelligence and air pollution forecasting system that predicts PM2.5 levels and Air Quality Index (AQI) using environmental, weather, and satellite (NDVI) data.

The system combines Machine Learning, Explainable AI (SHAP), and Interactive Dashboard Visualization to provide environmental risk insights and decision support.

The dashboard provides:

📊 PM2.5 and AQI prediction
⏳ 6-hour AQI forecast
🌦 Environmental factor monitoring
🧠 AI-generated insights
⚠️ Health risk recommendations
📍 City location mapping
🏆 City AQI ranking
🔍 Explainable AI using SHAP
🎯 Problem Statement

Air pollution prediction involves complex and non-linear relationships between environmental factors such as temperature, humidity, wind speed, pollutant levels, and vegetation indices.

Traditional statistical models fail to capture these relationships effectively.

This project develops an AI-based predictive and decision support system that improves both prediction accuracy and interpretability using Explainable AI techniques.

🧠 Objectives
Predict PM2.5 levels using Machine Learning
Calculate Air Quality Index (AQI)
Forecast future AQI (6-hour prediction)
Analyze environmental risk factors
Provide AI-generated insights and health recommendations
Use Explainable AI (SHAP) to interpret model predictions
Develop an interactive dashboard for visualization
🛠️ Tech Stack
Category	Tools
Language	Python
ML Model	Random Forest Regression
Data Processing	Pandas, NumPy
Visualization	Matplotlib, Plotly
Dashboard	Streamlit
Explainable AI	SHAP
API	Open-Meteo API
Environment	Jupyter Notebook / Google Colab
⚙️ System Workflow
Data Collection & Integration
Data Preprocessing
Exploratory Data Analysis (EDA)
Feature Engineering
Model Training (Random Forest Regression)
Model Evaluation (MAE, RMSE, R²)
Explainable AI using SHAP
AQI Prediction
AQI Forecasting
Dashboard Visualization
AI Insights & Health Recommendations
📊 Dashboard Features
Feature	Description
Live AQI Prediction	Predicts AQI using ML model
6-Hour Forecast	Predicts future AQI
AQI Meter	Shows AQI severity
Pollution Trend	Historical PM2.5 & PM10
AI Insights	Environmental risk explanation
Health Recommendation	Safety advice
Environmental Factors	Temperature, Humidity, Wind, NDVI
Explainable AI	SHAP Feature Importance
City Map	Location visualization
City Ranking	AQI comparison

📂 Project Structure
EnviroAI/
│
├── data/                # Dataset
├── notebooks/           # EDA & experiments
├── model/               # Model training code
├── dashboard/           # Streamlit dashboard
│   ├── app.py
│   ├── style.css
│
├── images/              # Graphs & outputs
├── model.pkl            # Trained model
├── requirements.txt
└── README.md

▶️ Installation & Setup
# Clone repository
git clone https://github.com/AnushkaRana-12/EnviroAI.git

# Open project folder
cd EnviroAI

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run app.py

📈 Model Performance

The Random Forest model was evaluated using:

Metric	Description
MAE	Mean Absolute Error
RMSE	Root Mean Squared Error
R² Score	Model Accuracy

The model achieved high prediction accuracy and captured non-linear environmental relationships effectively.

🔍 Explainable AI (SHAP)

SHAP (SHapley Additive exPlanations) is used to interpret the model and understand how each environmental factor affects AQI prediction.

Key influencing factors:

Temperature
Humidity
Wind Speed
Vegetation Index (NDVI)
🚀 Future Scope
Hyperparameter tuning
Deep learning models (LSTM, ANN)
Real-time IoT sensor integration
Mobile application
Cloud deployment (AWS / Azure)
Pollution source detection
Automated alert system
👩‍💻 Author

Anushka Rana
B.Tech CSE (AI & ML)
KR Mangalam University

📄 License

This project is developed for academic and research purposes only.
