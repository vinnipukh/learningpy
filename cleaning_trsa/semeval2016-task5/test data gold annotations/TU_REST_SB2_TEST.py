import xml.etree.ElementTree as ET
import json


def convert_test_xml_to_json(xml_file_path, output_json_path):
    try:
        # XML'i dosyadan oku
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        json_output = []

        for review in root.findall('Review'):
            rid = review.get('rid')

            # --- TEXT EKLEME KISMI ---
            # Review içindeki tüm cümlelerin textlerini bul ve birleştir
            sentences = [s.find('text').text for s in review.findall('.//sentence') if s.find('text') is not None]
            full_text = " ".join(sentences)

            triplets = []

            # Review tag'inin hemen altındaki Opinions bloğuna bakıyoruz
            opinions_block = review.find('Opinions')

            if opinions_block is not None:
                for opinion in opinions_block.findall('Opinion'):
                    # Target bu XML'de yok, o yüzden boş string ("") bırakıyoruz
                    # Eğer diğer JSON ile eşleşsin istersen burayı "NULL" da yapabilirsin
                    triplets.append({
                        "target": "",
                        "category": opinion.get('category'),
                        "polarity": opinion.get('polarity')
                    })

            json_output.append({
                "rid": rid,
                "text": full_text,  # Metin artık burada
                "triplets": triplets
            })

        # JSON olarak kaydet
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=4, ensure_ascii=False)

        print(f"Test seti (text dahil) başarıyla dönüştürüldü: {output_json_path}")

    except Exception as e:
        print(f"Hata oluştu: {e}")


# --- AYARLAR ---
xml_yolu = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\test data gold annotations\TU_REST_SB2_TEST.xml'
cikti_yolu = 'ali_erkan_test.json'

convert_test_xml_to_json(xml_yolu, cikti_yolu)