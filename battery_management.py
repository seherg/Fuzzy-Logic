import numpy as np
from bms_fuzzy import compute_fuzzy_logic
from utils import visualize_battery_status

def manage_battery():
    temperatures, voltages, socs, sohs = [], [], [], []  # sohs listesi eklendi
    time = np.array([1, 2, 3, 4, 5])  # 5 ölçüm
    
    # Batarya kapasitesi ve güç (örnek değerler, gerçek değerler proje gereksinimlerine göre ayarlanabilir)
    battery_capacity = 50  # Batarya kapasitesi (kWh cinsinden)
    power_consumption_rate = 5  # Tüketim oranı (kW cinsinden, örneğin arabanın ortalama güç tüketimi)
    
    for i in range(5):
        print(f"\n--- {i+1}. Ölçüm ---")
        temperature = float(input("🌡️ Lütfen sıcaklık değerini girin (°C, -20 ile 80 arası): "))
        voltage = float(input("⚡ Lütfen voltaj değerini girin (V, 0 ile 60 arası): "))
        soc = float(input("🔋 Lütfen SOC (State of Charge) değerini girin (% 0 ile 100 arası): "))
        
        # SOH hesaplama
        soh = compute_fuzzy_logic(temperature, voltage, soc)
        
        # Verileri listeye ekleme
        temperatures.append(temperature)
        voltages.append(voltage)
        socs.append(soc)
        sohs.append(soh)  # sohs'e de değer ekleniyor
        
        # Batarya durumunu emoji ile yazma
        if soh is not None:
            if soh >= 70:
                print(f"🔋 Batarya Sağlık Durumu: 🟢 İyi (SOH: {soh:.2f}%)")
            elif 40 <= soh < 70:
                print(f"🔋 Batarya Sağlık Durumu: 🟡 Orta - Düzenli bakım önerilir. (SOH: {soh:.2f}%)")
            else:
                print(f"🔋 Batarya Sağlık Durumu: 🔴 Kötü - Değişim önerilir. (SOH: {soh:.2f}%)")
        else:
            print("🔋 Batarya Sağlık Durumu: Bilinmiyor - SOH değeri hesaplanamadı.")
        
        print(f"🔌 Şarj Durumu (SOC): {soc:.2f}%")
        print(f"🌡️ Sıcaklık: {temperature}°C, Voltaj: {voltage}V\n")
        
        # Kalan şarjın ne kadar sürede biteceğini hesapla
        remaining_capacity = (soc / 100) * battery_capacity  # Kalan kapasite (kWh)
        remaining_time = remaining_capacity / power_consumption_rate  # Kalan süre (saat cinsinden)
        print(f"🔋 Kalan Şarj Süresi: {remaining_time:.2f} saat")
        
        # Tam dolu batarya için süre hesaplama
        full_battery_time = battery_capacity / power_consumption_rate  # Tam dolu batarya süresi (saat cinsinden)
        print(f"🔋 Tam Dolu Batarya Süresi: {full_battery_time:.2f} saat")

    # Verileri görselleştirme
    visualize_battery_status(time, temperatures, voltages, socs, sohs)  # Görselleştirme fonksiyonu
