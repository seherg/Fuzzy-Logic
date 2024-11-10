# Fuzzy Logic Battery Management System (BMS) 🔋⚡
![Soft Pink Minimalist Personal Growth Tips Graph](https://github.com/user-attachments/assets/3429d5aa-cc3f-4140-99c1-42efaa05a6bb)

Bu proje, batarya yönetim sistemi (BMS) üzerinde bulanık mantık (fuzzy logic) kullanarak batarya sağlığını değerlendiren ve batarya parametrelerini izleyen bir sistem geliştirmeyi amaçlamaktadır. Batarya sağlığı (SOH), sıcaklık, voltaj ve SOC (State of Charge - Şarj Durumu) gibi parametrelerle hesaplanır ve görselleştirilir.

## İçerik 📂
battery_management.py: Batarya parametrelerini yöneten ana modül.
bms_fuzzy.py: Batarya sağlığı (SOH) hesaplamalarını yapan fuzzy logic sistemi.
utils.py: Grafik görselleştirme ve yardımcı fonksiyonlar.
main.py: Kullanıcıdan batarya parametrelerini alarak sistemi çalıştıran ana dosya.
requirements.txt: Projede kullanılan Python kütüphaneleri.
## Özellikler 🌟
Bulanık Mantık (Fuzzy Logic): Batarya sağlığı (SOH) hesaplamalarında bulanık mantık kullanılarak, sıcaklık, voltaj ve SOC gibi parametrelerin değerlendirilmesi.
Kullanıcı Girdisi: Kullanıcıdan batarya sıcaklığı, voltaj ve SOC değerleri alınarak sistemin çalışması sağlanır.
Kalan Şarj Süresi Hesaplaması: Kullanıcının girdiği SOC değerine göre, bataryanın ne kadar süreyle çalışabileceği hesaplanır.
Grafik Görselleştirme: Batarya parametreleri zaman içinde görselleştirilerek kullanıcıya sunulur.
# Başlangıç 🚀
## Gerekli Kütüphaneler 📦
Proje, Python ve aşağıdaki kütüphaneleri gerektirir. requirements.txt dosyasındaki kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:
=> pip install -r requirements.txt

#Projeyi Çalıştırma ▶️
Projeyi çalıştırmak için terminal veya komut istemcisine aşağıdaki komutu yazın:
=> python main.py

Uygulama çalıştığında, sizden sırasıyla batarya sıcaklığı, voltajı ve SOC değeri istenecektir. Bu bilgileri girdikten sonra, batarya sağlığı (SOH) hesaplanacak ve sonucu görselleştirecektir.

# Ana İşlem Adımları 📝:
Sıcaklık (°C): Batarya sıcaklığını girin. (Örnek: 44)
Voltaj (V): Batarya voltajını girin. (Örnek: 34)
SOC (%): Batarya şarj durumunu girin. (Örnek: 54)
Programın sonunda, batarya sağlığına göre bir emoji ile durumu gösterilecektir:

🟢 İyi (SOH ≥ 70%)
🟡 Orta (40% ≤ SOH < 70%)
🔴 Kötü (SOH < 40%)
Ayrıca, bataryanın kalan şarj süresi hesaplanır ve kullanıcıya gösterilir:

⏳ Kalan Şarj Süresi: Bataryanın ne kadar süreyle çalışabileceği.
🔋 Tam Dolu Batarya Süresi: Batarya tamamen dolu olduğunda ne kadar süreyle çalışabileceği.
## Kullanılan Teknolojiler ⚙️
Python 3.x 🐍
Numpy: Sayısal verilerin işlenmesi için.
Matplotlib: Batarya parametrelerini görselleştirmek için.
Bulanık Mantık (Fuzzy Logic): Batarya sağlığı hesaplamaları için.

# Ekran Görüntüleri


![image](https://github.com/user-attachments/assets/a5834540-5342-4c1e-b325-ce7ef78e62dc)
![image](https://github.com/user-attachments/assets/1643c220-d97f-4c1d-b266-1e3f562a483c)
![image](https://github.com/user-attachments/assets/780b0dc5-8662-4037-8d4d-324dbc6a581e)


