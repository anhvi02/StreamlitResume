import numpy as np
import pandas as pd
import joblib
import streamlit as st
# settting streamlit
st.set_page_config(layout = 'centered',
                    # page_icon="🧊",
                    page_title="Stroke Prediction")

st.title('Stroke Prediction Project')

# TAB INITIALIZING
model, dashboard, code, about = st.tabs(["Model","Dashboard", "Code","About"])


# --------------- TAB MODEL ----------------------
with model:
    # input of the model
    st.subheader('Please input your data')
    data = np.zeros(14)

    # -- CHECKBOXES
    def binary_feature(content):
        choice = st.checkbox(content)
        value = 0
        if choice:
            value = 1
        return value
    col1, col2, col3 = st.columns(3)
    with col1: 
        heart_disease = binary_feature('Heart Disease')
    with col2:
        hyptertension = binary_feature('Hypertension')
    with col3:
        ever_married_Yes = binary_feature('Married')

    # -- OTHER DATA
    col1, col2 = st.columns(2)
    # - column1: 3 numeric feature
    with col1:
        age = st.number_input('Age', 0, 125)
        avg_glucose_level = st.number_input('Average Glucose Level', 0.0, 500.0,step=0.001)
        bmi = st.number_input('BMI', 0.0, 100.0,step=0.001)

    # - column2: 3 multiple choices feature
    with col2: 
        def multi_feature(content, list_choices, exception):
            size = len(list_choices) - len(exception)
            value = np.zeros(size)
            choice = st.selectbox(content, list_choices)
            if choice in exception:
                return value
            else:
                for ind,ele in enumerate(list_choices):
                    if ele == choice:
                        value[ind] = 1
                return value

        gender = st.selectbox('Gender', ['Male', 'Female','Other'])
        work_type = st.selectbox('Work Type', ['Never worked', 'Self-employed','Children','Private'])
        living = st.selectbox('Residence Type', ['Urban', 'Rural'])
        # test = multi_feature('test', ['Male','Female'])

    smoke = st.selectbox('Smoking Status', ['Never smoke', 'Formerly smoked', 'Smokes'])

    # -- PREDICT BUTTON
    col1, col2, col3 = st.columns([1,0.4,1])
    with col2:
        st.button("Predict")

# load model
model = joblib.load("model.sav")
# feat = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi',
#        'gender_Male', 'gender_Other', 'ever_married_Yes',
#        'work_type_Never_worked', 'work_type_Self-employed',
#        'Residence_type_Urban', 'smoking_status_formerly smoked',
#        'smoking_status_never smoked', 'smoking_status_smokes']





# --------------- TAB DASHBOARD ----------------------
with dashboard:
    st.subheader("Stroke Data Dashboard")
    # import data:
    df = pd.read_csv('cleaned_data.csv')

    # -- DATAFRAME
    showdata = st.checkbox("Display Data")
    if showdata:
        st.dataframe(df, width=1920)

    # -- METRICS
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

    # -- VISUALIZATIONS
    vi1, vi2= st.columns((7,3))

    # distribution plots
    with vi1:
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

    # pie plot
    # with vi2:

