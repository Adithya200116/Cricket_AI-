import json
import pandas as pd
import glob
import os

# Store all records
all_deliveries = []

# Get all JSON files
files = glob.glob("data/raw_json/*.json")

print(f"Found {len(files)} JSON files")

# Process every match file
for file in files:

    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Match ID
        match_id = os.path.basename(file).split(".")[0]

        # Match Info
        info = data.get("info", {})

        venue = info.get("venue", "Unknown")
        city = info.get("city", "Unknown")

        dates = info.get("dates", ["Unknown"])
        match_date = dates[0]

        season = str(info.get("season", "Unknown"))
        match_type = info.get("match_type", "Unknown")

        teams = info.get("teams", [])

        toss = info.get("toss", {})
        toss_winner = toss.get("winner", "Unknown")
        toss_decision = toss.get("decision", "Unknown")

        outcome = info.get("outcome", {})
        winner = outcome.get("winner", "No Result")

        innings_data = data.get("innings", [])

        # Store first innings score for target calculation
        first_innings_total = None

        # Process innings
        for innings_index, innings in enumerate(innings_data):

            batting_team = innings.get("team", "Unknown")

            # Bowling team
            bowling_team = ""

            if len(teams) == 2:
                bowling_team = (
                    teams[0]
                    if batting_team != teams[0]
                    else teams[1]
                )

            overs = innings.get("overs", [])

            cumulative_score = 0
            wickets_fallen = 0

            # T20 total balls
            TOTAL_BALLS = 120

            # Target setup
            target_runs = None

            if innings_index == 1 and first_innings_total is not None:
                target_runs = first_innings_total + 1

            # Process overs
            for over_data in overs:

                over_number = over_data.get("over", 0)

                deliveries = over_data.get("deliveries", [])

                for ball_index, delivery in enumerate(deliveries):

                    # Players
                    batter = delivery.get("batter", "Unknown")
                    bowler = delivery.get("bowler", "Unknown")
                    non_striker = delivery.get("non_striker", "Unknown")

                    # Runs
                    runs_data = delivery.get("runs", {})

                    batter_runs = runs_data.get("batter", 0)
                    extra_runs = runs_data.get("extras", 0)
                    total_runs = runs_data.get("total", 0)

                    # Extras
                    extras_data = delivery.get("extras", {})

                    wides = extras_data.get("wides", 0)
                    noballs = extras_data.get("noballs", 0)
                    byes = extras_data.get("byes", 0)
                    legbyes = extras_data.get("legbyes", 0)

                    # Wicket Info
                    wicket = 0
                    wicket_kind = "None"
                    player_out = "None"

                    if "wickets" in delivery:

                        wicket = 1
                        wickets_fallen += len(delivery["wickets"])

                        wicket_info = delivery["wickets"][0]

                        wicket_kind = wicket_info.get(
                            "kind",
                            "Unknown"
                        )

                        player_out = wicket_info.get(
                            "player_out",
                            "Unknown"
                        )

                    # Update score
                    cumulative_score += total_runs

                    # Ball Number
                    ball_number = ball_index + 1

                    # Balls Bowled
                    balls_bowled = (over_number * 6) + ball_number

                    # Prevent invalid values
                    balls_remaining = max(
                        TOTAL_BALLS - balls_bowled,
                        0
                    )

                    # Overs completed
                    overs_completed = balls_bowled / 6

                    # Current Run Rate
                    current_rr = (
                        cumulative_score / overs_completed
                        if overs_completed > 0
                        else 0
                    )

                    # Required Run Rate
                    required_rr = None

                    if (
                        target_runs is not None
                        and balls_remaining > 0
                    ):

                        runs_needed = max(
                            target_runs - cumulative_score,
                            0
                        )

                        required_rr = (
                            runs_needed * 6
                        ) / balls_remaining

                    # Final Row
                    row = {

                        # Match Info
                        "match_id": match_id,
                        "season": season,
                        "date": match_date,
                        "match_type": match_type,
                        "venue": venue,
                        "city": city,

                        # Teams
                        "batting_team": batting_team,
                        "bowling_team": bowling_team,

                        # Toss
                        "toss_winner": toss_winner,
                        "toss_decision": toss_decision,

                        # Result
                        "winner": winner,

                        # Innings
                        "innings": innings_index + 1,

                        # Ball Info
                        "over": over_number,
                        "ball": ball_number,

                        # Players
                        "batter": batter,
                        "bowler": bowler,
                        "non_striker": non_striker,

                        # Runs
                        "batter_runs": batter_runs,
                        "extra_runs": extra_runs,
                        "total_runs": total_runs,

                        # Extras
                        "wides": wides,
                        "noballs": noballs,
                        "byes": byes,
                        "legbyes": legbyes,

                        # Wickets
                        "wicket": wicket,
                        "wicket_kind": wicket_kind,
                        "player_out": player_out,

                        # Match State
                        "cumulative_score": cumulative_score,
                        "wickets_fallen": wickets_fallen,
                        "current_run_rate": round(current_rr, 2),

                        # Chase Metrics
                        "target_runs": target_runs,
                        "balls_remaining": balls_remaining,
                        "required_run_rate": (
                            round(required_rr, 2)
                            if required_rr is not None
                            else 0
                        )
                    }

                    all_deliveries.append(row)

            # Save first innings total
            if innings_index == 0:
                first_innings_total = cumulative_score

    except Exception as e:
        print(f"Error processing {file}: {e}")

# Create DataFrame
df = pd.DataFrame(all_deliveries)

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date column
df["date"] = pd.to_datetime(df["date"], errors="coerce")

# Create output folder
os.makedirs("data/processed", exist_ok=True)

# Save CSV
output_path = "data/processed/all_matches.csv"

df.to_csv(output_path, index=False)

# Summary
print("\n==============================")
print("DATA EXTRACTION COMPLETED")
print("==============================")

print(f"Total Rows: {len(df)}")
print(f"Total Columns: {len(df.columns)}")

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nFirst 5 Rows:")
print(df.head())

print(f"\nCSV Saved At: {output_path}")