import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

@st.cache
def load_data():
    data = pd.read_csv("data.csv")
    return data

df = load_data()

year = st.sidebar.slider("Please select a year:", min_value = df["year"].min(), max_value=df["year"].max())
countries = st.sidebar.multiselect("Please select one or more contries:", df["country"].unique())

subset = df[(df["year"] == year)& df["country"].isin(countries)]

if st.sidebar.checkbox("Show Data"):
    st.write(subset)

def chart_graph():
    bubble = sns.scatterplot(data = subset, x = 'GNI', y = 'Life_expectancy', size = 'Population', hue = 'country')
    bubble.set(xscale='log')
    bubble.set(xlim=(None,df["GNI"].max()))
    bubble.set(ylim=(df["Life_expectancy"].min(),df["Life_expectancy"].max()))

chart_graph()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()