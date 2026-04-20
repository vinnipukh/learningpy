import json


def merge_targets(test_json_path, reference_json_path, output_path):
    try:
        # 1. Referans JSON'u (Cevapları olan) yükle
        with open(reference_json_path, 'r', encoding='utf-8') as f:
            ref_data = json.load(f)

        # Hızlı arama için lookup table oluştur: (rid, category, polarity) -> target
        lookup_table = {}
        for review in ref_data:
            rid = review['rid']
            for triplet in review['triplets']:
                # Key oluştururken tuple kullanıyoruz (O(1) erişim hızı için)
                key = (rid, triplet['category'], triplet['polarity'])
                lookup_table[key] = triplet['target']

        # 2. Test JSON'u (Text içeren ama target'ları boş olan) yükle
        with open(test_json_path, 'r', encoding='utf-8') as f:
            test_data = json.load(f)

        match_count = 0
        missing_count = 0

        # 3. Test verisi içinde dön ve eşleşen target'ları yerleştir
        for review in test_data:
            rid = review['rid']
            # Dikkat: 'text' anahtarı review sözlüğünde duruyor, dokunmuyoruz.

            for triplet in review['triplets']:
                key = (rid, triplet['category'], triplet['polarity'])

                if key in lookup_table:
                    # Eşleşme varsa target'ı referans dosyadan alıyoruz
                    triplet['target'] = lookup_table[key]
                    match_count += 1
                else:
                    # Eşleşme yoksa target olduğu gibi (boş string) kalsın
                    missing_count += 1

        # 4. Sonucu yeni bir JSON olarak kaydet
        with open(output_path, 'w', encoding='utf-8') as f:
            # test_data değiştiği için içindeki text'lerle beraber kaydedilir
            json.dump(test_data, f, indent=4, ensure_ascii=False)

        print(f"--- İşlem Başarıyla Tamamlandı ---")
        print(f"Doldurulan (Eşleşen) Target Sayısı: {match_count}")
        print(f"Eşleşme Bulunamayan (Boş Kalan): {missing_count}")
        print(f"Çıktı Dosyası: {output_path}")

    except Exception as e:
        print(f"Bir hata oluştu kanka: {e}")


# --- KULLANIM ---
# Path'leri senin Pycharm projerine göre güncelledim
test_json = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\semeval2016-task5\test data gold annotations\ali_erkan_test.json'
referans_json = r'C:\Users\arhan\PycharmProjects\learningpy\cleaning_trsa\ABSA_Semeval_Turkish\TU_REST_SB1\TU_REST_SB1_TEST.json'
cikti_json = 'ali_erkan_test_native_turkish.json'

merge_targets(test_json, referans_json, cikti_json)