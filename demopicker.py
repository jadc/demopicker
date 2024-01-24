# Demo Picker by jadc

import argparse, csv, random
from pathlib import Path
from datetime import datetime

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("csv", type=str, help="students csv (from 'Participants' tab on eClass)")
    p.add_argument("-p", "--proportion", type=float, default=1/3, help="proportion of students that should demo (default 1/3)")
    p.add_argument("-d", "--dir", type=str, default="demos", help="directory to store demo lists (default './demos')")
    args = p.parse_args()

    # Extract names from csv
    with open(args.csv, "r") as f:
        names = dict( (x[3], 0) for x in csv.reader(f) )

    # Compare names with history
    if Path(args.dir).is_dir():
        history = Path(args.dir).glob("*.txt")
        for file_name in history:
            with open(file_name, "r") as f:
                for name in f.readlines():
                    name = name.strip()
                    if names.get(name, None) is not None:
                        names[name] += 1

    # Sample size based on proportion
    sample_size = round( len(names) * args.proportion )

    # Prioritize lowest demo count first
    # Sorts by number of demos, random if equal
    sample = sorted(names.keys(), key=lambda x: (names[x], random.random()))[:sample_size]

    # Write to file
    Path(args.dir).mkdir(parents=True, exist_ok=True)
    file_name = datetime.today().strftime("%Y-%m-%d") + ".txt"
    with open(f"{args.dir}/{file_name}", "w") as f:
        for student in sample:
            print(f"Selected '{student}' (prev. demo {names[student]} times)")
            f.write(student + "\n")
    print(f"Created new demo list in {args.dir}/{file_name}.")
