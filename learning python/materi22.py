# latihan percabangan - kalkulator sederhana

print(20 * "=")
print("Kalkulator Sederhana")
print(20 * "=" + "\n")

angka_1 = float(input("Masukkan angka 1 = "))
operator = input("Masukkan operator (+,-,*,/) = ")
angka_2 = float(input("Masukkan angka 2 = "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")
elif operator == "-":
    hasil = angka_1 - angka_2
    print(f"{angka_1} - {angka_2} = {hasil}")
elif operator == "*":
    hasil = angka_1 * angka_2
    print(f"{angka_1} * {angka_2} = {hasil}")
elif operator == "/":
    hasil = angka_1 / angka_2
    print(f"{angka_1} / {angka_2} = {hasil}")
else:
    print("Operator yang anda masukkan salah!")

print("Akhir dari program, terima kasih!")