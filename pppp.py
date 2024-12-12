from html.parser import endtagfind

print('Halo! Selamat datang ke kalkulator luas bentuk! (Harap Jangan Memakai ".")')
nama = str(input('Masukkan Nama Anda:'))
while (nama == ''):
    print('Tolong Masukan Nama Anda!')
    nama = input('Masukkan Nama Anda:')

print('Halo', nama)
print('Jangan Memakai Space Saat Memilih Bentuk!')
print('')
print('1. Persegi (1)')
print('2. Segitiga (2)')
print('3. Persegi Panjang (3)')
print('4. Kubus (4)')
print('5. Trapesium (5)')
print('6. Tidak ada dalam list! (6)')
htng = input('Pilih Bentuk yang terdaftar! - ("End" untuk mematikan program!):')

if htng == 'End':
    print("Terimakasih Sudah Mencoba Kalkulator Kami")

while htng != '1' and htng != '2' and htng != '3' and htng != '4' and htng != '5' and htng != '6' and htng != 'End':
    print('ERROR! Invalid Data. Mohon Masukkan opsi yang di pilih! (1,2,3,4,5,6)')
    htng = input('Pilih segi yang terdaftar! - ("End" untuk mematikan program!):')
print('')


if htng == '1':
    print('')
    ko = int(input('Masukkan Panjang Persegi!:'))
    lo = int(input('Masukkan Lebar Persegi!:'))
    hit = ko*lo
    print(hit)
    print('Restart program untuk memakai ulang kalkulator luas bentuk!')

if htng == '2':
    print('')
    poa = int(input('Masukkan Panjang Alas Segitiga!:'))
    asdo = int(input('Masukkan Panjang Tinggi Segitiga!:'))
    asda = poa * asdo / 2
    print(asda)
    print('Restart program untuk memakai ulang kalkulator luas bentuk!')

if htng == '3':
    print('')
    k = int(input('Masukkan Panjang Persegi!:'))
    l = int(input('Masukkan Lebar Persegi!:'))
    hi = k * l
    print(hi)
    print('Restart program untuk memakai ulang kalkulator luas bentuk!')

if htng == "4":
    pjg = int(input("Masukkan Panjang Kubus:"))
    luas = int(input("Masukkan Luas Kubus: "))
    lebar = int(input("Masukkan Lebar Kubus: "))
    volume = pjg * luas * lebar
    print(volume)
    print('Restart program untuk memakai ulang kalkulator luas bentuk!')

if htng == '6':
    print('Maaf, Bentuk yang anda cari belum/tidak terdaftar pada data! Tunggu update selanjutnya!')

if htng == '5':
    kor = int(input('Masukkan A Trapesium!:'))
    kr = int(input('Masukkan B Trapesium!:'))
    rk = int(input('Masukkan Tinggi Trapesium!:'))
    pk = kor*kr
    hk = pk/2
    mk = hk*rk
    print('Area sama dengan:', mk)

