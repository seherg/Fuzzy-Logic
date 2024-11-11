import matplotlib.pyplot as plt

def visualize_battery_status(time, temperatures, voltages, socs, sohs):
   
    # Batarya parametrelerinin zaman içindeki değişimini görselleştiren fonksiyon.
   
    plt.figure(figsize=(10, 8))

    # Sıcaklık grafiği
    plt.subplot(2, 2, 1)
    plt.plot(time, temperatures, 'r-', label='Sıcaklık (°C)')
    plt.xlabel('Zaman (Saat)')
    plt.ylabel('Sıcaklık (°C)')
    plt.title('Zamanla Sıcaklık Değişimi')
    plt.grid(True)

    # Voltaj grafiği
    plt.subplot(2, 2, 2)
    plt.plot(time, voltages, 'b-', label='Voltaj (V)')
    plt.xlabel('Zaman (Saat)')
    plt.ylabel('Voltaj (V)')
    plt.title('Zamanla Voltaj Değişimi')
    plt.grid(True)

    # SOC grafiği
    plt.subplot(2, 2, 3)
    plt.plot(time, socs, 'g-', label='SOC (%)')
    plt.xlabel('Zaman (Saat)')
    plt.ylabel('SOC (%)')
    plt.title('Zamanla SOC Değişimi')
    plt.grid(True)

    # SOH grafiği
    plt.subplot(2, 2, 4)
    plt.plot(time, sohs, 'y-', label='SOH (%)')
    plt.xlabel('Zaman (Saat)')
    plt.ylabel('SOH (%)')
    plt.title('Zamanla SOH Değişimi')
    plt.grid(True)

    # Grafikleri göster
    plt.tight_layout()
    plt.show()
