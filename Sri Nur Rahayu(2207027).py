kalimat = "ini adalah kalimat"
paragraf = """ini adalah paragraf.
paragraf terdiri dari beberapa baris."""
print (kalimat)
print (paragraf)
#ini adalah kalimat
#ini adalah paragraf.
#paragraf terdiri dari beberapa baris.


kalimat = "abcdefghijklmnopqrstuvwxyz"
print (kalimat [:5])
print (kalimat [5:10])
print (kalimat [21:])
print (kalimat [-10:-1])
print (kalimat [-10:])
#abcde
#fghij
#vwxyz
#qrstuvwxy
#qrstuvwxyz


kalimat = "Halo, semua. saya adalah progremer python. "
print (kalimat.upper())
print (kalimat.lower())
print (kalimat.capitalize())
print (kalimat.title())
print (kalimat.swapcase())
print (kalimat.replace("python", "java"))
print (kalimat.replace("a", "i"))
print (kalimat.strip())
print (kalimat.split('.'))
#HALO, SEMUA. SAYA ADALAH PROGREMER PYTHON. 
#halo, semua. saya adalah progremer python.
#Halo, semua. saya adalah progremer python.
#Halo, Semua. Saya Adalah Progremer Python.
#hALO, SEMUA. SAYA ADALAH PROGREMER PYTHON.
#Halo, semua. saya adalah progremer java.
#Hilo, semui. siyi idilih progremer python.
#Halo, semua. saya adalah progremer python.
#['Halo, semua', ' saya adalah progremer python', ' ']


kalimat = "Halo, semua. saya adalah progremer python. "
tambahan = "saya sedang belajar python. Mohon bimbingannya."
print (kalimat + tambahan)
#Halo, semua. saya adalah progremer python. saya sedang belajar python. Mohon bimbingannya.


kalimat = "Halo, semua. saya adalah progremer \"python\". "
tambahan = "saya sedang belajar python. Mohon bimbingannya."
print (kalimat + tambahan)
#Halo, semua. saya adalah progremer "python". saya sedang belajar python. Mohon bimbingannya.


umur = 21
rumah = 3
mobil = 5
emas = 10
kalimat = "saya berumur {} tahun, rumah saya ada {}, mobil saya ada {}, dan emas saya ada {} kilogram"
print(kalimat.format(umur, rumah, mobil, emas))
#saya berumur 21 tahun, rumah saya ada 3, mobil saya ada 5, dan emas saya ada 10 kilogram
