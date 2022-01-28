import pandas as pd
import csv

# CSV file
F = "covid-vaccination-brazil.csv"

# Number of vaccinations
N = 2000000

# Read CSV with pandas
data = pd.read_csv(F, delimiter=";")

# Loop index
index = 0
# Output columns
header = ["date", "daily_vaccinations", "total_vaccinations"]

# Write output file
with open("out.csv", "w", encoding="utf-8", newline="") as output:
    for i in range(0, data.shape[0]):
        row = data.iloc[i]
        if row[1] > N:
            # CSV writer
            writer = csv.writer(output)
            # Previous value
            pval = data.iloc[i - 1][1]
            # Loop index
            index += 1
            if index == 1:
                # Write header
                writer.writerow(header)

            # Split date variable   
            split_date = row[0].split("-")
            # Format date to "dd/mm/yyyy"
            format_date = f"{split_date[2]}/{split_date[1]}/{split_date[0]}"

            # Calculate daily vacinations
            daily = row[1] - pval
            writer.writerow([format_date, daily, row[1]])
