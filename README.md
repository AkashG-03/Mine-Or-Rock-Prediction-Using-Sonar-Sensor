# Mine-Or-Rock-Prediction-Using-Sonar-Sensor
Machine Learning model to classify sonar signals as rocks or mines using Logistic Regression.



**Project Overview**

Dataset: SONAR dataset from UCI Machine Learning Repository.

Goal: Classify objects as Mine or Rock.

Algorithm Used: Logistic Regression.

Environment: Python 3.11.9, Virtual Environment (sonar_env).

**Tech Stack**


Python

NumPy & Pandas for data handling

scikit-learn for ML model building

Virtual Environment for isolation

**Project Structure**

SONAR-Rock-or-Mine-Project/
│-- sonar_env/          
│-- sonar_data.csv       
│-- sonar_prediction.py  
│-- requirements.txt     
│-- README.md            
│-- .gitignore           

**Installation & Setup**

**1.Clone the repository:**
git clone https://github.com/AkashG-03/Mine-Or-Rock-Prediction-Using-Sonar-Sensor.git
cd Mine-Or-Rock-Prediction-Using-Sonar-Sensor

**2.Create and activate virtual environment:**
python -m venv sonar_env
sonar_env\Scripts\activate   # Windows
source sonar_env/bin/activate # Mac/Linux

**3.Install dependencies:**
pip install -r requirements.txt

**4.Run the script to train and test the model:**
streamlit run app.py
