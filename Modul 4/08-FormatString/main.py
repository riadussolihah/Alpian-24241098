# format string

"""
    String : kumpulan dari karakter
    cara membuat string :
    1. dengan single qoute *...*
    2. dengan double qoute "..."
"""
# membuat sting dengan single qoute
nama = 'nama saya Azraqif'
print(nama)

# memebuat string dengan double qoute
nama = "nama saya Aznaqii"
print(nama)

print("nama saya ma'ruf ")
print("jangan lupa shalat jum'at ")

# maksa harus single qoute
# pakai tanda \ 
print('g\'day')
print('what\'sUpi')

print('C:\\user\\adam')

nama = "adam"
print("selamat datang",nama)

# fotmat string
format_str = f'selamat datang(nama)'
print(format_str)

# format string angka
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'jutaan = {angka:,}'
print(format_str)

#bilangan desimal
angka = 2005.54321
format_str = f'desimal = {angka:.3f}'
print(format_str)

# persen
angka = 0.55 # 0,55 * 100 = 55%
format_str = f'persen = {angka:.1%}'
print(format_str)

# melakukan operasi aritmatika dengan format string
harga = 57250
jumlah = 3

print(f'total bayar :  {harga*jumlah:,}')