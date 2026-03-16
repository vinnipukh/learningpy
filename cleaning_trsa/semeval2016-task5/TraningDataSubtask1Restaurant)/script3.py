import pandas as pd
import xml.etree.ElementTree as ET
import os

# DOSYA YOLUNU BURAYA YAPIŞTIR
xml_file = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\TraningDataSubtask1Restaurant)\restaurant_tain_text_level_final.xml'

if not os.path.exists(xml_file):
    print(f"HATA: Dosya bulunamadı: {xml_file}")
else:
    tree = ET.parse(xml_file)
    root = tree.getroot()
    data = []

    for review in root.findall('Review'):
        rid = review.get('rid')

        # 1. Adım: Review içindeki tüm cümleleri tek bir metin olarak birleştir
        sentences_tag = review.find('sentences')
        full_text = ""
        if sentences_tag is not None:
            text_list = []
            for s in sentences_tag.findall('sentence'):
                t_el = s.find('text')
                if t_el is not None and t_el.text:
                    text_list.append(t_el.text)
            full_text = " ".join(text_list)

        # 2. Adım: Review'ın en altındaki asıl Opinion'ları al
        opinions_tag = review.find('Opinions')
        if opinions_tag is not None:
            for op in opinions_tag.findall('Opinion'):
                data.append({
                    'review_id': rid,
                    'text': full_text,
                    'category': op.get('category'),
                    'polarity': op.get('polarity')
                })

    # DataFrame oluştur ve kaydet
    df = pd.DataFrame(data)
    output_name = 'restaurant_tain_text_level_final.csv'
    df.to_csv(output_name, index=False, encoding='utf-8-sig')

    print(f"İşlem tamam! {len(df)} satırlık veri '{output_name}' dosyasına kaydedildi.")
    print(df.head())