#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMK 141-142 Tazminat Hesaplama Programı - Örnek Kullanımlar
"""

from tazminat_hesaplama import TazminatHesaplayici


def ornek_1_gozalti_tazminati():
    """Örnek 1: Gözaltı/Tutukluluk Tazminatı Hesaplama"""
    print("\n" + "="*70)
    print("ÖRNEK 1: GÖZALTI/TUTUKLULUK TAZMİNATI".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 2023 yılında 6 aylık tutukluluk
    sonuc = hesaplayici.gozalti_tutukluluk_hesapla(
        baslangic_tarihi="01.01.2023",
        bitis_tarihi="30.06.2023"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    
    # JSON olarak kaydet
    hesaplayici.sonuc_kaydet(sonuc, "ornek1_gozalti.json")
    

def ornek_2_cok_yillik_tutukluluk():
    """Örnek 2: Çok Yıllı Tutukluluk Tazminatı"""
    print("\n" + "="*70)
    print("ÖRNEK 2: ÇOK YILLI TUTUKLULUK TAZMİNATI".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 2020-2024 arası tutukluluk
    sonuc = hesaplayici.gozalti_tutukluluk_hesapla(
        baslangic_tarihi="15.03.2020",
        bitis_tarihi="20.08.2024"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek2_cok_yillik.json")


def ornek_3_mala_el_koyma():
    """Örnek 3: Mala El Koyma Tazminatı"""
    print("\n" + "="*70)
    print("ÖRNEK 3: MALA EL KOYMA TAZMİNATI".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 50.000 TL değerindeki mala el koyma
    sonuc = hesaplayici.mala_el_koyma_hesapla(
        mal_degeri=50000.00,
        el_koyma_tarihi="01.01.2023",
        karar_tarihi="31.12.2024"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek3_mal_elkoyma.json")


def ornek_4_yuksek_degerli_mal():
    """Örnek 4: Yüksek Değerli Mal El Koyma"""
    print("\n" + "="*70)
    print("ÖRNEK 4: YÜKSEK DEĞERLİ MAL EL KOYMA".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 500.000 TL değerindeki araç/taşınmaza el koyma
    sonuc = hesaplayici.mala_el_koyma_hesapla(
        mal_degeri=500000.00,
        el_koyma_tarihi="15.06.2022",
        karar_tarihi="01.12.2024"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek4_yuksek_deger.json")


def ornek_5_manuel_faiz():
    """Örnek 5: Manuel Faiz Oranı ile Hesaplama"""
    print("\n" + "="*70)
    print("ÖRNEK 5: MANUEL FAİZ ORANI İLE HESAPLAMA".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # %30 manuel faiz oranı ile
    sonuc = hesaplayici.faiz_hesapla(
        ana_para=100000.00,
        el_koyma_tarihi="01.01.2024",
        karar_tarihi="31.12.2024",
        manuel_faiz_orani=0.30  # %30
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek5_manuel_faiz.json")


def ornek_6_kisa_sure_gozalti():
    """Örnek 6: Kısa Süreli Gözaltı"""
    print("\n" + "="*70)
    print("ÖRNEK 6: KISA SÜRELİ GÖZALTI (15 GÜN)".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 15 günlük gözaltı
    sonuc = hesaplayici.gozalti_tutukluluk_hesapla(
        baslangic_tarihi="10.05.2024",
        bitis_tarihi="24.05.2024"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek6_kisa_sure.json")


def ornek_7_yillar_arasi_gecis():
    """Örnek 7: Yıllar Arası Geçişli Süre"""
    print("\n" + "="*70)
    print("ÖRNEK 7: YILLAR ARASI GEÇİŞLİ SÜRE".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 2023 sonundan 2024 başına geçiş
    sonuc = hesaplayici.gozalti_tutukluluk_hesapla(
        baslangic_tarihi="15.11.2023",
        bitis_tarihi="15.02.2024"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek7_yil_gecis.json")


def ornek_8_eski_tarihli():
    """Örnek 8: Eski Tarihli Tutukluluk (TL Dönüşümü)"""
    print("\n" + "="*70)
    print("ÖRNEK 8: ESKİ TARİHLİ TUTUKLULUK (2000-2001)".center(70))
    print("="*70)
    
    hesaplayici = TazminatHesaplayici()
    
    # 2000-2001 arası (YTL dönüşümü öncesi)
    sonuc = hesaplayici.gozalti_tutukluluk_hesapla(
        baslangic_tarihi="01.06.2000",
        bitis_tarihi="31.12.2001"
    )
    
    hesaplayici.sonuc_yazdir(sonuc)
    hesaplayici.sonuc_kaydet(sonuc, "ornek8_eski_tarih.json")


def tum_ornekleri_calistir():
    """Tüm örnekleri sırayla çalıştır"""
    print("\n" + "#"*70)
    print("CMK 141-142 TAZMİNAT HESAPLAMA - TÜM ÖRNEKLER".center(70))
    print("#"*70)
    
    ornek_1_gozalti_tazminati()
    ornek_2_cok_yillik_tutukluluk()
    ornek_3_mala_el_koyma()
    ornek_4_yuksek_degerli_mal()
    ornek_5_manuel_faiz()
    ornek_6_kisa_sure_gozalti()
    ornek_7_yillar_arasi_gecis()
    ornek_8_eski_tarihli()
    
    print("\n" + "#"*70)
    print("TÜM ÖRNEKLER TAMAMLANDI".center(70))
    print("#"*70)
    print("\nHesaplama sonuçları JSON dosyalarına kaydedildi.")
    print("Dosyalar: ornek1_gozalti.json, ornek2_cok_yillik.json, vb.")


if __name__ == "__main__":
    # Kullanıcıya seçenek sun
    print("\nÇalıştırmak istediğiniz örneği seçin:")
    print("1. Gözaltı/Tutukluluk Tazminatı")
    print("2. Çok Yıllı Tutukluluk Tazminatı")
    print("3. Mala El Koyma Tazminatı")
    print("4. Yüksek Değerli Mal El Koyma")
    print("5. Manuel Faiz Oranı ile Hesaplama")
    print("6. Kısa Süreli Gözaltı")
    print("7. Yıllar Arası Geçişli Süre")
    print("8. Eski Tarihli Tutukluluk")
    print("9. Tüm Örnekleri Çalıştır")
    
    secim = input("\nSeçiminiz (1-9): ").strip()
    
    ornekler = {
        '1': ornek_1_gozalti_tazminati,
        '2': ornek_2_cok_yillik_tutukluluk,
        '3': ornek_3_mala_el_koyma,
        '4': ornek_4_yuksek_degerli_mal,
        '5': ornek_5_manuel_faiz,
        '6': ornek_6_kisa_sure_gozalti,
        '7': ornek_7_yillar_arasi_gecis,
        '8': ornek_8_eski_tarihli,
        '9': tum_ornekleri_calistir
    }
    
    if secim in ornekler:
        ornekler[secim]()
    else:
        print("Geçersiz seçim!")
