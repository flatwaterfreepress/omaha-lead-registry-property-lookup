import csv
import json

# Input and output file names
csv_file = "data/lead.csv"
json_file = "data/lead.json"

def csv_to_json(csv_file, json_file):
	data = []

	with open(csv_file, newline='', encoding="utf-8") as f:
		reader = csv.DictReader(f)
		for row in reader:
			# Normalize keys (strip spaces, lowercase, replace spaces with underscores)
			clean_row = {k.strip().lower().replace(" ", "_"): v.strip() for k, v in row.items()}
			data.append(clean_row)

	with open(json_file, "w", encoding="utf-8") as f:
		json.dump(data, f, indent=2, ensure_ascii=False)

	print(f"✅ Converted {len(data)} rows from {csv_file} → {json_file}")

if __name__ == "__main__":
	csv_to_json(csv_file, json_file)
