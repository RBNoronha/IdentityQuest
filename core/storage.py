
import json
import csv

def save_results(results: dict, output_format: str = "json"):
    if output_format == "json":
        with open("data/results.json", "w") as f:
            json.dump(results, f, indent=2)
    elif output_format == "csv":
        with open("data/results.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["source", "result"])
            for k, v in results.items():
                writer.writerow([k, str(v)])
