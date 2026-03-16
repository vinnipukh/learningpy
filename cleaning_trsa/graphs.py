import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Temizlenmiş final dosyanı oku
df = pd.read_csv(r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\merged_semeval.csv')

# NaN metin kalmışsa diye son bir güvenlik önlemi
df = df.dropna(subset=['text'])



# Metin uzunluklarını hesapla (Karakter sayısına göre)
df['text_length'] = df['text'].astype(str).apply(len)
ortalama_uzunluk = df['text_length'].mean()

# Grafikler için Seaborn temasını ayarla
sns.set_theme(style="whitegrid")

# Yan yana 3 grafiklik bir tuval (figure) oluşturuyoruz
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# 1. Grafik: Polarity Dağılımı (Bar Chart)
sns.countplot(data=df, x='polarity', ax=axes[0], palette='Set2')
axes[0].set_title('Polarity (Duygu) Dağılımı')
axes[0].set_ylabel('Yorum Sayısı')
axes[0].set_xlabel('Duygu')

# 2. Grafik: En Fazla Geçen Kategoriler
# Çok kategori varsa karmaşık durmasın diye en çoktan aza doğru sıralıyoruz
kategori_siralamasi = df['category'].value_counts().index
sns.countplot(data=df, y='category', order=kategori_siralamasi, ax=axes[1], palette='viridis')
axes[1].set_title('Kategori Dağılımı')
axes[1].set_xlabel('Yorum Sayısı')
axes[1].set_ylabel('Kategori')

# 3. Grafik: Metin Uzunluğu Dağılımı (Histogram)
sns.histplot(data=df, x='text_length', bins=30, kde=True, ax=axes[2], color='coral')
# Ortalama uzunluğu gösteren dikey bir kırmızı çizgi ekleyelim
axes[2].axvline(ortalama_uzunluk, color='red', linestyle='--', label=f'Ortalama: {ortalama_uzunluk:.1f} karakter')
axes[2].set_title('Metin Uzunluğu Dağılımı')
axes[2].set_xlabel('Karakter Sayısı')
axes[2].set_ylabel('Frekans')
axes[2].legend()

# Grafikleri ekranda göster
plt.tight_layout()
plt.show()

print(f"Genel Ortalama Metin Uzunluğu: {ortalama_uzunluk:.2f} karakter.")

null_target_satirlari = df[df['target'].isna() | (df['target'] == 'null')]
print(f"Toplam target'ı null/NaN olan satır sayısı: {len(null_target_satirlari)}")
print(null_target_satirlari)
print("null sum: ")
print(df.isnull().sum)