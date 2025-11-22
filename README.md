# CMK 141-142 Tazminat Hesaplama Programı

Türk Ceza Muhakemesi Kanunu'nun 141 ve 142. maddelerine göre gözaltı, tutukluluk ve mala el koyma nedeniyle tazminat hesaplama programı.

## Özellikler

### 1. Gözaltı/Tutukluluk Tazminatı Hesaplama
- Başlangıç ve bitiş tarihleri girilerek otomatik süre hesaplama
- 1995-2025 yılları arası Çalışma ve Sosyal Güvenlik Bakanlığı asgari ücret verileri
- Yıl bazında detaylı hesaplama dökümü
- Günlük asgari ücret üzerinden tazminat hesaplama

### 2. Faiz Hesaplama
- Yasal faiz oranlarını kullanarak otomatik hesaplama
- Manuel faiz oranı girme seçeneği
- El koyma tarihinden karar tarihine kadar faiz işletme
- Yıl bazında faiz detayları

### 3. Mala El Koyma Tazminatı
- Malın el koyma tarihindeki piyasa değeri üzerinden hesaplama
- Faiz hesaplaması dahil toplam tutar belirleme
- Detaylı döküm ve raporlama

### 4. JSON Veri Saklama
- Hesaplama sonuçlarını JSON formatında kaydetme
- Saklanmış verileri okuma ve yeniden kullanma

## Kurulum

### Gereksinimler
- Python 3.6 veya üzeri

### Kurulum Adımları

```bash
# Depoyu klonlayın
git clone https://github.com/acaroktay1967-crypto/Tazminat-Hesaplama-Program-.git
cd Tazminat-Hesaplama-Program-

# Programı çalıştırın
python3 tazminat_hesaplama.py
```

## Kullanım

### Komut Satırı Kullanımı

Programı çalıştırdığınızda interaktif menü açılır:

```bash
python3 tazminat_hesaplama.py
```

### Menü Seçenekleri

1. **Gözaltı/Tutukluluk Tazminatı Hesapla**: Gözaltı veya tutukluluk süresi için tazminat hesaplar
2. **Mala El Koyma Tazminatı Hesapla**: Mala el koyma nedeniyle tazminat ve faiz hesaplar
3. **Faiz Hesapla**: Herhangi bir ana para için faiz hesaplar
4. **Çıkış**: Programdan çıkar

### Python Modülü Olarak Kullanım

```python
from tazminat_hesaplama import TazminatHesaplayici

# Hesaplayıcı nesnesi oluştur
hesaplayici = TazminatHesaplayici()

# Gözaltı/tutukluluk tazminatı hesapla
sonuc = hesaplayici.gozalti_tutukluluk_hesapla(
    baslangic_tarihi="01.01.2020",
    bitis_tarihi="31.12.2020"
)

# Sonucu yazdır
hesaplayici.sonuc_yazdir(sonuc, "GÖZALTI TAZMİNATI")

# Sonucu JSON olarak kaydet
hesaplayici.sonuc_kaydet(sonuc, "tazminat_hesap.json")
```

### Örnek Kullanım Senaryoları

#### Örnek 1: Gözaltı Tazminatı

```python
from tazminat_hesaplama import TazminatHesaplayici

hesaplayici = TazminatHesaplayici()
sonuc = hesaplayici.gozalti_tutukluluk_hesapla("15.03.2023", "20.08.2024")
hesaplayici.sonuc_yazdir(sonuc)
```

#### Örnek 2: Mala El Koyma Tazminatı

```python
from tazminat_hesaplama import TazminatHesaplayici

hesaplayici = TazminatHesaplayici()
sonuc = hesaplayici.mala_el_koyma_hesapla(
    mal_degeri=50000.00,
    el_koyma_tarihi="01.01.2023",
    karar_tarihi="31.12.2024"
)
hesaplayici.sonuc_yazdir(sonuc)
```

#### Örnek 3: Manuel Faiz Oranı ile Hesaplama

```python
from tazminat_hesaplama import TazminatHesaplayici

hesaplayici = TazminatHesaplayici()
sonuc = hesaplayici.faiz_hesapla(
    ana_para=100000.00,
    el_koyma_tarihi="01.06.2023",
    karar_tarihi="31.12.2024",
    manuel_faiz_orani=0.30  # %30 faiz oranı
)
hesaplayici.sonuc_yazdir(sonuc)
```

## Veri Yapısı

### Asgari Ücret Verileri (asgari_ucret_verileri.json)

Program, asgari ücret ve yasal faiz oranlarını JSON dosyasından okur:

```json
{
  "asgari_ucretler": {
    "2023": 8506800000,
    "2024": 11402400000,
    "2025": 17002440000
  },
  "yasal_faiz_oranlari": {
    "2023": 0.295,
    "2024": 0.40,
    "2025": 0.24
  }
}
```

**Not**: Tüm asgari ücret değerleri yeni Türk Lirası (TL) cinsindendir. 1 Ocak 2005 tarihinde yapılan para reformunda 1 milyon eski lira = 1 yeni lira olmuştur.

## Yasal Dayanak

### CMK Madde 141 - Gözaltı ve Tutuklulukta Tazminat

Kanuna uygun olmayan yakalama, gözaltına alma ve tutuklama nedeniyle kişiye verilen zararın tazmini hakkında düzenlemeler içerir.

### CMK Madde 142 - Eşyaya El Koymada Tazminat

Kanuna uygun olmayan eşyaya el koyma nedeniyle kişiye verilen zararın tazmini hakkında düzenlemeler içerir.

## Hesaplama Metodolojisi

### Gözaltı/Tutukluluk Tazminatı
- Her yıl için o yılın yıllık brüt asgari ücreti baz alınır
- Günlük ücret = Yıllık asgari ücret / 365
- Tazminat = Günlük ücret × Gün sayısı

### Faiz Hesaplama
- Yasal faiz oranı yıl bazında uygulanır
- Günlük faiz oranı = Yıllık faiz oranı / 365
- Faiz = Ana para × Günlük faiz oranı × Gün sayısı

### Mala El Koyma
- Tazminat = Malın el koyma tarihindeki piyasa değeri
- Faiz = Mal değeri üzerinden hesaplanan yasal faiz

## Çıktı Formatı

Program detaylı hesaplama dökümü sunar:

```
======================================================================
               GÖZALTI/TUTUKLULUK TAZMİNATI
======================================================================

Başlangıç Tarihi: 01.01.2023
Bitiş Tarihi: 31.12.2024
Toplam Gün: 731

Yıllık Detaylı Hesaplama:
----------------------------------------------------------------------

2023 Yılı:
  Gün Sayısı: 365
  Yıllık Asgari Ücret: 8,506.80 TL
  Günlük Ücret: 23.31 TL
  Yıl Tazminatı: 8,506.80 TL

2024 Yılı:
  Gün Sayısı: 366
  Yıllık Asgari Ücret: 11,402.40 TL
  Günlük Ücret: 31.15 TL
  Yıl Tazminatı: 11,402.40 TL

======================================================================
TOPLAM TAZMİNAT: 19,909.20 TL
======================================================================
```

## Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen:

1. Bu depoyu fork edin
2. Yeni bir branch oluşturun (`git checkout -b ozellik/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin ozellik/YeniOzellik`)
5. Pull Request oluşturun

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakınız.

## Sorumluluk Reddi

Bu program yalnızca bilgilendirme amaçlıdır. Hesaplamalar yaklaşık değerlerdir ve resmi hukuki işlemlerde kullanılmadan önce uzman görüşü alınmalıdır. Geliştiriciler, programın kullanımından kaynaklanan herhangi bir zarardan sorumlu değildir.

## İletişim

Sorularınız için issue açabilir veya pull request gönderebilirsiniz.
