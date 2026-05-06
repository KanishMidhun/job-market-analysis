import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
df = pd.read_csv('jobs_data.csv')

# 1. Jobs by Category (Bar chart)
category_counts = df['category'].value_counts()
fig1 = px.bar(
    x=category_counts.index, 
    y=category_counts.values,
    title='Jobs by Category',
    labels={'x': 'Category', 'y': 'Number of Jobs'},
    color=category_counts.values,
    color_continuous_scale='Blues'
)
fig1.write_html('chart_categories.html')
print("✓ Created chart_categories.html")

# 2. Job Types (Pie chart)
job_type_counts = df['job_type'].value_counts()
fig2 = px.pie(
    values=job_type_counts.values,
    names=job_type_counts.index,
    title='Job Types Distribution'
)
fig2.write_html('chart_job_types.html')
print("✓ Created chart_job_types.html")

# 3. Top Companies (Horizontal bar)
top_companies = df['company'].value_counts().head(10)
fig3 = px.bar(
    y=top_companies.index,
    x=top_companies.values,
    orientation='h',
    title='Top 10 Hiring Companies',
    labels={'x': 'Number of Jobs', 'y': 'Company'},
    color=top_companies.values,
    color_continuous_scale='Greens'
)
fig3.write_html('chart_companies.html')
print("✓ Created chart_companies.html")

print("\n🎨 All charts created! Open the HTML files in your browser to view them.")