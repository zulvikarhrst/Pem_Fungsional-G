# 1. Data tuple
data_tuple = ('Pensil', 1500, 'Buku', 5000, 'Penggaris', 2000)

# 2. Fungsi untuk memisahkan data
def separate_data(data_tuple):
    names = [data_tuple[i] for i in range(0, len(data_tuple), 2)]
    prices = [data_tuple[i] for i in range(1, len(data_tuple), 2)]
    return names, prices

# 3. Fungsi untuk membuat dictionary
def create_dictionary(names, prices):
    return dict(zip(names, prices))

# 4. Tampilkan hasil
print(f"1. {data_tuple}")
names_list, prices_list = separate_data(data_tuple)
print(f"2. {names_list} {prices_list}")
result_dict = create_dictionary(names_list, prices_list)
print(f"3. {result_dict}")