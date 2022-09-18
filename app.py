# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st
import pandas as pd
import seaborn as sns


st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

#upload dataset

upload = st.file_uploader("Upload your Dataset (In CSV Format)")
if upload is not None:
    data = pd.read_csv(upload)

if upload is not None:   
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            

#check datatype of each column
if upload is not None:  
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes.astype(str))
        
if upload is not None:  
    data_shape = st.radio("What Dimension Do you Want To Check?", ('Rows','Columns'))
    if data_shape =='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Rows")
        st.write(data.shape[1])
        
#find null values    
if upload is not None:  
    test = data.isnull().values.any()
    if test==True:
        st.title("seyma")
        if st.checkbox("Null Values in the dataset"):
            st.title("ozler")
            sns.heatmap(data.isnull())
            st.pyplot()
    else:
        st.success("congratulations!!!, No missing values")

#find dublicate values
if upload is not None:  
    test = data.duplicated().any()
    if test == True:
        st.warning("This dataset contains some dublicate values")
        dup = st.selectbox("Do you want to remove duplicate values",\
                           ("Select one", "Yes", "No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate values are removed")
        if dup== "No":
            st.text("Ok no problem")
            

if upload is not None:  
    if st.checkbox("Summary of the dataset"):
        st.write(data.describe())
        
if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("thanks to streamlit")
            


        
