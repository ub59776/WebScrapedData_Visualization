import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

#file path 
csv_file_path = r'C:\Users\ub597\Downloads\profile_applied_jobs_data.xls'

# Load the CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Streamlit App
st.title("Applicant Data Analysis")

# Sidebar for filtering
st.sidebar.header("Filters")
selected_college = st.sidebar.multiselect("Select College", df['College'].unique(), default=df['College'].unique())
selected_mode_of_work = st.sidebar.multiselect("Select Mode of Work", df['Mode of Work'].unique(), default=df['Mode of Work'].unique())

# Filter Data
filtered_df = df[(df['College'].isin(selected_college)) & (df['Mode of Work'].isin(selected_mode_of_work))]

# Show the filtered data
st.write("Filtered Data", filtered_df)

# Pie chart for applicants per company
company_counts = filtered_df['Company'].value_counts()
fig_pie = px.pie(values=company_counts.values, names=company_counts.index, title="Applicants per Company")
st.plotly_chart(fig_pie)

# Horizontal Bar chart for number of companies applied by each candidate
candidate_counts = filtered_df['Name'].value_counts()
fig_bar_h = px.bar(x=candidate_counts.values, y=candidate_counts.index, orientation='h', title="Number of Companies Applied by Each Candidate")
st.plotly_chart(fig_bar_h)

# Vertical Bar chart for applicant locations
location_counts = filtered_df['ApplicantLocation'].value_counts()
fig_bar_v = px.bar(x=location_counts.index, y=location_counts.values, title="Applicants Location Distribution")
st.plotly_chart(fig_bar_v)

# Line Chart: Applications over Time (based on Status)
st.write("### Applications Over Time")
df['Applied Time'] = df['Applied on'].str.extract(r'(\d+)(\w)').apply(lambda x: pd.to_numeric(x[0]) * (168 if x[1] == 'w' else 720 if x[1] == 'mo' else 1), axis=1)
df_sorted = df.sort_values('Applied Time')
plt.figure(figsize=(10, 6))
sns.lineplot(x='Company', y='Applied Time', data=df_sorted, marker="o", linewidth=2)
plt.xlabel('Company')
plt.ylabel('Time Applied (in hours)')
plt.title('Applications Over Time')
st.pyplot(plt)

# Applicants per College
college_counts = filtered_df['College'].value_counts()
fig_college = px.bar(x=college_counts.index, y=college_counts.values, title="Applicants per College")
st.plotly_chart(fig_college)

# Applicants per job title
job_title_counts = filtered_df['Job Title'].value_counts()
fig_job_title = px.pie(values=job_title_counts.values, names=job_title_counts.index, title="Applicants per Job Title")
st.plotly_chart(fig_job_title)

