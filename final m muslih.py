# NAMA : M.MUSLIH
# NIM : D0221074

class Balok():
    def __init__(self,panjang,lebar,tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume (self):
        volume_balok = self.panjang * self.lebar * self.tinggi
        print("volume balok adalah : " , volume_balok)

    def luas (self):
        luas_balok = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang)
        print("luas balok adalah : ", luas_balok)

class Tabung():
    def __init__(self, jari, tinggi):
        self.jari = jari
        self.tinggi = tinggi

    def volume (self):
        volume_tabung = 22/7 * self.jari**2 * self.tinggi
        print("volume tabung adalah : " , round(volume_tabung,2))

    def luas (self):
        luas_tabung = 2 * 22/7 * self.jari * self.tinggi + 2 * 22/7 * self.jari**2
        print("luas tabung adalah : ", round(luas_tabung,2))

class LimasSegitiga():
    def __init__(self, alas, tinggiA, tinggi):
        self.alas = alas
        self.tinggiA = tinggiA
        self.tinggi = tinggi

    def volume (self):
        volume_limasSegitiga = 1/3 * 1/2 * self.alas * self.tinggiA * self.tinggi
        print("volume limas segitiga adalah : " , round(volume_limasSegitiga,2))

    def luas (self):
        luas_limasSegitiga = 1/2 * self.alas * self.tinggiA + ( 3 * 1/2 * self.alas * self.tinggiA)
        print("luas limas segitiga adalah : ", round(luas_limasSegitiga,2))
        

    
while True:
    print() 
    print("""plihan menu
        1. Balok,  
        2. Tabung, 
        3. Limas Segitiga, 
        4. Berhenti""")

        
    pilihan = input('masukan pilihan menu : ')
    
    if pilihan == '1':
        p = float(input("masukkan panjang: "))
        l = float(input("masukkan lebar: "))
        t = float(input("masukkan tinggi: "))
        balok = Balok(p,l,t)
        print()
        balok.volume()
        balok.luas()
        
        
    
    elif pilihan == '2':
        j = float(input("masukkan jari: "))
        t = float(input("masukkan tinggi: "))
        tabung = Tabung (j,t)
        print()
        tabung.volume()
        tabung.luas()
        
    elif pilihan == '3':
        a = float(input("masukkan alas: "))
        tA = float(input("masukkan tinggi alas: "))
        t = float(input("masukkan tinggi: "))
        limasSegitiga = LimasSegitiga (a,tA,t)
        print()
        limasSegitiga.volume()
        limasSegitiga.luas()
    
    elif pilihan == '4':
        break
    
    else:
        print('pilihan kosong')
       
    
    
    
        