import xml.etree.ElementTree as ET
import json


def xml_to_json_triplets(xml_path, json_output_path):
    try:
        # XML dosyasını parse et
        tree = ET.parse(xml_path)
        root = tree.getroot()

        all_reviews = []

        # Her bir <Review> elementini dön
        for review in root.findall('Review'):
            # --- TEXT EKLEME KISMI ---
            # Review içindeki tüm sentence'ların textlerini bul ve birleştir
            sentences = [s.find('text').text for s in review.findall('.//sentence') if s.find('text') is not None]
            full_text = " ".join(sentences)

            review_data = {
                "rid": review.get('rid'),
                "text": full_text,  # Metni buraya ekledik
                "triplets": []
            }

            # Review altındaki tüm Opinion tag'lerini bul
            for opinion in review.findall('.//Opinion'):
                target_val = opinion.get('target')

                # Senin if-else mantığın: target yoksa, boşsa veya "NULL" ise "NULL" yap
                triplet = {
                    "target": "NULL" if target_val in ["", "NULL", None] else target_val,
                    "category": opinion.get('category'),
                    "polarity": opinion.get('polarity')
                }
                review_data["triplets"].append(triplet)

            all_reviews.append(review_data)

        # JSON dosyasına yaz
        with open(json_output_path, 'w', encoding='utf-8') as f:
            json.dump(all_reviews, f, indent=4, ensure_ascii=False)

        print(f"Başarıyla dönüştürüldü ve textler eklendi: {json_output_path}")

    except ET.ParseError:
        print("Hata: XML dosyası bozuk veya tam kapanmamış (tag hatası).")
    except FileNotFoundError:
        print("Hata: Belirttiğin dosya yolu bulunamadı.")


# --- KULLANIM ---
dosya_yolu = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\ABSA_Semeval_Turkish\TU_REST_SB1\TU_REST_SB1_TEST.xml'
cikti_yolu = 'TU_REST_SB1_TEST.json'

xml_to_json_triplets(dosya_yolu, cikti_yolu)