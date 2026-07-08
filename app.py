import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Student Placement Readiness Analysis Dashboard")


# Load dataset
df = pd.read_csv("Cleaned_Student_Placement_Readiness_Data.csv")


st.subheader("Dataset Preview")
st.dataframe(df.head())


# Dashboard 1

st.header("Student Skills Dashboard")


fig1 = px.histogram(
    df,
    x="2.  Current CGPA",
    title="CGPA Distribution"
)

st.plotly_chart(fig1)


fig2 = px.pie(
    df,
    names="6. Have you completed any internships?",
    title="Internship Status"
)

st.plotly_chart(fig2)


fig3 = px.bar(
    df,
    x="7. How many certifications have you completed?",
    title="Certification Analysis"
)

st.plotly_chart(fig3)


# Dashboard 2

st.header("Placement Preparation Dashboard")


fig4 = px.bar(
    df,
    x="8. How would you rate your communication skills?",
    title="Communication Skills"
)

st.plotly_chart(fig4)


fig5 = px.pie(
    df,
    names="12. Is your resume ready?",
    title="Resume Readiness"
)

st.plotly_chart(fig5)


fig6 = px.histogram(
    df,
    x="13. How confident are you in attending placement interviews?",
    title="Interview Confidence"
)

st.plotly_chart(fig6)


st.header("Insights")

st.write("""
- CGPA, projects and internships affect placement preparation.
- Regular coding practice improves technical readiness.
- Certifications improve student skills.
- Resume preparation and communication skills are important for placements.
""")
