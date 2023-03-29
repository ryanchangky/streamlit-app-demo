import streamlit as st

st.title("title")

st.markdown("markdown test")

var1 = st.number_input("square feet")

var2 = st.selectbox("num rooms", ("1","2"))

if st.button("predict"):
	var = var1 + int(var2) 
	st.markdown(f"Predicted val is {var}!!!")