import xml.etree.ElementTree as ET
import pandas as pd

# XML dosyanı yükle (dosya adını kendi dosyanla değiştir)
tree = ET.parse('TU_REST_SB2_TEST.xml')
root = tree.getroot()

data = []

for review in root.findall('Review'):
    # 1. DURUM: Cümle içi (Sentence-level) Opinion'ları topla
    sentences_node = review.find('sentences')
    if sentences_node is not None:
        for sentence in sentences_node.findall('sentence'):
            text_node = sentence.find('text')
            text = text_node.text if text_node is not None else ""

            opinions_node = sentence.find('Opinions')
            if opinions_node is not None:
                for opinion in opinions_node.findall('Opinion'):
                    target = opinion.get('target', 'NULL')  # Target yoksa NULL
                    category = opinion.get('category', '')
                    polarity = opinion.get('polarity', '')
                    data.append([text, target, category, polarity])

    # 2. DURUM: Yorum sonu (Review-level) Opinion'ları topla (Senin örneğindeki gibi)
    review_opinions = review.find('Opinions')
    if review_opinions is not None and len(review_opinions.findall('Opinion')) > 0:
        # Opinion yorumun genelindeyse, text olarak tüm cümleleri birleştiriyoruz
        all_sentences = [s.find('text').text for s in sentences_node.findall('sentence') if
                         s.find('text').text is not None]
        full_text = " ".join(all_sentences)

        for opinion in review_opinions.findall('Opinion'):
            target = opinion.get('target', 'NULL')
            category = opinion.get('category', '')
            polarity = opinion.get('polarity', '')
            data.append([full_text, target, category, polarity])

# DataFrame oluştur ve CSV'ye yaz
df = pd.DataFrame(data, columns=['text', 'target', 'category', 'polarity'])
df.to_csv('absa_hazir_veri.csv', index=False)

print("İşlem tamamlandı. absa_hazir_veri.csv dosyası oluşturuldu.")
print(df.head())