# latihan date and time
# cari : library python

import datetime as dt

# .date.today()
hari_ini = dt.date.today()
print(hari_ini)
print(f"Hari ini adalah hari = {hari_ini:%A}")

# .date()
tanggal = dt.date(2005, 4, 4)
print(tanggal)
print(f"Hari lahir saya adalah hari = {tanggal:%A}")

# latihan
print("Silahkan masukkan tanggal, bulan, dan tahun lahir anda")
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"tanggal lahir anda adalah = {tanggal_lahir}")

hari_ini = dt.date.today()
print(f"hari ini tanggal : {hari_ini}")
jumlah_hari = hari_ini - tanggal_lahir
umur_tahun = jumlah_hari.days // 365 # .days -> agar kata 'days' yang ada di console tidak ada
umur_bulan = (jumlah_hari.days % 365) // 30 # harus pakai .days agar tidak error
umur_hari = (jumlah_hari.days % 365) % 30
print(f"Harinya adalah : {tanggal_lahir:%A}")
print(f"Umur anda adalah : {umur_tahun} tahun {umur_bulan} bulan {umur_hari} hari")