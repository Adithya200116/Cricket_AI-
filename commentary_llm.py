import random

templates = {

    "six":[

        "What a sensational six! The crowd erupts in celebration.",

        "That's gone miles into the stands!",

        "An extraordinary strike from the batter."
    ],

    "four":[

        "Beautifully timed and away for four.",

        "No chance for the fielders there.",

        "Exquisite placement. Four runs."
    ],

    "wicket":[

        "OUT! A huge breakthrough.",

        "The batter has to walk back.",

        "Brilliant bowling under pressure."
    ],

    "single":[

        "Quick single taken.",

        "Good running between the wickets."
    ],

    "dot":[

        "Excellent delivery. No run scored.",

        "Pressure building with another dot ball."
    ]
}

event = input(
    "Enter Event: "
).lower()

for key in templates:

    if key in event:

        print(
            random.choice(
                templates[key]
            )
        )

        break

else:

    print(
        "Interesting phase of play."
    )