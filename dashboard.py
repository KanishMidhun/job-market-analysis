import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Job Market Dashboard", layout="wide")

# Load data
df = pd.read_csv('jobs_data.csv')

# Header
st.title("🎯 Remote Job Market Analysis")
st.markdown("*Real-time insights from current remote job postings*")

# Top metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Jobs", len(df))
with col2:
    st.metric("Categories", df['category'].nunique())
with col3:
    st.metric("Companies", df['company'].nunique())
with col4:
    jobs_with_salary = len(df[df['salary'] != 'Not specified'])
    st.metric("With Salary Info", f"{jobs_with_salary}/{len(df)}")

st.divider()

# Two columns for charts
col_left, col_right = st.columns(2)

with col_left:
    st.subheader("📊 Jobs by Category")
    category_counts = df['category'].value_counts()
    fig1 = px.bar(
        x=category_counts.index, 
        y=category_counts.values,
        labels={'x': 'Category', 'y': 'Jobs'},
        color=category_counts.values,
        color_continuous_scale='Blues'
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_right:
    st.subheader("💼 Job Types")
    job_type_counts = df['job_type'].value_counts()
    fig2 = px.pie(
        values=job_type_counts.values,
        names=job_type_counts.index
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

# Full width chart
st.subheader("🏢 Top Hiring Companies")
top_companies = df['company'].value_counts().head(10)
fig3 = px.bar(
    y=top_companies.index,
    x=top_companies.values,
    orientation='h',
    labels={'x': 'Number of Jobs', 'y': 'Company'},
    color=top_companies.values,
    color_continuous_scale='Greens'
)
st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Show raw data
st.subheader("📋 Raw Data")
st.dataframe(df, use_container_width=True)