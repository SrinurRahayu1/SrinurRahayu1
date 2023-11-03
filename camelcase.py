def camel_case(input_text):
    words = input_text.split()
    camel_case_text = '  '.join([word.capitalize() for word in words])
    return camel_case_text

# Input teks biasa
normal_text = "ini adalah contoh teks biasa"

# Memanggil fungsi camel_case
camel_case_result = camel_case(normal_text)

# Menampilkan hasil
print(f" {normal_text}")
print(f" {camel_case_result}")

# Input teks biasa
normal_text = "ini adalah contoh teks camelcase"

# Memanggil fungsi camel_case
camel_case_result = camel_case(normal_text)

# Menampilkan hasil
print(f" {camel_case_result}")
print(f" {normal_text}")

#hasil
ini adalah contoh teks biasa
Ini  Adalah  Contoh  Teks  Biasa
Ini  Adalah  Contoh  Teks  Camelcase
ini adalah contoh teks camelcase
