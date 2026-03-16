import pandas as pd
import xml.etree.ElementTree as ET


# XML dosyasını oku
# Dosyanın tam yolunu tırnak içine yapıştır ve başına r harfi koy
xml_file = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\TraningDataSubtask1Restaurant)\reviews.xml'



tree = ET.parse(xml_file)
root = tree.getroot()

data = []

for review in root.findall('Review'):
    sentences = review.find('sentences')
    if sentences is not None:
        for sentence in sentences.findall('sentence'):
            # Metni çekiyoruz
            text_element = sentence.find('text')
            text = text_element.text if text_element is not None else ""

            # Opinions etiketini arıyoruz
            opinions = sentence.find('Opinions')

            # Eğer Opinions varsa (yani OutOfScope değilse ve yorum içeriyorsa)
            if opinions is not None:
                for op in opinions.findall('Opinion'):
                    data.append({
                        'text': text,
                        'target': op.get('target') if op.get('target') else "",
                        'category': op.get('category'),
                        'polarity': op.get('polarity')
                    })
            # Not: Eğer Opinions yoksa, bu cümle data listesine eklenmez (skips).

# DataFrame oluştur
df = pd.DataFrame(data)

# CSV'ye kaydet
df.to_csv('TU_REST_SB1_TEST.csv', index=False, encoding='utf-8-sig')

# Kontrol için ilk 5 satırı yazdır
print(f"İşlem tamam! Toplam {len(df)} adet opinion satırı oluşturuldu.")
print(df.head())

"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xml.etree.ElementTree as ET

xml_file = 'C:\\Users\\arhan\\PycharmProjects\\learningpy\\cleaning_trsa\\ABSA_Semeval_Turkish\\turkish_rest_sb1_train.xml'
tree = ET.parse(xml_file)
root = tree.getroot()

data = []

for review in root.findall('Review'):
    sentences = review.find('sentences')
    if sentences is not None:
        for sentence in sentences.findall('sentence'):
            text = sentence.find('text').text
            opinions = sentence.find('Opinions')

            if(opinions) is not None:
                for op in opinions.findall('Opinion'):
                    data.append({
                        'text': text,
                        'target': op.get('target'),
                        'category': op.get('category'),
                        'polarity': op.get('polarity'),

                    })
df = pd.DataFrame(data)
df.to_csv('turkish_rest_sb1_train.csv', index=False, encoding='utf-8-sig')

print(f"Toplam {len(df)} satır oluşturuldu.")

print(df.head())
"""