import json
import pandas as pd


def json_to_csv_flattened(json_path, csv_path):
    try:
        # 1. JSON dosyasını oku
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        rows = []

        # 2. Veriyi düzleştir (Flattening)
        for review in data:
            rid = review.get('rid')
            text = review.get('text')
            triplets = review.get('triplets', [])

            # Eğer review içinde hiç triplet yoksa ama yine de satır olsun istersen:
            if not triplets:
                rows.append({
                    "rid": rid,
                    "text": text,
                    "target": "NULL",
                    "category": "NULL",
                    "polarity": "NULL"
                })
            else:
                # Her bir triplet için ayrı bir satır oluştur
                for triplet in triplets:
                    rows.append({
                        "rid": rid,
                        "text": text,
                        "target": triplet.get('target'),
                        "category": triplet.get('category'),
                        "polarity": triplet.get('polarity')
                    })

        # 3. Pandas DataFrame oluştur
        df = pd.DataFrame(rows)

        # 4. CSV olarak kaydet
        # utf-8-sig: Excel'in Türkçe karakterleri (ş, ğ, ı vb.) doğru tanımasını sağlar
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        print(f"--- İşlem Tamamlandı ---")
        print(f"Toplam Satır Sayısı: {len(df)}")
        print(f"Dosya oluşturuldu: {csv_path}")

        # İlk 5 satırı önizleme olarak göster
        print("\nÖnizleme:")
        print(df.head())

    except Exception as e:
        print(f"Hata oluştu kanka: {e}")


# --- AYARLAR ---
json_girdi = 'ali_erkan_test_native_turkish.json'
csv_cikti = 'ali_erkan_test_native_turkish.csv'

json_to_csv_flattened(json_girdi, csv_cikti)