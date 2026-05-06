import pandas as pd

# Load the data
df = pd.read_csv('jobs_data.csv')

print("=" * 50)
print("JOB MARKET INSIGHTS")
print("=" * 50)

print(f"\n📊 Total jobs analyzed: {len(df)}")

print("\n🏢 Top 10 hiring companies:")
print(df['company'].value_counts().head(10))

print("\n💼 Jobs by category:")
print(df['category'].value_counts())

print("\n🌍 Top locations:")
print(df['location'].value_counts().head(10))

print("\n💰 Jobs with salary info:")
salary_mentioned = df[df['salary'] != 'Not specified']
print(f"{len(salary_mentioned)} out of {len(df)} jobs mention salary")

print("\n🔥 Most common job types:")
print(df['job_type'].value_counts())