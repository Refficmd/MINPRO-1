
# menghitung harga dan jumlah barang
while True: # looping untuk menghitung harga barang

    harga_barang = float(input("masukkan harga barang: Rp. "))
    jumlah_barang = int(input("masukkan jumlah barang: "))

    #menghitung total harga barang
    total_harga_barang = harga_barang * jumlah_barang

#mengecek apakah total harga barang mencapai Rp.250000
    if total_harga_barang >= 250000:
        print("anda mendapatkan diskon sebesar 25%")
        Diskon_bonus= 0.25 * total_harga_barang
        total_harga_barang -= Diskon_bonus
        print("total harga barang setelah didiskon Rp.", total_harga_barang)
    else:
        print("Pembelanjaan anda kurang dari 250000, anda tidak mendapatkan diskon ", total_harga_barang)
    
    ulang = input("ingin menghitung ulang y/t: ")
    if ulang == "y":
        continue
    else: 
        print ("selamat tinggal, hati-hati dijalan :)")
        break






