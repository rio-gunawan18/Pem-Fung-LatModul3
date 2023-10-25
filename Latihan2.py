data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]

int_values = [list(filter(str.isdigit, entry.split())) for entry in data]

formatted_output = []
for entry in int_values:
    formatted_output.append(entry[:4])

for entry in formatted_output:
    print(entry)
