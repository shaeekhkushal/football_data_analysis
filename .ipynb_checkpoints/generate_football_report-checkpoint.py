import base64
from pathlib import Path

# === Setup ===
project_dir = Path.cwd()
output_file = project_dir / "final_report.html"

# === Chart Titles, Filenames & Descriptions ===
chart_data = [
    ("⚽ Top 20 Goal Scorers", "top_goal_scorers.png", 
     "These are the top scorers in the EPL 24/25 season, led by players with the highest total goals scored."),
    
    ("🎯 Top 20 Assist Providers", "top_assist_providers.png", 
     "This chart highlights players who created the most goals for their teammates via assists."),
    
    ("⚡ Most Efficient Players (G+A/90)", "top_efficient_players.png", 
     "Efficiency measured by Goals + Assists per 90 mins. Shows impact regardless of total minutes played."),
    
    ("🟥 Most Carded Players", "top_carded_players.png", 
     "The most disciplined-challenged players based on total yellow and red cards received."),
    
    ("📈 Goal Overperformers", "top_goal_overperformers.png", 
     "Players who scored more than their xG (expected goals), suggesting clinical finishing."),
    
    ("📉 Goal Underperformers", "top_goal_underperformers.png", 
     "Players whose goal tally is lower than expected based on their xG. Indicates missed opportunities."),
    
    ("🏟️ Clubs by Total Goals", "club_total_goals.png", 
     "Which clubs scored the most? A quick look at team attacking power."),
    
    ("🎯 Clubs by Total Assists", "club_total_assists.png", 
     "Team playmakers and how often each club set up goals."),
    
    ("🟥 Clubs by Total Cards", "club_total_cards.png", 
     "A summary of the most and least disciplined teams in the league."),
    
    ("⚡ Clubs by Avg G+A/90", "club_ga90_avg.png", 
     "Average offensive contribution per 90 mins across squads. Reveals team effectiveness."),
    
    ("🏆 Club Radar Comparison", "epl_club_radar.png", 
     "Radar comparison between clubs across key performance metrics."),
    
    ("🏅 EPL Player Comparison", "epl_top_players_comparison.png", 
     "A visual comparison of selected top EPL players across core stats."),
    
    ("📋 Best EPL Squad Prediction for 2025/26(Visual Formation)", "epl_pitch_squad.png", 
     "This 4-3-3 formation showcases the prediction of top-performing EPL players by position for the 25/26 season.")
]

# === Encode image to base64 ===
def embed_image(img_path):
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# === Build HTML sections ===
sections = []
for title, filename, description in chart_data:
    img_path = project_dir / filename
    if img_path.exists():
        img_base64 = embed_image(img_path)
        sections.append(f"""
        <section>
            <h2>{title}</h2>
            <p>{description}</p>
            <img src="data:image/png;base64,{img_base64}" />
        </section>
        """)

# === Final HTML (Dark Mode) ===
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>📊 Football Player Stats Report 2024/25 (Dark Mode)</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            padding: 40px;
            background-color: #121212;
            color: #e0e0e0;
        }}
        h1, h2 {{
            color: #ffffff;
        }}
        section {{
            background-color: #1e1e1e;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.6);
            margin-bottom: 40px;
        }}
        p {{
            font-size: 16px;
            color: #cccccc;
            margin-bottom: 16px;
        }}
        img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            border: 1px solid #333;
        }}
    </style>
</head>
<body>
    <h1>📊 Football Player Stats Report 2024/25</h1>
    {"".join(sections)}
</body>
</html>
"""

# === Write to file ===
with open(output_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"✅ report saved to: {output_file}")
