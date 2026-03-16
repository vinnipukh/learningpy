import pandas as pd
import xml.etree.ElementTree as ET
import os

# DOSYA YOLUNU BURAYA YAPIŞTIR
xml_file = r'/cleaning_trsa/semeval2016-task5/trial data2/tu_restaurant_trial_sb2.xml'

tree = ET.parse(xml_file)
root = tree.getroot()
data = []

for review in root.findall('Review'):
    # 1. O yorumdaki tüm cümleleri birleştir (Metin bütünlüğü için)
    sentences_tag = review.find('sentences')
    full_text = ""
    if sentences_tag is not None:
        text_list = []
        for s in sentences_tag.findall('sentence'):
            t_el = s.find('text')
            if t_el is not None and t_el.text:
                text_list.append(t_el.text)
        full_text = " ".join(text_list)

    # 2. Review altındaki 'Opinions' kısmına bak
    opinions_tag = review.find('Opinions')
    if opinions_tag is not None:
        # DİKKAT: Senin XML'inde 'opinion' küçük harf olabilir, ikisini de kontrol ediyoruz
        # Eğer XML'de küçükse .findall('opinion'), büyükse .findall('Opinion') yapmalısın.
        for op in opinions_tag.findall('opinion'):
            data.append({
                'text': full_text,
                'category': op.get('category'),
                'polarity': op.get('polarity')
            })

df = pd.DataFrame(data)
df.to_csv('tu_restaurant_trial_sb2.csv', index=False, encoding='utf-8-sig')

print(f"İşlem bitti! Toplam {len(df)} satır veri çekildi.")