import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

def scrape_github_jobs():
    """
    Scrape job data from a public API (GitHub Jobs alternative - Remotive)
    This is easier and more reliable than web scraping
    """
    print("Fetching job data...")
    
    # Using Remotive API (free, no auth needed)
    url = "https://remotive.com/api/remote-jobs"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        jobs = []
        for job in data['jobs'][:100]:  # Get first 100 jobs
            jobs.append({
                'title': job.get('title', 'N/A'),
                'company': job.get('company_name', 'N/A'),
                'location': job.get('candidate_required_location', 'Remote'),
                'job_type': job.get('job_type', 'N/A'),
                'category': job.get('category', 'N/A'),
                'salary': job.get('salary', 'Not specified'),
                'date_posted': job.get('publication_date', 'N/A'),
                'url': job.get('url', 'N/A')
            })
        
        # Save to CSV
        df = pd.DataFrame(jobs)
        df.to_csv('jobs_data.csv', index=False)
        
        print(f"✓ Successfully scraped {len(jobs)} jobs!")
        print(f"✓ Data saved to jobs_data.csv")
        print(f"\nFirst few jobs:")
        print(df[['title', 'company', 'category']].head())
        
        return df
        
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    scrape_github_jobs()