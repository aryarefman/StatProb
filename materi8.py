# latihan perhitungan sederhana

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukkan suhu dalam celcius: "))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("suhu dalam reamur adalah", reamur, "Reamaur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("suhu dalam fahrenheit adalah", fahrenheit, "Fahrenheit")

# Kelvin
kelvin = celcius + 273
print("suhu dalam kelvin adalah", kelvin, 'Kelvin')

print("\n")

# Fahrenheit ke Kelvin
print("--Konversi fahrenheit ke kelvin--")
fahrenheit = float(input("Masukkan suhu dalam fahrenheit "))
fahrenheit_to_kelvin = ((5/9)*(fahrenheit-32)) + 273
print("konversi fahrenheit ke kelvin =", fahrenheit_to_kelvin, "Kelvin")

print("\n")

# Kelvin ke Fahrenheit
print("--Konversi kelvin ke fahrenheit--")
kelvin = float(input("Masukkan suhu dalam kelvin "))
kelvin_to_fahrenheit = ((9/5)*(kelvin-273)) + 32
print("konversi kelvin ke fahrenheit =", kelvin_to_fahrenheit, "Fahrenheit")