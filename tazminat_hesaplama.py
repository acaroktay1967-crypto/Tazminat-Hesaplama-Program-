#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CMK 141-142 Tazminat Hesaplama Programı
========================================

Türk Ceza Muhakemesi Kanunu'nun 141 ve 142. maddelerine göre
gözaltı, tutukluluk ve mala el koyma nedeniyle tazminat hesaplama programı.

Yazar: Tazminat Hesaplama Programı
Lisans: MIT
"""

import json
import os
from datetime import datetime, timedelta
from decimal import Decimal, ROUND_HALF_UP


class TazminatHesaplayici:
    """CMK 141-142 maddelerine göre tazminat hesaplama sınıfı"""
    
    def __init__(self, veri_dosyasi='asgari_ucret_verileri.json'):
        """
        Tazminat hesaplayıcı başlatıcı
        
        Args:
            veri_dosyasi: Asgari ücret ve faiz oranları içeren JSON dosya yolu
        """
        self.veri_dosyasi = veri_dosyasi
        self.veriler = self._veri_yukle()
        self.asgari_ucretler = self.veriler.get('asgari_ucretler', {})
        self.yasal_faiz_oranlari = self.veriler.get('yasal_faiz_oranlari', {})
        
    def _veri_yukle(self):
        """JSON dosyasından verileri yükle"""
        dosya_yolu = os.path.join(os.path.dirname(__file__), self.veri_dosyasi)
        try:
            with open(dosya_yolu, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"UYARI: {dosya_yolu} bulunamadı. Varsayılan değerler kullanılacak.")
            return {'asgari_ucretler': {}, 'yasal_faiz_oranlari': {}}
    
    def _tarih_parse(self, tarih_str):
        """
        Tarih string'ini datetime nesnesine çevir
        
        Args:
            tarih_str: 'GG.AA.YYYY' veya 'GG/AA/YYYY' formatında tarih
            
        Returns:
            datetime nesnesi
        """
        # Farklı formatlarda tarih girişini destekle
        for fmt in ['%d.%m.%Y', '%d/%m/%Y', '%Y-%m-%d']:
            try:
                return datetime.strptime(tarih_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Geçersiz tarih formatı: {tarih_str}. Lütfen GG.AA.YYYY formatında giriniz.")
    
    def _gun_sayisi_hesapla(self, baslangic, bitis):
        """İki tarih arasındaki gün sayısını hesapla"""
        if isinstance(baslangic, str):
            baslangic = self._tarih_parse(baslangic)
        if isinstance(bitis, str):
            bitis = self._tarih_parse(bitis)
        return (bitis - baslangic).days + 1  # Her iki gün de dahil
    
    def _yil_bazinda_gun_dagilimi(self, baslangic, bitis):
        """
        Başlangıç ve bitiş tarihleri arasındaki günleri yıllara göre dağıt
        
        Args:
            baslangic: Başlangıç tarihi (datetime veya string)
            bitis: Bitiş tarihi (datetime veya string)
            
        Returns:
            dict: {yıl: gün_sayısı} şeklinde sözlük
        """
        if isinstance(baslangic, str):
            baslangic = self._tarih_parse(baslangic)
        if isinstance(bitis, str):
            bitis = self._tarih_parse(bitis)
            
        gun_dagilimi = {}
        current_date = baslangic
        
        while current_date <= bitis:
            yil = current_date.year
            gun_dagilimi[yil] = gun_dagilimi.get(yil, 0) + 1
            current_date += timedelta(days=1)
            
        return gun_dagilimi
    
    def _asgari_ucret_getir(self, yil):
        """
        Belirtilen yıl için asgari ücreti getir
        
        Args:
            yil: Yıl (int)
            
        Returns:
            Decimal: Asgari ücret tutarı
        """
        yil_str = str(yil)
        if yil_str not in self.asgari_ucretler:
            raise ValueError(f"{yil} yılı için asgari ücret verisi bulunamadı.")
        
        ucret = Decimal(str(self.asgari_ucretler[yil_str]))
        return ucret
    
    def gozalti_tutukluluk_hesapla(self, baslangic_tarihi, bitis_tarihi, detayli_cikti=True):
        """
        Gözaltı/tutukluluk tazminatı hesapla
        
        Args:
            baslangic_tarihi: Gözaltı/tutukluluk başlangıç tarihi
            bitis_tarihi: Gözaltı/tutukluluk bitiş tarihi
            detayli_cikti: Yıl bazında detaylı döküm göster
            
        Returns:
            dict: Hesaplama sonuçları
        """
        gun_dagilimi = self._yil_bazinda_gun_dagilimi(baslangic_tarihi, bitis_tarihi)
        toplam_gun = sum(gun_dagilimi.values())
        
        yillik_hesaplamalar = []
        toplam_tazminat = Decimal('0')
        
        for yil in sorted(gun_dagilimi.keys()):
            gun_sayisi = gun_dagilimi[yil]
            yillik_asgari_ucret = self._asgari_ucret_getir(yil)
            gunluk_ucret = yillik_asgari_ucret / Decimal('365')
            yil_tazminati = gunluk_ucret * Decimal(str(gun_sayisi))
            
            yillik_hesaplamalar.append({
                'yil': yil,
                'gun_sayisi': gun_sayisi,
                'yillik_asgari_ucret': float(yillik_asgari_ucret.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)),
                'gunluk_ucret': float(gunluk_ucret.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)),
                'yil_tazminati': float(yil_tazminati.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
            })
            
            toplam_tazminat += yil_tazminati
        
        sonuc = {
            'baslangic_tarihi': baslangic_tarihi if isinstance(baslangic_tarihi, str) else baslangic_tarihi.strftime('%d.%m.%Y'),
            'bitis_tarihi': bitis_tarihi if isinstance(bitis_tarihi, str) else bitis_tarihi.strftime('%d.%m.%Y'),
            'toplam_gun': toplam_gun,
            'toplam_tazminat': float(toplam_tazminat.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)),
            'yillik_hesaplamalar': yillik_hesaplamalar if detayli_cikti else None
        }
        
        return sonuc
    
    def _faiz_orani_getir(self, yil):
        """
        Belirtilen yıl için yasal faiz oranını getir
        
        Args:
            yil: Yıl (int)
            
        Returns:
            Decimal: Faiz oranı (örn: 0.24 = %24)
        """
        yil_str = str(yil)
        if yil_str in self.yasal_faiz_oranlari:
            return Decimal(str(self.yasal_faiz_oranlari[yil_str]))
        else:
            # Varsayılan oran
            print(f"UYARI: {yil} yılı için faiz oranı bulunamadı. %24 varsayılan oran kullanılıyor.")
            return Decimal('0.24')
    
    def faiz_hesapla(self, ana_para, el_koyma_tarihi, karar_tarihi, manuel_faiz_orani=None, detayli_cikti=True):
        """
        Yasal faiz hesapla
        
        Args:
            ana_para: Ana para tutarı (mal değeri veya tazminat tutarı)
            el_koyma_tarihi: El koyma/hak doğum tarihi
            karar_tarihi: Dava kararı tarihi
            manuel_faiz_orani: Manuel faiz oranı (örn: 0.24 = %24), belirtilmezse otomatik kullanılır
            detayli_cikti: Yıl bazında detaylı döküm göster
            
        Returns:
            dict: Faiz hesaplama sonuçları
        """
        gun_dagilimi = self._yil_bazinda_gun_dagilimi(el_koyma_tarihi, karar_tarihi)
        ana_para_decimal = Decimal(str(ana_para))
        
        yillik_faiz_hesaplamalari = []
        toplam_faiz = Decimal('0')
        
        for yil in sorted(gun_dagilimi.keys()):
            gun_sayisi = gun_dagilimi[yil]
            
            if manuel_faiz_orani is not None:
                faiz_orani = Decimal(str(manuel_faiz_orani))
            else:
                faiz_orani = self._faiz_orani_getir(yil)
            
            # Günlük faiz oranı
            gunluk_faiz_orani = faiz_orani / Decimal('365')
            
            # Bu yıl için faiz tutarı
            yil_faizi = ana_para_decimal * gunluk_faiz_orani * Decimal(str(gun_sayisi))
            
            yillik_faiz_hesaplamalari.append({
                'yil': yil,
                'gun_sayisi': gun_sayisi,
                'faiz_orani': float(faiz_orani),
                'faiz_orani_yuzde': f"%{float(faiz_orani * 100):.2f}",
                'yil_faizi': float(yil_faizi.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))
            })
            
            toplam_faiz += yil_faizi
        
        sonuc = {
            'ana_para': float(ana_para_decimal.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)),
            'el_koyma_tarihi': el_koyma_tarihi if isinstance(el_koyma_tarihi, str) else el_koyma_tarihi.strftime('%d.%m.%Y'),
            'karar_tarihi': karar_tarihi if isinstance(karar_tarihi, str) else karar_tarihi.strftime('%d.%m.%Y'),
            'toplam_gun': sum(gun_dagilimi.values()),
            'toplam_faiz': float(toplam_faiz.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)),
            'genel_toplam': float((ana_para_decimal + toplam_faiz).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)),
            'yillik_faiz_hesaplamalari': yillik_faiz_hesaplamalari if detayli_cikti else None
        }
        
        return sonuc
    
    def mala_el_koyma_hesapla(self, mal_degeri, el_koyma_tarihi, karar_tarihi, 
                              manuel_faiz_orani=None, detayli_cikti=True):
        """
        Mala el koyma nedeniyle tazminat ve faiz hesapla
        
        Args:
            mal_degeri: El koyma tarihindeki piyasa değeri
            el_koyma_tarihi: El koyma tarihi
            karar_tarihi: Dava kararı tarihi
            manuel_faiz_orani: Manuel faiz oranı (örn: 0.24 = %24)
            detayli_cikti: Yıl bazında detaylı döküm göster
            
        Returns:
            dict: Hesaplama sonuçları
        """
        # Mala el koymada tazminat = mal değeri, faiz bu değer üzerinden hesaplanır
        faiz_sonuc = self.faiz_hesapla(
            mal_degeri, 
            el_koyma_tarihi, 
            karar_tarihi, 
            manuel_faiz_orani, 
            detayli_cikti
        )
        
        return {
            'hesaplama_turu': 'Mala El Koyma Tazminatı',
            'mal_degeri': mal_degeri,
            **faiz_sonuc
        }
    
    def sonuc_yazdir(self, sonuc, baslik=""):
        """
        Hesaplama sonuçlarını ekrana yazdır
        
        Args:
            sonuc: Hesaplama sonucu dictionary
            baslik: Çıktı başlığı
        """
        print("\n" + "=" * 70)
        if baslik:
            print(baslik.center(70))
            print("=" * 70)
        
        # Gözaltı/tutukluluk hesaplaması
        if 'toplam_tazminat' in sonuc and 'toplam_faiz' not in sonuc:
            print(f"\nBaşlangıç Tarihi: {sonuc['baslangic_tarihi']}")
            print(f"Bitiş Tarihi: {sonuc['bitis_tarihi']}")
            print(f"Toplam Gün: {sonuc['toplam_gun']}")
            
            if sonuc.get('yillik_hesaplamalar'):
                print("\nYıllık Detaylı Hesaplama:")
                print("-" * 70)
                for hesap in sonuc['yillik_hesaplamalar']:
                    print(f"\n{hesap['yil']} Yılı:")
                    print(f"  Gün Sayısı: {hesap['gun_sayisi']}")
                    print(f"  Yıllık Asgari Ücret: {hesap['yillik_asgari_ucret']:,.2f} TL")
                    print(f"  Günlük Ücret: {hesap['gunluk_ucret']:,.2f} TL")
                    print(f"  Yıl Tazminatı: {hesap['yil_tazminati']:,.2f} TL")
            
            print("\n" + "=" * 70)
            print(f"TOPLAM TAZMİNAT: {sonuc['toplam_tazminat']:,.2f} TL")
            print("=" * 70)
        
        # Faiz hesaplaması veya mala el koyma
        elif 'toplam_faiz' in sonuc:
            if 'hesaplama_turu' in sonuc:
                print(f"\nHesaplama Türü: {sonuc['hesaplama_turu']}")
                print(f"Mal Değeri: {sonuc['mal_degeri']:,.2f} TL")
            
            print(f"\nAna Para: {sonuc['ana_para']:,.2f} TL")
            print(f"El Koyma/Başlangıç Tarihi: {sonuc['el_koyma_tarihi']}")
            print(f"Karar Tarihi: {sonuc['karar_tarihi']}")
            print(f"Toplam Gün: {sonuc['toplam_gun']}")
            
            if sonuc.get('yillik_faiz_hesaplamalari'):
                print("\nYıllık Faiz Detayı:")
                print("-" * 70)
                for hesap in sonuc['yillik_faiz_hesaplamalari']:
                    print(f"\n{hesap['yil']} Yılı:")
                    print(f"  Gün Sayısı: {hesap['gun_sayisi']}")
                    print(f"  Faiz Oranı: {hesap['faiz_orani_yuzde']}")
                    print(f"  Yıl Faizi: {hesap['yil_faizi']:,.2f} TL")
            
            print("\n" + "=" * 70)
            print(f"Ana Para: {sonuc['ana_para']:,.2f} TL")
            print(f"Toplam Faiz: {sonuc['toplam_faiz']:,.2f} TL")
            print(f"GENEL TOPLAM: {sonuc['genel_toplam']:,.2f} TL")
            print("=" * 70)
    
    def sonuc_kaydet(self, sonuc, dosya_adi):
        """
        Hesaplama sonuçlarını JSON dosyasına kaydet
        
        Args:
            sonuc: Hesaplama sonucu dictionary
            dosya_adi: Kaydedilecek dosya adı
        """
        with open(dosya_adi, 'w', encoding='utf-8') as f:
            json.dump(sonuc, f, ensure_ascii=False, indent=2)
        print(f"\nSonuçlar {dosya_adi} dosyasına kaydedildi.")


def ana_menu():
    """Ana program menüsü"""
    hesaplayici = TazminatHesaplayici()
    
    while True:
        print("\n" + "=" * 70)
        print("CMK 141-142 TAZMİNAT HESAPLAMA PROGRAMI".center(70))
        print("=" * 70)
        print("\n1. Gözaltı/Tutukluluk Tazminatı Hesapla")
        print("2. Mala El Koyma Tazminatı Hesapla")
        print("3. Faiz Hesapla")
        print("4. Çıkış")
        
        secim = input("\nSeçiminiz (1-4): ").strip()
        
        if secim == '1':
            print("\n--- Gözaltı/Tutukluluk Tazminatı Hesaplama ---")
            try:
                baslangic = input("Başlangıç Tarihi (GG.AA.YYYY): ").strip()
                bitis = input("Bitiş Tarihi (GG.AA.YYYY): ").strip()
                
                sonuc = hesaplayici.gozalti_tutukluluk_hesapla(baslangic, bitis)
                hesaplayici.sonuc_yazdir(sonuc, "GÖZALTI/TUTUKLULUK TAZMİNATI")
                
                kaydet = input("\nSonuçları dosyaya kaydetmek ister misiniz? (e/h): ").strip().lower()
                if kaydet == 'e':
                    dosya_adi = input("Dosya adı (örn: tazminat_hesap.json): ").strip()
                    hesaplayici.sonuc_kaydet(sonuc, dosya_adi)
                    
            except Exception as e:
                print(f"\nHATA: {str(e)}")
        
        elif secim == '2':
            print("\n--- Mala El Koyma Tazminatı Hesaplama ---")
            try:
                mal_degeri = float(input("Malın El Koyma Tarihindeki Piyasa Değeri (TL): ").strip())
                el_koyma = input("El Koyma Tarihi (GG.AA.YYYY): ").strip()
                karar = input("Dava Kararı Tarihi (GG.AA.YYYY): ").strip()
                
                manuel_faiz = input("Manuel faiz oranı girmek ister misiniz? (e/h): ").strip().lower()
                faiz_orani = None
                if manuel_faiz == 'e':
                    faiz_yuzde = float(input("Yıllık faiz oranı (%, örn: 24): ").strip())
                    faiz_orani = faiz_yuzde / 100
                
                sonuc = hesaplayici.mala_el_koyma_hesapla(
                    mal_degeri, el_koyma, karar, faiz_orani
                )
                hesaplayici.sonuc_yazdir(sonuc, "MALA EL KOYMA TAZMİNATI")
                
                kaydet = input("\nSonuçları dosyaya kaydetmek ister misiniz? (e/h): ").strip().lower()
                if kaydet == 'e':
                    dosya_adi = input("Dosya adı (örn: mal_elkoyma.json): ").strip()
                    hesaplayici.sonuc_kaydet(sonuc, dosya_adi)
                    
            except Exception as e:
                print(f"\nHATA: {str(e)}")
        
        elif secim == '3':
            print("\n--- Faiz Hesaplama ---")
            try:
                ana_para = float(input("Ana Para (TL): ").strip())
                baslangic = input("Başlangıç Tarihi (GG.AA.YYYY): ").strip()
                bitis = input("Bitiş Tarihi (GG.AA.YYYY): ").strip()
                
                manuel_faiz = input("Manuel faiz oranı girmek ister misiniz? (e/h): ").strip().lower()
                faiz_orani = None
                if manuel_faiz == 'e':
                    faiz_yuzde = float(input("Yıllık faiz oranı (%, örn: 24): ").strip())
                    faiz_orani = faiz_yuzde / 100
                
                sonuc = hesaplayici.faiz_hesapla(ana_para, baslangic, bitis, faiz_orani)
                hesaplayici.sonuc_yazdir(sonuc, "FAİZ HESAPLAMA")
                
                kaydet = input("\nSonuçları dosyaya kaydetmek ister misiniz? (e/h): ").strip().lower()
                if kaydet == 'e':
                    dosya_adi = input("Dosya adı (örn: faiz_hesap.json): ").strip()
                    hesaplayici.sonuc_kaydet(sonuc, dosya_adi)
                    
            except Exception as e:
                print(f"\nHATA: {str(e)}")
        
        elif secim == '4':
            print("\nProgram sonlandırılıyor...")
            break
        
        else:
            print("\nGeçersiz seçim! Lütfen 1-4 arasında bir değer giriniz.")


if __name__ == "__main__":
    ana_menu()
