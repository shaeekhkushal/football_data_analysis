# ⚽ Football Player Stats Report 2024/25

This project analyzes the performance of all football players in the **Top 5 European Leagues** for the **2024/25** season — with a primary focus on the **English Premier League (EPL)**.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## 🧠 What This Project Does

### ✅ Step-by-step analysis:
- Loads and cleans the original Excel dataset
- Focuses on **EPL** subset for detailed breakdown
- Generates **EDA**:
  - Top goal scorers
  - Assist providers
  - Efficient attackers (G+A/90)
  - Most carded players
  - Overperformers vs underperformers (based on xG)
- Club-level stats:
  - Total team goals, assists, cards, G+A/90
  - Radar comparison between top clubs
- Player comparison:
  - Radar chart comparing top EPL performers
- Predictive squad selection:
  - Builds a **15-player squad** (GK, DF, MF, FW)
  - Based solely on performance metrics
- 📊 Visual formation of the squad (4-3-3)
- 💡 All charts embedded into a single **dark-mode HTML report**

---

## 🚀 How to Run Locally

1. Clone the repo:
   git clone https://github.com/<your-username>/football-stats-24-25.git
   cd football-stats-24-25

Place the top5-players24-25.xlsx in the root folder.

**Run the analysis scripts:
python generate_report.py
python pitch_visual.py
Open football_report_dark.html in your browser.

📈 Tools & Libraries Used
- Python 3.x
- Pandas
- Seaborn, Matplotlib
- NumPy
- Base64, pathlib (for embedding)
- Jupyter Notebook (for iterative dev)
- GitHub for version control
