import xml.etree.ElementTree as ET
import json
import os


def convert_xml_file_to_json(xml_file_path, output_json_path):
    try:
        # Dosyayı yoldan parse et
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        json_output = []

        for review in root.findall('Review'):
            rid = review.get('rid')
            triplets = []

            # Review altındaki tüm Opinion tag'lerini bul
            for opinion in review.findall('.//Opinion'):
                triplets.append({
                    "target": opinion.get('target'),
                    "category": opinion.get('category'),
                    "polarity": opinion.get('polarity')
                })

            json_output.append({
                "rid": rid,
                "triplets": triplets
            })

        # Sonucu JSON olarak kaydet
        with open(output_json_path, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=4, ensure_ascii=False)

        print(f"İşlem tamam! JSON dosyası oluşturuldu: {output_json_path}")

    except FileNotFoundError:
        print("Hata: Belirttiğin yolda dosya bulunamadı.")
    except ET.ParseError:
        print("Hata: XML dosyası bozuk veya eksik (tagler kapanmamış olabilir).")


# --- KULLANIM ---
# Windows dosya yolunu r"..." şeklinde yazmayı unutma
dosya_yolu = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\ABSA_Semeval_Turkish\turkish_rest_sb1_train.xml'
cikti_yolu = 'turkish_rest_sb1_train.json'

convert_xml_file_to_json(dosya_yolu, cikti_yolu)