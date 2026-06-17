print("=" * 60)
print("PRESSURE INDEX CALCULATOR")
print("=" * 60)

current_rr = float(
    input("Current Run Rate: ")
)

required_rr = float(
    input("Required Run Rate: ")
)

pressure_index = (
    required_rr - current_rr
)

print("\n")

print(
    f"Pressure Index: {pressure_index:.2f}"
)

if pressure_index <= 0:

    print(
        "Batting team is comfortable."
    )

elif pressure_index < 2:

    print(
        "Moderate pressure."
    )

elif pressure_index < 4:

    print(
        "High pressure."
    )

else:

    print(
        "Extreme pressure."
    )