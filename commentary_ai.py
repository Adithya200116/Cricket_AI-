import random

print("=" * 60)
print("COMMENTARY AI")
print("=" * 60)

event = input("Enter Event: ")

six_comments = [

    "What a magnificent six!",
    "That ball has disappeared!",
    "Absolutely launched into the crowd!",
    "Pure timing from the batter!"
]

four_comments = [

    "Beautifully timed boundary!",
    "Races away to the fence!",
    "Excellent placement!",
    "No chance for the fielder!"
]

wicket_comments = [

    "OUT! Massive breakthrough!",
    "The batter has to go!",
    "Brilliant bowling!",
    "The crowd erupts!"
]

event = event.lower()

if "six" in event:

    print(random.choice(
        six_comments
    ))

elif "four" in event:

    print(random.choice(
        four_comments
    ))

elif "wicket" in event:

    print(random.choice(
        wicket_comments
    ))

else:

    print(
        "Interesting passage of play."
    )