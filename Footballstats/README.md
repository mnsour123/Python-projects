# Soccer Data Analysis Project

A Python project for exploring and visualizing football (soccer) match data — team performance, match results, and scoring trends.

## Overview

This project loads a season's worth of match data, cleans it up, and produces summary stats and visualizations, including:

- Total goals scored per team
- Distribution of match results (Home win / Draw / Away win)
- Average goals per match over time

## Data Source

Match data is pulled from [football-data.co.uk](https://www.football-data.co.uk/), a free source of historical football match statistics (goals, shots, cards, and more) organized by league and season.

Example dataset used: Premier League 2023/24 season
`https://www.football-data.co.uk/mmz4281/2324/E0.csv`

To analyze a different league or season, swap the `url` variable for another CSV link from the same site.

## Requirements

- Python 3.8+
- pandas
- matplotlib
- seaborn

Install dependencies:

```bash
pip install pandas matplotlib seaborn
```

## Usage

Run the script:

```bash
python soccer_analysis.py
```

This will:

1. Download and load the match data into a pandas DataFrame
2. Clean and prepare the data (parse dates, compute total goals)
3. Print a summary of goals scored per team
4. Generate three charts:
   - Bar chart of total goals scored by team
   - Count plot of match result distribution
   - Line chart of average goals per match over time (weekly)

## Dataset Columns (key fields)

| Column   | Description               |
| -------- | ------------------------- |
| Date     | Match date                |
| HomeTeam | Home team name            |
| AwayTeam | Away team name            |
| FTHG     | Full-time home team goals |
| FTAG     | Full-time away team goals |
| FTR      | Full-time result (H/D/A)  |

## Roadmap / Ideas for Extension

- [ ] Home vs. away performance comparison
- [ ] Correlation between shots and goals scored
- [ ] Win/loss/draw streak tracking per team
- [ ] League table reconstruction from match results
- [ ] Multi-season comparison

## Project Structure

```
.
├── soccer_analysis.py   # Main analysis script
└── README.md            # Project documentation
```

## License

For personal/educational use. Data usage subject to football-data.co.uk's terms.
