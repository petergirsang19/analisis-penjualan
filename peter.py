import pandas as pd
import matplotlib.pyplot as plt

# Data Penjualan
data_penjualan = pd.DataFrame({
    'Tanggal': ['2023-01-15', '2023-01-15', '2023-01-16', '2023-02-10', '2023-02-12', '2023-03-05', '2023-03-15', '2023-04-01', '2023-04-15'],
    'ID_Transaksi': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009],
    'ID_Produk': ['P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008', 'P009'],
    'Nama_Produk': ['Laptop A', 'Kemeja B', 'Snack C', 'TV D', 'Jeans E', 'Roti F', 'Smartphone G', 'Kemeja H', 'Blender I'],
    'Kategori_Produk': ['Elektronik', 'Pakaian', 'Makanan', 'Elektronik', 'Pakaian', 'Makanan', 'Elektronik', 'Pakaian', 'Elektronik'],
    'Harga_Satuan': [7000000, 200000, 10000, 5500000, 400000, 15000, 3500000, 250000, 700000],
    'Jumlah_Terjual': [2, 5, 50, 1, 3, 20, 3, 4, 6],
    'ID_Toko': ['T01', 'T01', 'T02', 'T03', 'T04', 'T05', 'T01', 'T02', 'T03'],
    'Kota': ['Jakarta', 'Jakarta', 'Bandung', 'Surabaya', 'Yogyakarta', 'Jakarta', 'Jakarta', 'Bandung', 'Surabaya'],
    'Metode_Pembayaran': ['Kartu Kredit', 'Tunai', 'E-Wallet', 'Kartu Debit', 'Kartu Kredit', 'Tunai', 'E-Wallet', 'Kartu Kredit', 'Tunai']
})

# Total Pendapatan dari Penjualan "Blender I"
blender_i_penjualan = data_penjualan[data_penjualan['Nama_Produk'] == 'Blender I']
total_pendapatan_blender_i = blender_i_penjualan['Harga_Satuan'] * blender_i_penjualan['Jumlah_Terjual']

# Perbandingan Pendapatan Produk Elektronik
produk_elektronik = data_penjualan[data_penjualan['Kategori_Produk'] == 'Elektronik']
produk_elektronik['Total_Pendapatan'] = produk_elektronik['Harga_Satuan'] * produk_elektronik['Jumlah_Terjual']

# Tren Penjualan Bulanan
data_penjualan['Tanggal'] = pd.to_datetime(data_penjualan['Tanggal'])
data_penjualan['Bulan'] = data_penjualan['Tanggal'].dt.to_period('M')
tren_penjualan_bulanan = data_penjualan.groupby('Bulan')['Harga_Satuan'].sum()

# Distribusi Metode Pembayaran April 2023
april_data = data_penjualan[data_penjualan['Tanggal'].dt.month == 4]
distribusi_metode_pembayaran = april_data.groupby('Metode_Pembayaran')['Harga_Satuan'].sum()

# Plotting the graphs with different colors
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Plot 1: Total Pendapatan Blender I
axes[0, 0].bar(blender_i_penjualan['Nama_Produk'], total_pendapatan_blender_i, color='skyblue')
axes[0, 0].set_title('Total Pendapatan Blender I')
axes[0, 0].set_ylabel('Total Pendapatan (Rp)')

# Plot 2: Perbandingan Pendapatan Produk Elektronik
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
axes[0, 1].bar(produk_elektronik['Nama_Produk'], produk_elektronik['Total_Pendapatan'], color=colors)
axes[0, 1].set_title('Perbandingan Pendapatan Produk Elektronik')
axes[0, 1].set_ylabel('Total Pendapatan (Rp)')

# Plot 3: Tren Penjualan Bulanan
axes[1, 0].plot(tren_penjualan_bulanan.index.astype(str), tren_penjualan_bulanan, color='purple', marker='o')
axes[1, 0].set_title('Tren Penjualan Bulanan')
axes[1, 0].set_ylabel('Total Penjualan (Rp)')

# Plot 4: Distribusi Metode Pembayaran April 2023
axes[1, 1].bar(distribusi_metode_pembayaran.index, distribusi_metode_pembayaran, color=['orange', 'green', 'blue', 'red'])
axes[1, 1].set_title('Distribusi Metode Pembayaran April 2023')
axes[1, 1].set_ylabel('Total Penjualan (Rp)')

plt.tight_layout()
plt.show()
