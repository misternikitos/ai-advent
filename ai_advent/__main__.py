# noqa[T201]

import argparse
import runpy
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Run AI Advent solutions.")
    parser.add_argument("day", nargs="?", type=int, help="The day to run (1-25)")
    args = parser.parse_args()

    day = args.day
    if day is None:
        try:
            day_input = input("Enter day (1-25): ")
            day = int(day_input)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\nExiting.")
            sys.exit(0)

    if not (1 <= day <= 25):  # noqa: PLR2004
        print(f"Day {day} is out of range (1-25).")
        sys.exit(1)

    day_str = f"day{day:02d}"

    # Locate the day's directory relative to this script
    base_dir = Path(__file__).parent / "days"
    day_dir = base_dir / day_str

    if not day_dir.exists():
        print(f"Directory for day {day} not found: {day_dir}")
        sys.exit(1)

    # Check for __main__.py or similar entry point to be robust
    entry_point = day_dir / "solution.py"
    if not entry_point.exists():
        print(f"No solution.py found for day {day} in {day_dir}.")
        print("Please ensure the day's solution is implemented and has an entry point.")
        sys.exit(1)

    print(f"Running solution for Day {day}...")
    print("-" * 40)

    try:
        # executing the solution.py file
        runpy.run_path(str(entry_point), run_name="__main__")
    except Exception as e:  # noqa: BLE001
        print("-" * 40)
        print(f"An error occurred while running day {day}:")
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
