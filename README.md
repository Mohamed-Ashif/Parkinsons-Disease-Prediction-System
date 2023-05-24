
# Parkinson's Disease Prediction Using Machine Learning

This project aims to develop a machine learning model for predicting Parkinson's disease based on available data. Early detection and prediction of Parkinson's disease can assist in timely intervention and personalized treatment plans, improving patient outcomes.


![parkinsons-disease-image](https://github.com/Mohamed-Ashif/parkinsons-disease-prediction/assets/78372127/11d255bf-b97e-410b-8250-e8740d38510f)



## Dataset

This dataset is composed of a range of biomedical voice measurements from 31 people, 23 with Parkinson's disease (PD). Each column in the table is a particular voice measure, and each row corresponds to one of 195 voice recordings from these individuals ("name" column). The main aim of the data is to discriminate healthy people from those with PD, according to the "status" column which is set to 0 for healthy and 1 for PD.


## Attributes Information

■ Name - ASCII subject name and recording number

■ MDVP:Fo(Hz) - Average vocal fundamental frequency

■ MDVP:Fhi(Hz) - Maximum vocal fundamental frequency

■ MDVP:Flo(Hz) - Minimum vocal fundamental frequency

■ MDVP:Jitter(%), MDVP:Jitter(Abs), MDVP:RAP, MDVP:PPQ, Jitter:DDP - Several measures of variation in fundamental frequency

■ MDVP:Shimmer, MDVP:Shimmer(dB), Shimmer:APQ3, Shimmer:APQ5,MDVP:APQ, Shimmer:DDA - Several measures of variation in amplitude

■ NHR, HNR - Two measures of the ratio of noise to tonal components in the voice

■ status - The health status of the subject (one) - Parkinson's, (zero) - healthy

■ RPDE, D2 - Two nonlinear dynamical complexity measures

■ DFA - Signal fractal scaling exponent

■ spread1, spread2, PPE - Three nonlinear measures of fundamental frequency variation


## Requirements

To run the Streamlit application and reproduce the results of this project, the following dependencies are required:

◉ Python 3.9

◉ Pandas

◉ NumPy

◉ Scikit-learn

◉ Pickle

◉ Streamlit

◉ Streamlit-option-menu


## Project Structure

The project consists of the following files:

1. parkinsons.csv: The dataset file containing the features and target variable.

2. Parkinson's Disease Prediciton.ipynb:  Python script that includes the code for data preprocessing, model training, evaluation, and prediction.

3. parkinsons_model.sav: It is a saved machine learning model file, potentially used for Parkinson's disease prediction, with the ".sav" extension commonly associated with serialized models in Python.

4. app.py: Python script that includes the code for the Streamlit application.

4. requirements.txt: This file lists the external dependencies and their versions for a Python project, facilitating easy installation of the required packages.

6. README.md: Project documentation providing an overview of the project and instructions.


## Instructions

1. Install the required dependencies mentioned in the "Requirements" section.

2. Clone or download the project repository.

3. Open the Parkinson's Disease Prediciton.ipynb file

4. Follow the code to preprocess the data, train the ML model, evaluate its performance, and make predictions.

5. Save the ml model into parkinsons_model.sav file for webapp prediction.

6. Run the script using the command python app.py.

7. Once the script is running, it will launch a Streamlit application locally.

8. Access the Streamlit application in your web browser at the provided URL.

9. Use the interactive interface to input the necessary data for predicting the likelihood of Parkinson's disease.

10. The application will display the prediction results and any relevant visualizations.


## Screenshot

![Screenshot ](https://github.com/Mohamed-Ashif/parkinsons-disease-prediction/assets/78372127/f479e998-8253-41ed-b14b-3e31aecf63c5)


## Conclusion

This project demonstrates the application of machine learning techniques for predicting Parkinson's disease and deploys the model using Streamlit. The Streamlit application provides a user-friendly interface to interactively input data and obtain predictions for Parkinson's disease. The deployment allows for easy accessibility and utilization of the model by healthcare professionals and stakeholders.

