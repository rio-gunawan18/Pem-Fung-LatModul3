def convert_to_minutes(data):
    result = []
    for item in data:
        # Membagi string menjadi bagian-bagian yang berisi minggu, hari, jam, dan menit
        parts = item.split()
        weeks = int(parts[0]) * 7 * 24 * 60
        days = int(parts[2]) * 24 * 60
        hours = int(parts[4]) * 60
        minutes = int(parts[6])
        total_minutes = weeks + days + hours + minutes
        result.append(total_minutes)
    return result

data = ["3 minggu 3 hari 7 jam 21 menit", "5 minggu 5 hari 8 jam 11 menit", "7 minggu 1 hari 5 jam 33 menit"]
OutputData = convert_to_minutes(data)
print(OutputData)
