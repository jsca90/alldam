import time  
import numpy as np 
import pandas as pd 
import plotly.express as px  
import streamlit as st 
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="충청남도 어린이집, 유치원 현황",
    page_icon="✅",
    layout="wide",
)

# read csv from a github repo
dataset_path = 'birth_2016_2021.csv'

# read csv from a URL
@st.experimental_memo
def get_data() -> pd.DataFrame:
    return pd.read_csv(dataset_path)

df = get_data()

# dashboard title
st.title("충청남도 어린이집, 유치원 현황")




# # creating a single-element container
placeholder = st.empty()

# # dataframe filter



# creating KPIs
avg_age = np.mean(df["출생아수"])


with placeholder.container():

 

    col1, col2, col3 = st.columns(3)

    with col1:
       city_filter = st.selectbox("시군구", pd.unique(df["시군별"]))
       ls = df[df["시군별"] == city_filter]

    with col2:
       cty_filter = st.selectbox("시군구", pd.unique(df["연도"]))
       df = df[df["연도"] == cty_filter]

    with col3:
       ciy_filter = st.selectbox("시군구", pd.unique(df["출생아수"]))
       df = df[df["출생아수"] == ciy_filter]

    
    



    # create three columns
    kpi1, kpi2, kpi3 = st.columns(3)

    # fill in those three columns with respective metrics or KPIs
    kpi1.metric(
        label=f"평균 {city_filter} 출생아 수",
        value=round(avg_age),
        delta=round(avg_age) - 10,)

    kpi2.metric(
        label=f"평균 {city_filter} 출생아 수",
        value=round(avg_age),
        delta=round(avg_age) - 10,)

    kpi3.metric(
        label=f"평균 {city_filter} 출생아 수",
        value=round(avg_age),
        delta=round(avg_age) - 10,)


    fig_col1, fig_col2, fig_col3 = st.columns(3)

    with fig_col1:
        st.markdown("2016~2021 출생아수 현황")
        plt.figure(figsize=(10,5))
        fig = px.bar(data_frame=ls, y='출생아수', x="연도")
        st.write(fig)
        
    with fig_col2:
        st.markdown("### 2 Chart")
        plt.figure(figsize=(10,5))
        fig = px.bar(data_frame=df, y='출생아수', x="연도")
        st.write(fig)

    with fig_col3:
        st.markdown("### 3 Chart")
        plt.figure(figsize=(10,5))
        fig = px.bar(data_frame=df, y='출생아수', x="연도")
        st.write(fig)
        


    
