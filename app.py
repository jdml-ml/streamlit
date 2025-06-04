import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mi App Streamlit", page_icon="smile", layout="wide", initial_sidebar_state="collapsed")

df = pd.read_csv("covid_data.csv")

def main():
    st.title("Curso de Streamlit")
    st.sidebar.header("Navegación")
    st.dataframe(df)
    df_count = df.groupby('Gender').count().reset_index()
    fig = px.pie(df_count, values="Patient_ID", names="Gender", title="Género")
    st.plotly_chart(fig)
    df_avg = df.groupby("Gender")['BMI'].mean().reset_index()
    fig2 = px.bar(df_avg, x="Gender", y="BMI", color="Gender", title="Promedio BMI por género")
    # df_avg = df.groupby("Gender")['COVID_Strain'].count().reset_index()
    # fig2 = px.bar(df_avg, x="Gender", y="COVID_Strain", color="Gender")
    # df_avg_age = df.groupby("Gender")['Age'].mean().reset_index()
    # fig3 = px.bar(df_avg_age, x="Gender", y="Age", color="Gender")
    st.plotly_chart(fig2)
    # st.plotly_chart(fig3)# 1. Casos por género
    # Conteo por género
    df_gender = df['Gender'].value_counts().reset_index()
    df_gender.columns = ['Gender', 'Count']  # Renombra columnas

    fig = px.bar(df_gender, x='Gender', y='Count', title='Casos por género')
    st.plotly_chart(fig)

    # 2. Severidad por cepa
    fig_sev = px.histogram(df, x='COVID_Strain', color='Severity',
                        barmode='group', title='Severidad por variante')
    st.plotly_chart(fig_sev)

    # 3. Estado de vacunación
    fig_vac = px.pie(df, names='Vaccination_Status', title='Estado de vacunación')
    st.plotly_chart(fig_vac)

    # 4. Casos por mes
    df['Date_of_Infection'] = pd.to_datetime(df['Date_of_Infection'])
    df['Mes'] = df['Date_of_Infection'].dt.strftime('%Y-%m')  # Formato texto

    fig_time = px.histogram(df, x='Mes', title='Casos por mes')
    st.plotly_chart(fig_time)    

if __name__ == '__main__':
    main()