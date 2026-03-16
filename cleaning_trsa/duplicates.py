import pandas as pd

# 1. İki dosyanın yolunu belirt
csv1_yolu = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\maildekiler.csv'
csv2_yolu = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\sitedekiler.csv'

# Dosyaları oku
df1 = pd.read_csv(csv1_yolu)
df2 = pd.read_csv(csv2_yolu)

print(f"1. Dosya satır sayısı: {len(df1)}")
print(f"2. Dosya satır sayısı: {len(df2)}")

# 2. Önce iki dosyayı alt alta dümdüz birleştir
birlesik_df = pd.concat([df1, df2], ignore_index=True)
print(f"Birleşme sonrası toplam satır: {len(birlesik_df)}")

# 3. Kopyaları (Duplicate) sil
# 'text', 'category' ve 'polarity' sütunlarının üçü birden aynıysa o satırın kopyasını siler.
benzersiz_df = birlesik_df.drop_duplicates(subset=['text', 'category', 'polarity'])

# Satır numaralarını düzelt
benzersiz_df = benzersiz_df.reset_index(drop=True)

# 4. Final dosyasını kaydet
benzersiz_df.to_csv('benzersiz_final_veriseti.csv', index=False, encoding='utf-8-sig')

print(f"Kopyalar silindikten sonra kalan benzersiz (unique) satır: {len(benzersiz_df)}")
print(f"Toplam {len(birlesik_df) - len(benzersiz_df)} adet kopya satır çöpe atıldı!")