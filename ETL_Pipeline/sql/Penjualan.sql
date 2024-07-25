DROP TABLE IF EXISTS penjualan;
CREATE TABLE IF NOT EXISTS penjualan (
    tanggal DATE,
    jenis_produk VARCHAR(255),
    jumlah_order VARCHAR(50),
    harga VARCHAR(50), 
    total VARCHAR(50) 
);

CREATE TABLE IF NOT EXISTS top_products_monthly (
  year INT,
  month INT,
  jenis_produk VARCHAR(255),
  total_sales INT
);

ALTER TABLE top_products_monthly
ADD CONSTRAINT unique_year_month_product UNIQUE (year, month, jenis_produk);