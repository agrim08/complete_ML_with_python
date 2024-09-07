import streamlit as st
import numpy as np
import pandas as pd

# Adding title in streamlit
st.title("Hello World")

#display text

st.write("This is sample text")

#create a database:
df = pd.DataFrame({
    'first col' : [1,2,3,4],
    'second col' : [5,6,7,8]
})

#display df:
st.write("here is the database ")
st.write(df)

#create a lone chart:
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)

st.line_chart(chart_data)