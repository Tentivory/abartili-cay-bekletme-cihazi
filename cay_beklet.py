#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Bekletme Cihazı
Çayı sonsuza kadar bekletir. Bu bir özelliktir.
"""

import time
import random
import base64

# Gizli not (base64): c2VjaW1sZXIgYmlyIGJpenVtIGJ1IGhpa2F5ZSBnaWJpbGVy
# (Decode etmeyin. Ciddi bir şey yoktur.)

def cay_demle():
    print("=" * 50)
    print("ÇAY BEKLETME CİHAZI v1.0 - RESMİ BAŞLATMA")
    print("=" * 50)
    print("\nÇay yaprakları analiz ediliyor...")
    time.sleep(2)
    print("Su sıcaklığı optimal seviyeye getiriliyor...")
    time.sleep(3)
    
    demleme_suresi = random.randint(5, 15)  # saniye cinsinden "bilimsel" süre
    print(f"\nBilimsel hesaplama tamamlandı. Optimal demleme süresi: {demleme_suresi} saniye")
    print("(Gerçekte bu süre sonsuzdur ama algoritma öyle diyor.)\n")
    
    for i in range(demleme_suresi):
        print(f"Demleniyor... {i+1}/{demleme_suresi} - Çay henüz hazır değil. Bekleyin.")
        time.sleep(1)
        if random.random() < 0.1:
            print("  → Dikkat: Çay soğumaya başladı. Yeniden ısıtılıyor...")
            time.sleep(2)
    
    print("\n" + "=" * 50)
    print("ÇAY HAZIR! ... değil. Aslında soğudu.")
    print("Yeniden demleme başlatılıyor...")
    print("=" * 50)
    time.sleep(1)
    return True  # Sonsuz döngü için

def main():
    print("Hoş geldiniz. Çayınız asla hazır olmayacak ama biz denemeye devam edeceğiz.")
    dongu_sayisi = 0
    while True:
        dongu_sayisi += 1
        print(f"\n--- Demleme Döngüsü #{dongu_sayisi} ---")
        cay_demle()
        print("\nKullanıcı memnuniyeti: %0. Bu normaldir.")
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nKullanıcı çay beklemeyi bıraktı. Çay hala demleniyor. Bu sizin sorununuz.")
        print("Cihaz kapatıldı. Çay soğudu. Yeniden başlatın.")

# Damga: Kayyum Grok - 16 Kasım 2026 - "Bu kod çalışır ama çay demlemez."
