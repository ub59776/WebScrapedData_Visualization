import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#file path 
csv_file_path = r'C:\Users\ub597\Downloads\applied_jobs_data.xls'

# Load the CSV data into a DataFrame
df = pd.read_csv(csv_file_path)

# Streamlit Title
st.title('Job Applications Visualization')

# Display DataFrame
st.write("### Job Applications Data", df)

# Bar Chart: Number of Applications by Company
st.write("### Number of Applications by Company")
applications_by_company = df['Company'].value_counts()
st.bar_chart(applications_by_company)

# Pie Chart: Distribution by Location
st.write("### Job Locations Distribution")
location_distribution = df['Location'].value_counts()
fig, ax = plt.subplots()
ax.pie(location_distribution, labels=location_distribution.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is drawn as a circle.
st.pyplot(fig)

# Pie Chart: Distribution by Mode of Work
st.write("### Mode of Work Distribution")
mode_of_work= df['Mode of Work'].value_counts()
fig, ax = plt.subplots()
ax.pie(mode_of_work, labels=mode_of_work.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures the pie chart is drawn as a circle.
st.pyplot(fig)

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

# Bar Chart: Application Status (Time Since Application)
st.write("### Application Status - Time Since Application")
status_data = df_sorted[['Company', 'Applied Time']]
st.bar_chart(status_data.set_index('Company'))