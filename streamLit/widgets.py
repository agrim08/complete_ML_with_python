import streamlit as st
import pandas as pd

st.title("Text Input in streamLit")

#Single Line Input Feild
name = st.text_input("Enter your name :")
if name:
    st.write(f"hello, {name}")


#multi line input feild
para = st.text_area("Enter your para")  
if "Machine Learning" in para:
    st.write("Keep going, ML is a very good profession")  

#creating a slider:
age = st.slider("Select your age : " ,0,100,25)
st.write(f"Your age is {age}")

#Selctbox:
options = ["select","Python","Java","Cpp","JS"]
choice = st.selectbox("Choose your fav language :" , options)
if choikoce == 'select':
    st.write("Choose an option")
else:
    st.write(f"{choice} is a good choice")

data =  {
    "names": ["Alice", "Bob", "Charlie", "Diana", "Eva"],
    "ages": [28, 35, 22, 40, 31],
    "cities": ["New York", "Los Angeles", "Chicago", "Houston", "Miami"]
}

df = pd.DataFrame(data)
st.write(df)

upload_file = st.file_uploader("Choose a csv file",type = 'csv')
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)