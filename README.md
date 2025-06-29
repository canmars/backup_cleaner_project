
# Backup Cleaner

Bu küçük Python scripti, her gün POS sisteminden çıkan `.bak` uzantılı yedek dosyaların bulunduğu klasörü kontrol eder ve sadece **en son oluşturulan** yedeği bırakır, diğerlerini siler.

## 📌 Kullanım Amacı
Marketinizdeki yedek klasörü sürekli dolduğu için manuel temizlik gerekiyordu. Bu yazılım, bu işlemi otomatik hale getirir.

## 🔧 Sistem Gereksinimleri
- Python 3.x
- Windows işletim sistemi (Task Scheduler ile çalışacak)

## 📝 Yapılandırma
`config.ini` dosyasından:
- Yedek klasörü
- Dosya uzantısı
gibi bilgileri değiştirebilirsiniz.

## ⚙️ Otomatik Çalıştırma
Windows Görev Zamanlayıcı (Task Scheduler) ile bu scripti her gün otomatik çalıştırabilirsiniz. Detaylı bilgi için `scheduler_guide.txt` dosyasına bakın.

## 🧠 Yazılımı Geliştiren: 
@canmars ve ChatGPT
