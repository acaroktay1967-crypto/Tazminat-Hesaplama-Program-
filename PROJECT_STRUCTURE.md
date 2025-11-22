# Proje Yapısı

## CMK 141-142 Tazminat Hesaplama Programı

### Dosya Organizasyonu

```
Tazminat-Hesaplama-Program-/
│
├── tazminat_hesaplama.py          # Ana program dosyası
├── ornekler.py                     # Örnek kullanım senaryoları
├── asgari_ucret_verileri.json     # Asgari ücret ve faiz oranı verileri
│
├── README.md                       # Ana dokümantasyon
├── HIZLI_BASLANGIC.md             # Hızlı başlangıç kılavuzu
├── METODOLOJI.md                   # Yasal dayanak ve hesaplama metodolojisi
├── PROJECT_STRUCTURE.md            # Bu dosya - proje yapısı
│
├── requirements.txt                # Python gereksinimleri
├── .gitignore                      # Git ignore kuralları
└── LICENSE                         # MIT Lisansı
```

### Ana Modüller

#### 1. tazminat_hesaplama.py

**Sınıf:** `TazminatHesaplayici`

**Temel Metodlar:**
- `gozalti_tutukluluk_hesapla()` - Gözaltı/tutukluluk tazminatı
- `faiz_hesapla()` - Yasal faiz hesaplama
- `mala_el_koyma_hesapla()` - Mala el koyma tazminatı
- `sonuc_yazdir()` - Formatlanmış çıktı
- `sonuc_kaydet()` - JSON kaydetme
- `ana_menu()` - İnteraktif kullanıcı arayüzü

**Yardımcı Metodlar:**
- `_tarih_parse()` - Tarih dönüştürme
- `_gun_sayisi_hesapla()` - Gün sayısı hesaplama
- `_yil_bazinda_gun_dagilimi()` - Yıllara göre dağılım
- `_asgari_ucret_getir()` - Asgari ücret verisi alma
- `_faiz_orani_getir()` - Faiz oranı verisi alma

#### 2. ornekler.py

**8 Farklı Örnek Senaryo:**
1. Kısa süreli gözaltı (6 ay)
2. Çok yıllı tutukluluk (4+ yıl)
3. Mala el koyma (50,000 TL)
4. Yüksek değerli mal (500,000 TL)
5. Manuel faiz oranı kullanımı
6. Çok kısa süre (15 gün)
7. Yıllar arası geçiş
8. Eski tarihli (YTL dönüşümü öncesi)

#### 3. asgari_ucret_verileri.json

**Veri Yapısı:**
```json
{
  "asgari_ucretler": {
    "1995": 4.50,
    ...
    "2025": 17002.44
  },
  "yasal_faiz_oranlari": {
    "2023": 0.295,
    "2024": 0.40,
    "2025": 0.24
  },
  "yeni_turk_lirasi_donusum": {...},
  "aciklama": "..."
}
```

### Özellikler

#### Desteklenen İşlevler
✅ Gözaltı/tutukluluk tazminatı hesaplama
✅ Mala el koyma tazminatı hesaplama
✅ Otomatik yasal faiz hesaplama
✅ Manuel faiz oranı desteği
✅ Yıl bazında detaylı döküm
✅ JSON formatında veri saklama
✅ Çoklu tarih formatı desteği
✅ İnteraktif menü sistemi
✅ Python modülü olarak kullanım

#### Desteklenen Tarih Formatları
- GG.AA.YYYY (15.03.2024)
- GG/AA/YYYY (15/03/2024)
- YYYY-MM-DD (2024-03-15)

#### Veri Aralığı
- **Yıllar:** 1995-2025
- **Asgari Ücretler:** Çalışma Bakanlığı verileri
- **Faiz Oranları:** 2019-2025

### Teknik Detaylar

#### Kullanılan Kütüphaneler
- `json` - Veri okuma/yazma
- `datetime` - Tarih işlemleri
- `timedelta` - Süre hesaplamaları
- `Decimal` - Hassas sayısal hesaplamalar
- `os` - Dosya yolu işlemleri

#### Hesaplama Hassasiyeti
- **Decimal** kullanımı ile yüksek hassasiyet
- Kuruş hassasiyetinde sonuçlar (2 ondalık)
- ROUND_HALF_UP yuvarlama stratejisi

#### Kodlama Standartları
- UTF-8 encoding
- PEP 8 stil kılavuzu
- Docstring dokümantasyonu
- Type hints kullanımı (bazı fonksiyonlarda)

### Test ve Doğrulama

#### Test Kapsamı
✓ Kısa süreli gözaltı (1-30 gün)
✓ Orta vadeli tutukluluk (1-12 ay)
✓ Uzun vadeli tutukluluk (1+ yıl)
✓ Yıl geçişleri
✓ Artık yıllar
✓ Farklı tarih formatları
✓ Mala el koyma senaryoları
✓ Manuel faiz hesaplamaları
✓ JSON kaydetme/okuma
✓ Hata durumları

#### Doğrulama
- Manuel hesaplamalarla karşılaştırma
- Farklı senaryolar için test
- Sınır değer testleri
- Format testleri

### Kullanım Senaryoları

#### 1. Komut Satırı
```bash
python3 tazminat_hesaplama.py
```

#### 2. Python Modülü
```python
from tazminat_hesaplama import TazminatHesaplayici
h = TazminatHesaplayici()
sonuc = h.gozalti_tutukluluk_hesapla("01.01.2024", "31.12.2024")
```

#### 3. Örnek Çalıştırma
```bash
python3 ornekler.py
```

### Gelecek Geliştirmeler

#### Potansiyel İyileştirmeler
- [ ] Web arayüzü (Flask/Django)
- [ ] Excel rapor çıktısı
- [ ] Veritabanı entegrasyonu
- [ ] Çoklu dil desteği
- [ ] API servisi
- [ ] Grafik arayüz (GUI)
- [ ] Toplu hesaplama özelliği
- [ ] Karşılaştırma analizi

### Lisans ve Katkı

**Lisans:** MIT License

**Katkı Yapmak İçin:**
1. Repository'yi fork edin
2. Yeni özellik branch'i oluşturun
3. Değişikliklerinizi commit edin
4. Pull request gönderin

### Destek ve İletişim

**Sorunlar için:**
- GitHub Issues kullanın
- Detaylı açıklama ekleyin
- Örnek girdi/çıktı sağlayın

**Dokümantasyon:**
- README.md - Genel kullanım
- HIZLI_BASLANGIC.md - Hızlı başlangıç
- METODOLOJI.md - Yasal ve teknik detaylar
- PROJECT_STRUCTURE.md - Proje yapısı

---

**Son Güncelleme:** Kasım 2024
**Versiyon:** 1.0.0
**Durum:** Stabil - Production Ready
