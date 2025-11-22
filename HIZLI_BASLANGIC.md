# Hızlı Başlangıç Kılavuzu

## CMK 141-142 Tazminat Hesaplama Programı

### 5 Dakikada Başlayın

#### 1. Programı İndirin
```bash
git clone https://github.com/acaroktay1967-crypto/Tazminat-Hesaplama-Program-.git
cd Tazminat-Hesaplama-Program-
```

#### 2. Programı Çalıştırın
```bash
python3 tazminat_hesaplama.py
```

#### 3. Menüden Seçim Yapın

**Örnek 1: Gözaltı Tazminatı**
```
Seçiminiz: 1
Başlangıç Tarihi: 01.01.2024
Bitiş Tarihi: 15.01.2024
```

**Örnek 2: Mala El Koyma**
```
Seçiminiz: 2
Mal Değeri: 50000
El Koyma Tarihi: 01.01.2023
Karar Tarihi: 31.12.2024
Manuel faiz? h (hayır - otomatik hesaplama)
```

**Örnek 3: Faiz Hesaplama**
```
Seçiminiz: 3
Ana Para: 100000
Başlangıç Tarihi: 01.06.2024
Bitiş Tarihi: 31.12.2024
Manuel faiz? e (evet)
Faiz Oranı: 30
```

### Örnek Dosyaları Çalıştırın

```bash
python3 ornekler.py
```

Menüden 1-9 arası bir seçim yapın:
- **1-8**: Belirli bir örneği çalıştır
- **9**: Tüm örnekleri çalıştır

### Python Modülü Olarak Kullanım

```python
from tazminat_hesaplama import TazminatHesaplayici

# Hesaplayıcı oluştur
h = TazminatHesaplayici()

# Gözaltı tazminatı hesapla
sonuc = h.gozalti_tutukluluk_hesapla("01.01.2024", "31.01.2024")

# Sonucu göster
h.sonuc_yazdir(sonuc)

# JSON olarak kaydet
h.sonuc_kaydet(sonuc, "hesaplama.json")
```

### Hızlı İpuçları

✅ **Tarih Formatı:** GG.AA.YYYY (örn: 15.03.2024)

✅ **Para Birimi:** Türk Lirası (TL)

✅ **Faiz Oranları:** Otomatik veya manuel girebilirsiniz

✅ **Sonuçları Kaydetme:** JSON formatında kaydedebilirsiniz

### Sık Karşılaşılan Sorular

**S: Hangi Python sürümü gerekli?**
C: Python 3.6 veya üzeri yeterlidir.

**S: Ek paket yüklenmeli mi?**
C: Hayır, sadece Python standart kütüphaneleri kullanılır.

**S: Asgari ücret verileri güncel mi?**
C: Evet, 2025 yılı dahil günceldir.

**S: Sonuçları nasıl kaydederim?**
C: Program, hesaplama sonrası kaydetme seçeneği sunar.

**S: Manuel faiz oranı nasıl girilir?**
C: Yüzde olarak girin (örn: 24 = %24), program otomatik çevirir.

### Daha Fazla Bilgi

- **Detaylı Kullanım:** README.md dosyasına bakın
- **Yasal Dayanak:** METODOLOJI.md dosyasını okuyun
- **Örnekler:** ornekler.py dosyasını inceleyin

### Destek

Sorularınız için GitHub'da issue açabilirsiniz:
https://github.com/acaroktay1967-crypto/Tazminat-Hesaplama-Program-/issues
