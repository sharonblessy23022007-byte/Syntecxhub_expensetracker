import csv

def export_to_csv(transactions, filename):

    with open(filename, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Date", "Category", "Amount", "Type"]
        )

        for row in transactions:
            writer.writerow(row)

    print(f"\n✓ Exported to {filename}")