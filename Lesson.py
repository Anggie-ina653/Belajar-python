# LESSON - 01 #

print("Hello, world!")

#challenge

#=========================
#   MY FIRST WEBSITE
#=========================

print("Nama : Anggie")
print("Target : fullstack Developer")
print("Backend : Python")
print("framework : FastAPI")



# LESSON - 02 #

Nama = "Anggie"
print(Nama)

Umur = 23
print(Umur)

Kota_Asal = "Kota Bekasi"
print(Kota_Asal)

Bahasa = "Python"
print(Bahasa)

Framework = "FastAPI"
print(Framework)


# LESSON - 03 #

Nama = "Anggie"
print(type(Nama))

Umur = 23
print(type(Umur))

Kota_Asal = "Kota Bekasi"
print(type(Kota_Asal))

Bahasa = "Python"
print(type(Bahasa))

Framework = "FastAPI"
print(type(Framework))

Tinggi_Badan = 1.50
print(type(Tinggi_Badan))

Sedang_Belajar = True
print(type(Sedang_Belajar))


# LESSON - 04 #

print(f"Nama saya {Nama}.")
print(f"Umur saya {Umur} tahun.")
print(f"Dengan tinggi badan sekitar {Tinggi_Badan} meter.")
print(f"Apa saya sedang belajar Python? {Sedang_Belajar}.") #ini disebut f-string

print(f"""
          ======================
                MY PROFILE  
          ====================== 
          Nama        : {Nama}
          Umur        : {Umur}
          Asal        : {Kota_Asal}
          Belajar     : {Bahasa}
          Framework   : {Framework}
         .""")  #ini disebut multiline f-string/triple-quoted string



# LESSON - 05 #

#tantangan hitung total harga dengan variable + OPerator + F-string
harga  = 15000
jumlah = 3
total = harga * jumlah
print(total)

#tantangan penggunaan operator perbandingan
umur = 23
print(f"Apakah sudah dewasa? {umur >= 18}")

#hitung total konten
jumlah_video  = 15
jumlah_feed   = 20
total_konten = jumlah_feed + jumlah_video
print(f"Total Konten : {total_konten}")
print(f"Apakah konten lebih dari 30? {total_konten > 30}")

# LESSON - 06 #

nama  = "Anggie"
umur  = 15

print(f"Halo {nama}")
if umur >= 18:
    print("Kamu sudah dewasa")
else : 
    print ("Kamu belum dewasa")

jumlah_konten = 45
if jumlah_konten < 10:
    print("konten masih sedikit")
elif jumlah_konten <= 30:
     print("konten cukup banyak")
else :
     print("konten sudah banyak")

# Challenge 06 
umur = 16 
if umur < 13:
    print("Belum memenuhi syarat")
elif umur <= 17:
    print("Boleh dengan pengawasan orang tua")
else :
    print("Boleh membuat akun")

# LESSON - 07 #

#part 1
for i in range(10):
    print("Saya belajar fullstack python")

for i in range(3):
    print(i)

#part 2
for i in range(5):
    print(f"Percobaan ke-{i}")

#part 3
for i in range(100, 111):
    print(f"Percobaan ke-{i}")

for i in range(5):
    print(f"Konten ke- {i+1}")

# LESSON - 07 #

Bahasa = ["Python", "FastAPI", "HTML", "CSS", "JavaScript"]

for choose in Bahasa:
    print(choose)

# LESSON - 08 #

#Part 1
B = ["Python", "Javascript","PHP", "SQL"]
print(B[0])
print(B[1])
print(B[3])

#Part 2
dic = {
    "judul": "Belajar Python",
    "jenis": "Video",
    "platform": "Tiktok"
}
print(dic["judul"])
print(dic["jenis"])
print(dic["platform"])

print("#Part 3")
coba = {
    "nama": "Anggie",
    "umur": 23,
    "kota": "Bekasi"
}
for key, value in coba.items():
    print(key,":", value)

print("hai")
#final
konten = [
    {"judul": "Tutorial Python",
     "platform": "Tiktok",
     "jenis": "video"},

    {"judul": "Tips Editing",
      "platform": "instagram",
      "jenis": "Reels"},

    {"judul": "Portofolio IT",
     "platform": "instagram",
     "jenis": "feed"}
]
for ini in konten:
    print(f"{ini['judul']} - {ini['platform']} - {ini['jenis']}")

# LESSON - 09 #
def belajar_python():
    print("Aku sedang belajar Python untuk menjadi Fullstack Developer!")

belajar_python()
belajar_python()

def perkenalan(nama, kota):
    print(f"Nama saya {nama}, dari {kota}.")

perkenalan("Anggie", "Bekasi")
perkenalan("Budi", "Bandung")

# LESSON - 10 #
def kali(harga, jumlah):
    return harga * jumlah

hasil = kali(15000, 3)
print(hasil)

konten= [
    {"judul": "Tutorial Python", "jenis": "video"},
    {"judul": "Tips Editing", "jenis": "video"},
    {"judul": "Portofolio IT", "jenis": "feed"}
]

def hitung_konten(data):
    return len(data)

jumlah = hitung_konten(konten)

print(f"Jumlah konten: {jumlah}")

# LESSON - 11 #

konten = [
        {"judul": "Tutorial Python", "jenis": "video"},
        {"judul": "Tips Editing", "jenis": "video"},
        {"judul": "Portofolio IT", "jenis": "feed"},
        {"judul": "Belajar FastAPI", "jenis": "video"},
        {"judul": "Desain Profil", "jenis": "feed"}
]

def hitung_video(data):
    jumlah = 0

    for item in data:
        if item["jenis"] == "video":
            jumlah = jumlah + 1
    return jumlah

print (hitung_video(konten))

# LESSON - 12 #

def hitung_jenis(data, jenis_dicari):
    jumlah = 0

    for item in data:
        if item["jenis"] == jenis_dicari:
            jumlah = jumlah + 1
    return jumlah 

print(hitung_jenis(konten,"video"))
print(hitung_jenis(konten, "feed"))

# LESSON - 13 #

konten = [
    {"judul": "Tutorial Python", "jenis": "video"},
    {"judul": "Tips Editing", "jenis": "video"}
]

konten.append({
    "judul": "Portofolio IT",
    "jenis": "feed"
})
konten.append({
    "judul": "Belajar FastAPI",
    "jenis": "video"
})
konten.append({
    "judul": "Desain Feed Instagram",
    "jenis": "feed"
})
print(f"Terdapat {len(konten)} konten")

# Menampilkan judul dan jenis konten secara otomatis #
for item in konten:
    print(f"{item['judul']} - {item['jenis']}")

# LESSON - 14 #

# 1. .remove()
konten = [
    {"judul": "Tutorial Python", "jenis": "video"},
    {"judul": "Tips Editing", "jenis": "video"},
    {"judul": "Portofolio IT", "jenis": "feed"},
    {"judul": "Belajar FastAPI", "jenis": "video"}
]

konten.remove({
    "judul": "Tips Editing",
    "jenis": "video"
})
print(len(konten))

# 2. .pop()
konten.pop(0)
print(len(konten))

#Challenge#
konten = [
    {"judul": "Tutorial Python", "jenis": "video"},
    {"judul": "Tips Editing", "jenis": "video"},
    {"judul": "Portofolio IT", "jenis": "feed"},
    {"judul": "Belajar FastAPI", "jenis": "video"},
    {"judul": "Desain Feed Instagram", "jenis": "feed"}
]

# 1. .remove() ke Tips Editing
konten.remove({
    "judul": "Tips Editing",
    "jenis": "video"
})

# 2. .pop() ke index 0 
konten.pop(0)

#3. menampilkan seluruh konten for.
for item in konten:
    print(f"{item['judul']} - {item['jenis']}")

# 4. tampilkan jumlah konten dengan len()
print(f"Terdapat {len(konten)} konten")

# LESSON - 15 #
# challenge 

konten = [
    {"judul": "Tutorial Python", "jenis": "video"},
    {"judul": "Tips Editing", "jenis": "video"},
    {"judul": "Portofolio IT", "jenis": "feed"}
]

konten[1]["judul"] = "Tips Editing CapCut"
konten[2]["jenis"] = "video"

for item in konten:
    print(f"{item['judul']} - {item['jenis']}")

# LESSON - 16 (Program CRUD sederhana) #

konten = [
    {"judul": "Tutorial Python", "jenis": "video"}, 
    {"judul": "Tips Editing", "jenis": "video"}
]

def tampilkan_konten():
    print("Daftar Konten: ")

    for item in konten:
        print(f"{item['judul']} - {item['jenis']}")

def tambah_konten(judul, jenis):
    konten.append({
        "judul": judul,
        "jenis": jenis
    })

tambah_konten("Belajar FastAPI", "video")
tambah_konten("Tutor Web Laravel", "feed")

tampilkan_konten()

# LESSON - 17 (Validasi Data dan Mencegah Duplikasi) #

konten = [
    {"judul": "Tutorial Python", "jenis": "video"},
    {"judul": "Tips Editing", "jenis": "video"}
]

def tambah_konten(judul, jenis):

    for item in konten:
        if item["judul"] == judul:
            print("Konten sudah ada!")
            return

    konten.append(
        {"judul": judul, "jenis": jenis })
    print("Konten berhasil ditambahkan!")

def tampilkan_konten():
    print("\nDaftar Konten: ")

    for item in konten:
        print(f"{item['judul']} - {item['jenis']}")

tambah_konten("Tutorial Python", "video")
tambah_konten("Belajar SQL", "video")

tampilkan_konten()

# Challenge #

tambah_konten("Tutorial Python", "video")
tambah_konten("Tutorial Python", "Feed")
tambah_konten("Belajar FastAPI", "video")

tampilkan_konten()
print(len(konten))