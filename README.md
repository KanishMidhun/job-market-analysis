# 🎯 Remote Job Market Analysis Dashboard

A Python-based data analysis project that scrapes, analyzes, and visualizes remote job market trends in real-time.

![Dashboard Preview](dashboard_preview.png)

## 📊 Features

- **Automated Data Collection**: Scrapes remote job postings from Remotive API
- **Interactive Visualizations**: Clean, professional charts using Plotly
- **Live Dashboard**: Streamlit-powered web interface
- **Data Analysis**: Identifies trends in job categories, companies, and employment types

## 🛠️ Tech Stack

- **Python 3.13**
- **Pandas** - Data manipulation
- **Plotly** - Interactive visualizations  
- **Streamlit** - Dashboard framework
- **BeautifulSoup4** - Web scraping
- **Requests** - API calls

## 🚀 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/job-market-analysis.git
cd job-market-analysis
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the scraper:
```bash
python scraper.py
```

4. Launch the dashboard:
```bash
streamlit run dashboard.py
```

## 📈 Sample Insights

- **Software Development** dominates with 41% of remote positions
- **54.5%** of jobs are full-time positions
- **100%** of listings include salary information
- Top hiring companies: Lemon.io, TELUS Digital, Coalition Technologies

## 📁 Project Structure

job-market-analysis/
├── scraper.py              # Data collection
├── quick_analysis.py       # Statistical analysis
├── visualize.py           # Chart generation
├── dashboard.py           # Streamlit dashboard
├── jobs_data.csv          # Scraped data
└── README.md              # Documentation

## 🎨 Visualizations

The project generates three main visualizations:
1. **Jobs by Category** - Bar chart showing distribution
2. **Job Types** - Pie chart of employment types
3. **Top Companies** - Horizontal bar of hiring leaders

## 📝 Future Enhancements

- [ ] Multi-source scraping (Indeed, LinkedIn, etc.)
- [ ] Salary range analysis and predictions
- [ ] Weekly trend tracking
- [ ] Email alerts for new postings
- [ ] Deploy to Streamlit Cloud

## 📄 License

MIT License - feel free to use for your own projects!

## 👤 Author

Built as a portfolio project to demonstrate data scraping, analysis, and visualization skills.