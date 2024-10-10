# latihan komparasi dan logika

# membuat gabungan area rentang dari angka

# +++++3-----10+++++

inputUser = float(input("masukkan angka yang bernilai\nkurang dari 3 \natau \nlebih besar dari 10\n:"))

# +++++3-----
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Kurang dari 3 =", isKurangDari)

# -----10+++++
# memeriksa angka lebih dari 10
isLebihDari = (inputUser > 10)
print("Lebih dari 10 =", isLebihDari)

# +++++3-----10+++++
isCorrect = isKurangDari or isLebihDari
print("angka yang anda masukkan: ", isCorrect)

# -----3+++++10-----
# kasus irisan 
print("\n", 10 * "=", "\n")
inputUser = float(input("masukkan angka yang bernilai\nlebih dari 3 \ndan \nkurang dari 10\n:"))

# -----3+++++
# lebih dari 3
isLebihDari = (inputUser > 3)
print("Lebih dari 3 =", isLebihDari)

# +++++10-----
# kurang dari 10
isKurangDari = (inputUser < 10)
print("kurang dari 10 =", isKurangDari)

# -----3+++++10-----
isCorrect = isKurangDari and isLebihDari
print("angka yang anda masukkan: ", isCorrect)

print("\n", 10 * "=", "\n")
print("=====HOMEWORK=====")
input = float(input("silahkan masukkan angka:"))

# -----0+++++5-----8+++++11-----
print("\n", "soal 1")
soal01 = (input > 0 and input < 5) or (input > 8 and input < 11)
print("angka yang terletak diantara 0-5 dan diantara 8-11 =", soal01)

# +++++0-----5+++++8-----11++++
print("\n", "soal 2")
soal02 = (input < 0) or (input > 5 and input < 8) or (input > 11)
print("angka yang kurang dari 0, terletak diantara 5 dan 8, dan angka yang lebih besar dari 11 =", soal02)