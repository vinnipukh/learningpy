import pandas as pd

# 1. Dosyayı oku
file_path = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\sitedekiler.csv'
df = pd.read_csv(file_path)

print(f"Temizlik öncesi satır sayısı: {len(df)}")

# 2. Gerçek boşlukları (NaN) temizle
df = df.dropna(subset=['text'])

# 3. İçinde metin olarak 'null' yazanları temizle
# (Bazı scriptlerde boş kalan yerlere 'null' yazdırmıştık, onları da uçuralım)
df = df[df['text'] != 'null']

# 4. İndeksi sıfırla (Satır numaraları 0, 1, 2... diye düzgün gitsin)
df = df.reset_index(drop=True)

# 5. Temizlenmiş halini kaydet
df.to_csv('final_temiz_veriler.csv', index=False, encoding='utf-8-sig')

print(f"Temizlik sonrası satır sayısı: {len(df)}")
print(f"Toplam {2830 - len(df)} (veya kaçsa) adet boş satır çöpe atıldı!")