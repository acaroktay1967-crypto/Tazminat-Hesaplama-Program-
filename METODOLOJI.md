# CMK 141-142 Tazminat Hesaplama - Yasal Dayanak ve Metodoloji

## Yasal Dayanak

### CMK Madde 141 - Gözaltı ve Tutuklulukta Tazminat

Türk Ceza Muhakemesi Kanunu'nun 141. maddesi, kanuna uygun olmayan yakalama, gözaltına alma ve tutuklama nedeniyle kişiye verilen zararın tazmini hakkında düzenlemeler içerir.

**Temel İlkeler:**
- Kanuna aykırı yakalama veya gözaltına alma
- Kanuna aykırı tutuklama
- Mahkumiyet hükmü verilmemesi veya beraat kararı
- Tazminat hakkı

### CMK Madde 142 - Eşyaya El Koymada Tazminat

142. madde, kanuna uygun olmayan eşyaya el koyma nedeniyle kişiye verilen zararın tazmini hakkında düzenlemeler içerir.

**Temel İlkeler:**
- Kanuna aykırı el koyma
- Malın iadesi veya değer tazmini
- Faiz işletilmesi

## Hesaplama Metodolojisi

### 1. Gözaltı/Tutukluluk Tazminatı Hesaplama

#### Formül:
```
Tazminat = Σ (Günlük Asgari Ücret × İlgili Yıldaki Gün Sayısı)
```

#### Adımlar:
1. Başlangıç ve bitiş tarihlerini belirle
2. Süreyi yıllara göre dağıt
3. Her yıl için:
   - O yılın asgari ücretini al
   - Günlük asgari ücret = Yıllık asgari ücret / 365
   - Yıl tazminatı = Günlük asgari ücret × O yıldaki gün sayısı
4. Tüm yılların tazminatlarını topla

#### Örnek Hesaplama:

**Durum:** 01.01.2023 - 30.06.2023 (181 gün)

```
2023 Yılı Asgari Ücret: 8,506.80 TL
Günlük Ücret: 8,506.80 / 365 = 23.31 TL
181 Gün Tazminatı: 23.31 × 181 = 4,218.44 TL
```

### 2. Faiz Hesaplama

#### Formül:
```
Faiz = Σ (Ana Para × Yıllık Faiz Oranı / 365 × İlgili Yıldaki Gün Sayısı)
```

#### Adımlar:
1. Ana para tutarını belirle
2. Başlangıç ve bitiş tarihlerini belirle
3. Süreyi yıllara göre dağıt
4. Her yıl için:
   - O yılın yasal faiz oranını al
   - Günlük faiz oranı = Yıllık faiz oranı / 365
   - Yıl faizi = Ana para × Günlük faiz oranı × O yıldaki gün sayısı
5. Tüm yılların faizlerini topla
6. Genel Toplam = Ana Para + Toplam Faiz

#### Örnek Hesaplama:

**Durum:** 50,000 TL ana para, 01.01.2024 - 31.12.2024 (366 gün)

```
2024 Yasal Faiz Oranı: %40
Günlük Faiz Oranı: 0.40 / 365 = 0.00109589
Toplam Faiz: 50,000 × 0.00109589 × 366 = 20,054.79 TL
Genel Toplam: 50,000 + 20,054.79 = 70,054.79 TL
```

### 3. Mala El Koyma Tazminatı

#### Metodoloji:
1. Malın el koyma tarihindeki piyasa değeri belirlenir
2. Bu değer ana para olarak kabul edilir
3. El koyma tarihinden karar tarihine kadar faiz işletilir
4. Toplam = Mal Değeri + Faiz

#### Örnek Hesaplama:

**Durum:** 100,000 TL değerinde araç, 01.01.2023 - 31.12.2024

```
Mal Değeri: 100,000 TL

2023 Faizi:
- Faiz Oranı: %29.5
- Gün Sayısı: 365
- Faiz: 100,000 × 0.295 / 365 × 365 = 29,500 TL

2024 Faizi:
- Faiz Oranı: %40
- Gün Sayısı: 366
- Faiz: 100,000 × 0.40 / 365 × 366 = 40,109.59 TL

Toplam Faiz: 69,609.59 TL
Genel Toplam: 100,000 + 69,609.59 = 169,609.59 TL
```

## Asgari Ücret Verileri

Program 1995-2025 yılları arası Çalışma ve Sosyal Güvenlik Bakanlığı tarafından belirlenen yıllık brüt asgari ücret verilerini kullanır.

### Önemli Notlar:

1. **Yeni Türk Lirası Dönüşümü (2005):**
   - 1 Ocak 2005 tarihinde para reformu yapılmıştır
   - 1 milyon eski TL = 1 yeni TL
   - Tüm veriler yeni TL cinsindendir

2. **Asgari Ücret Artışları:**
   - Yıllık olarak güncellenir
   - Bazı yıllarda yıl içi artış da olabilir
   - Program yıllık ortalama brüt asgari ücreti kullanır

3. **Son Yıl Verileri (2024-2025):**
   - 2024: 11,402.40 TL
   - 2025: 17,002.44 TL

## Yasal Faiz Oranları

Programda kullanılan yasal faiz oranları Türkiye Cumhuriyet Merkez Bankası ve ilgili mevzuat tarafından belirlenir.

### Güncel Oranlar:
- 2023: %29.5
- 2024: %40
- 2025: %24

### Manuel Faiz Girişi:
Program, otomatik faiz oranlarına ek olarak manuel faiz oranı girişine de izin verir.

## Hesaplama Hassasiyeti

- Tüm hesaplamalar Decimal kütüphanesi ile yapılır
- Kuruş hassasiyetinde (2 ondalık basamak) sonuç verilir
- Yuvarlama: Banker's rounding (ROUND_HALF_UP)

## Tarih Formatları

Program aşağıdaki tarih formatlarını destekler:
- GG.AA.YYYY (örn: 15.03.2023)
- GG/AA/YYYY (örn: 15/03/2023)
- YYYY-MM-DD (örn: 2023-03-15)

## Özel Durumlar

### 1. Yıl Geçişleri
Program, yıllar arası geçişleri otomatik olarak yönetir ve her yıl için doğru asgari ücret ve faiz oranını uygular.

### 2. Artık Yıllar
366 günlü yıllar (örn: 2024) doğru şekilde hesaplanır.

### 3. Kısa Süreler
Bir günlük süre bile doğru şekilde hesaplanır.

## Çıktı Formatı

### Konsol Çıktısı
- Başlık ve ayraçlarla düzenli format
- Yıl bazında detaylı hesaplama
- Binlik ayraç kullanımı (örn: 1,234.56)
- Toplam tutarlar vurgulanır

### JSON Çıktısı
```json
{
  "baslangic_tarihi": "01.01.2023",
  "bitis_tarihi": "30.06.2023",
  "toplam_gun": 181,
  "toplam_tazminat": 4218.44,
  "yillik_hesaplamalar": [...]
}
```

## Doğrulama ve Test

Program, aşağıdaki test senaryolarıyla doğrulanmıştır:
- Kısa süreli gözaltı (1-30 gün)
- Orta vadeli tutukluluk (1-12 ay)
- Uzun vadeli tutukluluk (1+ yıl)
- Yıl geçişli süreler
- Mala el koyma senaryoları
- Manuel faiz hesaplamaları

## Sorumluluk Reddi

Bu program yalnızca bilgilendirme ve hesaplama kolaylığı sağlamak amacıyla hazırlanmıştır. Resmi hukuki işlemlerde kullanılmadan önce:

1. Uzman hukuk danışmanlığı alınmalıdır
2. Güncel yasal düzenlemeler kontrol edilmelidir
3. Mahkeme kararları ve içtihatlar incelenmelidir
4. Hesaplamalar bağımsız olarak doğrulanmalıdır

Geliştiriciler, programın kullanımından kaynaklanan herhangi bir zarardan sorumlu değildir.

## Kaynaklar

- Türk Ceza Muhakemesi Kanunu (CMK)
- Çalışma ve Sosyal Güvenlik Bakanlığı Asgari Ücret Verileri
- Türkiye Cumhuriyet Merkez Bankası Faiz Oranları
- İlgili Yargıtay İçtihatları
