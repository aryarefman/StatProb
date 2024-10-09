# operasi dan manipulasi string (part 2)

# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case (.upper())
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case (.lower())
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case (.islower())
salam = "sist"
apakah_lower = salam.islower() # hasilnya bool
print(salam + " is Lower = " + str(apakah_lower))

# contoh untuk pengecekan upper case (.isUpper())
apakah_upper = salam.isupper()
print(salam + " is Upper = " + str(apakah_upper))

# .isalpha() <--- untuk mengecek semuanya huruf
# .isalnum() <--- untuk mengecek huruf dan angka
# .isdecimal() <--- untuk mengecek semuanya angka
# .isspace() <--- untuk mengecek string kosong(spasi, tab, newline)
# .istitle() <--- untuk mengecek semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasil bool
print(judul + " is title = " + str(cek_judul))

## ngecek komponen .startswith() .endswith() <--- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("start = " + str(cek_end))

## penggabungan komponen .join() .split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ', '.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = "akuehmsayangehmkamu"
print(gabungan.split('ehm'))

## alokasi karakter .rjust(), .ljust(), .center()
print(5 * "=" + "data" + "=" * 5)

kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(20, ":")
print("'" + tengah + "'")

# kebalikannya -> .strip()
tengah = tengah.strip(":") # menghilangkan tanda :
print("'" + tengah +"'")