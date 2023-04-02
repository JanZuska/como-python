import streamlit as st
import pandas as pd
import plotly.express as px

csv = r"countries_gdp.csv"

st.header("Ahoj, vítej ve Streamlitu")
st.markdown("**Python**")

df = pd.read_csv(csv)
st.dataframe(df)

chart = px.bar(df, x = "Country", y = "Population")
st.plotly_chart(chart)
