# 📊 Streamlit Projects

Interactive web applications for data science, financial analysis, and bioinformatics built with Streamlit.

## 🚀 Projects

### 1. 🏈 NFL Football Stats Explorer
**Folder:** `EDA-Football` | **File:** `football_app.py`

NFL rushing statistics analyzer with historical data from 1990-2019.

**Features:**
- Web scrapes data from pro-football-reference.com
- Filter by year, team, and position (RB, QB, WR, FB, TE)
- CSV export and correlation heatmap visualization
- Cached data loading for performance

---

### 2. 📈 S&P 500 Company & Stock Analyzer
**Folder:** `SP500-EDA` | **File:** `sp500-app.py`

S&P 500 company explorer with real-time stock price visualization.

**Features:**
- Scrapes S&P 500 company list from Wikipedia
- Filter by GICS sector with multi-select
- Year-to-date stock price charts (up to 5 companies)
- CSV download and interactive plotting

---

### 3. 🧬 DNA Nucleotide Counter
**Folder:** `DNA-Counter` | **File:** `dna-app.py`

Bioinformatics tool for DNA sequence analysis and nucleotide composition.

**Features:**
- DNA sequence input with FASTA format support
- Counts A, T, G, C nucleotides
- Four output formats: dictionary, text, DataFrame, bar chart
- Pre-loaded sample sequence for testing

---

### 4. 📊 Google Stock Tracker
**Folder:** `Stock-Price-App` | **File:** `app.py`

Simple Google (GOOGL) stock price tracker with historical data (2020-2025).

**Features:**
- Displays closing price and volume trends
- Clean line chart visualizations
- Real-time data via Yahoo Finance API

## 🛠️ Tech Stack

- **Framework:** Streamlit
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn, Altair
- **APIs:** yfinance (Yahoo Finance)
- **Web Scraping:** pandas.read_html()

## 📦 Installation

1. **Clone repository:**
```bash
git clone https://github.com/urvishah305/streamlit-projects.git
cd streamlit-projects
```

2. **Install dependencies:**
```bash
pip install streamlit pandas numpy matplotlib seaborn yfinance altair
```

## ▶️ Usage

Run any application:
```bash
cd [project-folder]
streamlit run [filename].py
```

Applications open at `http://localhost:8501`

## 📊 Data Sources

- **NFL Stats:** pro-football-reference.com
- **S&P 500:** Wikipedia + Yahoo Finance
- **Stock Data:** Yahoo Finance API
- **DNA:** User input with samples
