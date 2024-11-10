import numpy as np

# Fuzzy logic hesaplama fonksiyonu
def compute_fuzzy_logic(temperature, voltage, soc):
    # Üyelik fonksiyonları (değiştirilmiş)
    temp_low = max(0, min(1, (25 - temperature) / 25))  # Düşük sıcaklık
    temp_high = max(0, min(1, (temperature - 25) / 25))  # Yüksek sıcaklık
    
    voltage_low = max(0, min(1, (30 - voltage) / 30))  # Düşük voltaj
    voltage_high = max(0, min(1, (voltage - 30) / 30))  # Yüksek voltaj
    
    soc_low = max(0, min(1, (40 - soc) / 40))  # Düşük SOC
    soc_high = max(0, min(1, (soc - 40) / 60))  # Yüksek SOC

    # 12 kural:
    # Kural 1: Sıcaklık ve voltaj düşükse -> Batarya sağlığı düşük
    rule1 = min(temp_low, voltage_low)
    # Kural 2: Sıcaklık düşük, voltaj yüksekse -> Batarya sağlığı orta
    rule2 = min(temp_low, voltage_high)
    # Kural 3: Sıcaklık yüksek, voltaj düşükse -> Batarya sağlığı orta
    rule3 = min(temp_high, voltage_low)
    # Kural 4: Sıcaklık yüksek, voltaj yüksekse -> Batarya sağlığı iyi
    rule4 = min(temp_high, voltage_high)
    
    # Kural 5: Sıcaklık düşük, SOC düşükse -> Batarya sağlığı çok kötü
    rule5 = min(temp_low, soc_low)
    # Kural 6: Sıcaklık düşük, SOC yüksekse -> Batarya sağlığı orta
    rule6 = min(temp_low, soc_high)
    # Kural 7: Sıcaklık yüksek, SOC düşükse -> Batarya sağlığı kötü
    rule7 = min(temp_high, soc_low)
    # Kural 8: Sıcaklık yüksek, SOC yüksekse -> Batarya sağlığı çok iyi
    rule8 = min(temp_high, soc_high)

    # Kural 9: Voltaj düşük, SOC düşükse -> Batarya sağlığı çok kötü
    rule9 = min(voltage_low, soc_low)
    # Kural 10: Voltaj düşük, SOC yüksekse -> Batarya sağlığı orta
    rule10 = min(voltage_low, soc_high)
    # Kural 11: Voltaj yüksek, SOC düşükse -> Batarya sağlığı kötü
    rule11 = min(voltage_high, soc_low)
    # Kural 12: Voltaj yüksek, SOC yüksekse -> Batarya sağlığı çok iyi
    rule12 = min(voltage_high, soc_high)
    
    # Batarya Sağlık Durumu (SOH) hesaplama
    soh = (rule1 * 10 + rule2 * 30 + rule3 * 20 + rule4 * 40 +
           rule5 * 5 + rule6 * 15 + rule7 * 10 + rule8 * 50 +
           rule9 * 5 + rule10 * 15 + rule11 * 20 + rule12 * 50)
    
    # 12 kuralın toplamının 100'e bölünmesiyle SOH hesaplanır
    soh = min(100, soh)  # SOH %100'ü aşamaz
    return soh
