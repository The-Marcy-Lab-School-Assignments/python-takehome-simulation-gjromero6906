import csv

open_requests = 0
complaint_counts = {}
borough_counts = {}

with open('nyc_311_requests.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['resolution_status'] == 'Open':
            open_requests += 1

        complaint_type = row['complaint_type']
        complaint_counts[complaint_type] = complaint_counts.get(complaint_type, 0) + 1

        borough = row['borough']
        borough_counts[borough] = borough_counts.get(borough, 0) + 1

most_common_complaint = max(complaint_counts, key=complaint_counts.get)
most_common_count = complaint_counts[most_common_complaint]

borough_lines = []
for borough in sorted(borough_counts):
    borough_lines.append(f"- {borough}: {borough_counts[borough]}")

output_lines = [
    f"Open requests: {open_requests}",
    "",
    f"Most common complaint type: {most_common_complaint} ({most_common_count} requests)",
    "",
    "Requests per borough:",
    *borough_lines,
]

with open('output.txt', 'w') as f:
    f.write('\n'.join(output_lines) + '\n')

print("Output saved to output.txt")
