# -*- coding: utf-8 -*-
"""
Created on Mon May 22 10:07:53 2023

@author: Mohamed Ashif H
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

parkinsons_model = pickle.load(open('C:/Users/Dell/myenv/Projects/Parkinson Disease Prediction/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                    
                          ['Parkinsons Prediction'],
                          icons=['person'],
                          default_index=0
                          
                          )
    
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        fo = st.text_input('MDVP: Fo(Hz)')
        st.write(fo)
        
    with col2:
        fhi = st.text_input('MDVP: Fhi(Hz)')
        st.write(fhi)
        
    with col3:
        flo = st.text_input('MDVP: Flo(Hz)')
        st.write(flo)
        
    with col4:
        Jitter_percent = st.text_input('MDVP: Jitter(%)')
        st.write(Jitter_percent)
        
    with col1:
        Jitter_Abs = st.text_input('MDVP: Jitter(Abs)')
        st.write(Jitter_Abs)
        
    with col2:
        RAP = st.text_input('MDVP: RAP')
        st.write(RAP)
        
    with col3:
        PPQ = st.text_input('MDVP: PPQ')
        st.write(PPQ)
        
    with col4:
        DDP = st.text_input('Jitter: DDP')
        st.write(DDP)
        
    with col1:
        Shimmer = st.text_input('MDVP: Shimmer')
        st.write(Shimmer)
        
    with col2:
        Shimmer_dB = st.text_input('MDVP: Shimmer(dB)')
        st.write(Shimmer_dB)
        
    with col3:
        APQ3 = st.text_input('Shimmer: APQ3')
        st.write(APQ3)
        
    with col4:
        APQ5 = st.text_input('Shimmer: APQ5')
        st.write(APQ5)
        
    with col1:
        APQ = st.text_input('MDVP: APQ')
        st.write(APQ)
        
    with col2:
        DDA = st.text_input('Shimmer: DDA')
        st.write(DDA)
        
    with col3:
        NHR = st.text_input('NHR')
        st.write(NHR)
        
    with col4:
        HNR = st.text_input('HNR')
        st.write(HNR)
        
    with col1:
        RPDE = st.text_input('RPDE')
        st.write(RPDE)
        
    with col2:
        DFA = st.text_input('DFA')
        st.write(DFA)
        
    with col3:
        spread1 = st.text_input('spread1')
        st.write(spread1)
        
    with col4:
        spread2 = st.text_input('spread2')
        st.write(spread2)
        
    with col1:
        D2 = st.text_input('D2')
        st.write(D2)
        
    with col2:
        PPE = st.text_input('PPE')
        st.write(PPE)
        
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)
