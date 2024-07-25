SET DateStyle = 'DMY';
COPY penjualan FROM '/data/data_baru.csv' DELIMITER AS ',' CSV HEADER;