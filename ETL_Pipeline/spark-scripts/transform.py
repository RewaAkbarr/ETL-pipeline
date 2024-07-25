import psycopg2
import pandas as pd

# Fungsi untuk koneksi ke database
def connect_to_db():
    return psycopg2.connect(
        dbname="postgres_db", 
        user="user", 
        password="password", 
        host="host.docker.internal", 
        port=5432
    )

# Fungsi untuk mengambil dan membersihkan data
def fetch_and_clean_data(conn):
    query = "SELECT * FROM penjualan"
    df = pd.read_sql(query, conn)
    # Hapus baris dengan data yang hilang
    df_cleaned = df.dropna()
    return df_cleaned

# Fungsi untuk menemukan produk terlaris setiap bulan
def find_top_products_each_month(df):
    df['tanggal'] = pd.to_datetime(df['tanggal'])
    df['year'] = df['tanggal'].dt.year
    df['month'] = df['tanggal'].dt.month
    df['jumlah_order'] = pd.to_numeric(df['jumlah_order'])
    # Kelompokkan data berdasarkan tahun, bulan, dan jenis_produk
    grouped = df.groupby(['year', 'month', 'jenis_produk'])['jumlah_order'].sum().reset_index()
    # Temukan produk terlaris setiap bulan
    top_products = grouped.sort_values('jumlah_order', ascending=False).drop_duplicates(['year', 'month'])
    return top_products[['year', 'month', 'jenis_produk', 'jumlah_order']]

# Fungsi untuk menyimpan hasil analisis ke dalam database
def save_results_to_db(conn, df):
    cur = conn.cursor()
    for _, row in df.iterrows():
        cur.execute(
            "INSERT INTO top_products_monthly (year, month, jenis_produk, total_sales) VALUES (%s, %s, %s, %s) ON CONFLICT (year, month, jenis_produk) DO UPDATE SET total_sales = EXCLUDED.total_sales",
            (row['year'], row['month'], row['jenis_produk'], row['jumlah_order'])
        )
    conn.commit()
    cur.close()

# Main script
if __name__ == "__main__":
    conn = connect_to_db()
    df_cleaned = fetch_and_clean_data(conn)
    top_products_monthly = find_top_products_each_month(df_cleaned)
    save_results_to_db(conn, top_products_monthly)
    conn.close()