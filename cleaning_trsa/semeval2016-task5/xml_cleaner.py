import pandas as pd
import xml.etree.ElementTree as ET

# Kendi bilgisayarındaki tam yolu buraya yapıştır
xml_file = r'/cleaning_trsa/semeval2016-task5/trial data2/tu_restaurant_trial_sb2.xml'

tree = ET.parse(xml_file)
root = tree.getroot()
data = []

for review in root.findall('Review'):
    sentences = review.find('sentences')
    if sentences is not None:
        for sentence in sentences.findall('sentence'):
            text_el = sentence.find('text')
            text = text_el.text if text_el is not None else ""

            opinions = sentence.find('Opinions')
            if opinions is not None:
                for op in opinions.findall('Opinion'):
                    data.append({
                        'text': text,
                        'target': op.get('target') if op.get('target') else "",
                        'category': op.get('category'),
                        'polarity': op.get('polarity')
                    })

df = pd.DataFrame(data)
df.to_csv('TU_REST_SB1_TEST.csv', index=False, encoding='utf-8-sig')
print(f"İşlem tamam! {len(df)} satır oluşturuldu.")


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