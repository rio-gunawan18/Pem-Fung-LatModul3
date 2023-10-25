# Data list
data_list = [3.1, 2.7, 5.5, 107, 73, 41, "Hello", "Python", "world", "AI"]

# Filter untuk memisahkan nilai float, int, dan string
data_float = list(filter(lambda x: isinstance(x, float), data_list))
data_int = list(filter(lambda x: isinstance(x, int), data_list))
data_string = list(filter(lambda x: isinstance(x, str), data_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
def map_to_units(value):
    ratusan = value // 100
    puluhan = (value // 10) % 10
    satuan = value % 10
    return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}

data_int_mapped = list(map(map_to_units, data_int))

# Output
print("Data Float:", data_float)
print("Data Int:")
for item in data_int_mapped:
    print(item)
print("Data String:", data_string)