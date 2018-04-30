nama=[]
gaji=[]
mobil=[]
pajak=[]
pertahun=[]
perbulan=[]
pajakmobil=[]
print ('+-----------------------------------------------+')
print ('|     Program  Menghitung Pajak Penghasilan     |')
print ('|                  dan Mobil                    |')
print ('|                 Kelompok 4                    |')
print ('|    1. Eko pramono / 21120112140088            |')
print ('|    2. Dimas Putu Gumiwang  / 21120117120015   |')
print ('+-----------------------------------------------+')
print ('')
data=int(input('Masukan jumlah individu hitungan pajak : '))
print('==============================================')
 
for i in range(data):
    a = input('Masukan nama : ')
    nama.append(a)
    b = int(input('Masukan harga mobil : '))
    mobil.append(b)
    c = int(input('Berapa penghasilan/bulan : '))
    gaji.append(c)
    print('')

def gajisetaun():
    d = 12 * gaji[i]
    pertahun.append(d)

def pajakpertaun():
    e = 0.025 * pertahun[i]
    pajak.append(e)

def hargamobil():
    f = 0.020 * mobil[i]
    pajakmobil.append(f)

def pajakperbulan():
    g = pajak[i] / 12
    perbulan.append(g)
    
for i in range(data):
    gajisetaun()
    pajakpertaun()
    hargamobil()
    pajakperbulan()
 
