# mengambil input data dari user

# data yang dimasukkan pasti string
data = input("Masukkan data: ")
print("data = ", data, "type = ", type(data))

# jika kita ingin mengambil int dan float, maka
angka = int(input("Masukkan angka bulat: "))
print("data = ", angka, "type = ", type(angka))

angka = float(input("Masukkan angka desimal: "))
print("data = ", angka, "type = ", type(angka))

# bagaimana dengan boolean
biner = bool(int(input("Masukkan nilai boolean: ")))
print("data = ", biner, "type = ", type(biner))