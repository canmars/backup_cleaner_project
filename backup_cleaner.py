
import os
import configparser
from pathlib import Path

# Yapılandırmayı oku
config = configparser.ConfigParser()
config.read("config.ini")

backup_dir = Path(config["SETTINGS"]["backup_directory"])
extension = config["SETTINGS"]["file_extension"]

# .bak dosyalarını listele
backup_files = list(backup_dir.glob(f"*{extension}"))
if not backup_files:
    print("Hiç yedek dosyası bulunamadı.")
    exit()

# En yeni dosyayı belirle
latest_file = max(backup_files, key=lambda f: f.stat().st_mtime)

# Diğer tüm dosyaları sil
for file in backup_files:
    if file != latest_file:
        print(f"Siliniyor: {file}")
        file.unlink()

print(f"Sadece bu dosya bırakıldı: {latest_file}")
