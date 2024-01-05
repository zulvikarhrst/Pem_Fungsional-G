random_list = [105, 3.1, "Hello", 737, "python", 2.7, "World", 412, 5.5, "AI"]

int_dict = {"satuan": [], "puluhan": [], "ratusan": []}
float_tuple = ()
string_list = []

for item in random_list:
    if isinstance(item, int):
        # Pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        int_dict["satuan"].append(satuan)
        int_dict["puluhan"].append(puluhan)
        int_dict["ratusan"].append(ratusan)
    elif isinstance(item, float):
        # Data float disimpan dalam bentuk tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Data string disimpan dalam list
        string_list.append(item)

print("Data integer dalam bentuk dictionary:")
print(int_dict)
print("Data float dalam bentuk tuple:")
print(float_tuple)
print("Data string dalam bentuk list:")
print(string_list)