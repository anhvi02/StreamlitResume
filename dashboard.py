import numpy as np
import pandas as pd
import seaborn as sns 
import streamlit as st
import matplotlib.pyplot as plt

# settting streamlit
st.set_page_config(layout = 'wide')
# CREATE TABS
# model, dashboard, code, about = st.tabs(["Model", "Dashboard","Code",'About'])

# DASHBOARD
st.title("Stroke Data Dashboard")
# import data:
df = pd.read_csv('cleaned_data.csv')

# display dataframe
showdata = st.checkbox("Display Data")
if showdata:
    st.dataframe(df, width=1920)

# core metrics
me1, me2, me3 = st.columns(3)
with me1:
    records_cnt = len(df)
    st.metric("Total of cases", records_cnt)
with me2:
    avg_age = round(df['age'].mean())
    st.metric("Average age", avg_age)
with me3:
    death_rate = round(df['stroke'].value_counts()[1]/len(df)*100,2)
    st.metric('Death rate', f"{death_rate}%")

# other metric
di1, di2= st.columns((7,3))


# distribution
with di1:
    # function
    def plot_distribution(series, name):
        col_name = series.name
        df_dis = pd.DataFrame(series.value_counts()).reset_index()
        df_dis = df_dis.rename({'index':name,col_name:'Frequency'}, axis=1)
        st.bar_chart(df_dis, x=name, y ='Frequency')
        return df_dis

    dis_options = ['Age Distribution', 'BMI Score Distribution', 'Average Glucose Level Distribution']
    dis_choice = st.selectbox('Data Distribution',dis_options )
    if dis_choice == 'Age Distribution':
        plot_distribution(df['age'],'Age')
    elif dis_choice == 'BMI Score Distribution':
        plot_distribution(df['bmi'],'BMI Score')
    else:
        plot_distribution(df['avg_glucose_level'],'Average Glucose Level')













# correlation heatmap
# get dummies
# df_dum = pd.get_dummies(df, columns=cate_col, drop_first=True)
# pearson correlation
# corr = df.corr()

# # Generate a custom diverging colormap
# cmap = sns.diverging_palette(230, 20, as_cmap=True)

# # plotting
# plt.figure(figsize=(15,13))
# sns.heatmap(data=corr,annot=True, cmap=cmap)
# plt.show()

