import pandas as pd

# Dosyaları yükle
df1 = pd.read_csv('C:\\Users\\arhan\\PycharmProjects\\learningpy\\cleaning_trsa\\semeval2016-task5\\clean_csvs\\TU_REST_SB1_TEST.csv')
df2 = pd.read_csv('C:\\Users\\arhan\\PycharmProjects\\learningpy\\cleaning_trsa\\semeval2016-task5\\test data gold annotations\\TU_REST_SB1_TEST.csv')

# İki dataframe arasındaki ortak satırları bul (Inner Join mantığıyla)
ortak_satirlar = pd.merge(df1, df2, how='inner')

if ortak_satirlar.empty:
    print("İki dosya arasında tamamen aynı olan bir satır bulunamadı. (Veri temiz!)")
else:
    print(f"Toplam {len(ortak_satirlar)} adet ortak satır bulundu.")
    print(ortak_satirlar)