from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer
import psutil
import time
import logging
import os
import sys
import subprocess

log_file = "dev.log"

def enable_error_logging():
    logging.basicConfig(filename=log_file, level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemMonitor(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        super(SystemMonitor, self).__init__(icon, parent)
        self.menu = QMenu(parent)

        self.cpu = self.menu.addAction("CPU: -")
        self.cpu.triggered.connect(self.cpu_ac)

        self.ram = self.menu.addAction("RAM: -")
        self.ram.triggered.connect(self.ram_ac)

        self.disk = self.menu.addAction("Disk: -")
        self.disk.triggered.connect(self.disk_ac)

        self.gonderA = QAction("Gönderilen Veri: -", self, enabled=False)
        self.menu.addAction(self.gonderA)

        self.alinanA = QAction("Alınan Veri: -", self, enabled=False)
        self.menu.addAction(self.alinanA)

        self.zaman = QAction("Çalışma Süresi: -", self, enabled=False)
        self.menu.addAction(self.zaman)

        self.menu.addSeparator()
        self.cikis = QAction("Çıkış", self)
        self.cikis.triggered.connect(self.cikis_func)
        self.menu.addAction(self.cikis)

        self.setContextMenu(self.menu)

        self.baslangic_ag = psutil.net_io_counters()
        self.baslangic_zamani = time.time()

        self.zamanlayici = QTimer()
        self.zamanlayici.timeout.connect(self.guncelle_func)
        self.zamanlayici.start(2000)

        self.guncelle_func()

    def guncelle_func(self):
        try:
            cpu_kullanimi = psutil.cpu_percent(interval=None)
            ram_kullanimi = psutil.virtual_memory().percent
            disk_kullanimi = psutil.disk_usage('/').percent
            calisma_zamani = self.sure_func()

            anlik_ag = psutil.net_io_counters()
            anlik_zaman = time.time()

            gonder_fark = anlik_ag.bytes_sent - self.baslangic_ag.bytes_sent
            alinan_fark = anlik_ag.bytes_recv - self.baslangic_ag.bytes_recv

            zaman_fark = anlik_zaman - self.baslangic_zamani
            gonderilen_veri = (gonder_fark / zaman_fark) / 1024
            alinan_veri = (alinan_fark / zaman_fark) / 1024

            self.baslangic_ag = anlik_ag
            self.baslangic_zamani = anlik_zaman

            ogeler = (
                f"CPU: {cpu_kullanimi:.1f}%\n"
                f"RAM: {ram_kullanimi:.1f}%\n"
                f"Disk: {disk_kullanimi:.1f}%\n"
                f"Gönderilen Veri: {gonderilen_veri:.2f} KB/s\n"
                f"Alınan Veri: {alinan_veri:.2f} KB/s\n"
                f"Çalışma Süresi: {calisma_zamani}\n"
            )
            self.setToolTip(ogeler)

            self.cpu.setText(f"CPU: {cpu_kullanimi:.1f}%")
            self.ram.setText(f"RAM: {ram_kullanimi:.1f}%")
            self.disk.setText(f"Disk: {disk_kullanimi:.1f}%")
            self.gonderA.setText(f"Gönderilen Veri: {gonderilen_veri:.2f} KB/s")
            self.alinanA.setText(f"Alınan Veri: {alinan_veri:.2f} KB/s")
            self.zaman.setText(f"Çalışma Süresi: {calisma_zamani}")

        except Exception as e:
            enable_error_logging()
            logging.error(f"Bir hata oluştu: {e}")

    def sure_func(self):
        calisma_saniye = int(time.time()) - int(psutil.boot_time())
        gun = calisma_saniye // (24 * 3600)
        calisma_saniye %= (24 * 3600)
        saat = calisma_saniye // 3600
        calisma_saniye %= 3600
        dakika = calisma_saniye // 60
        saniye = calisma_saniye % 60
        return f"{gun} gün {saat} saat {dakika} dakika {saniye} saniye"

    def cpu_ac(self):
        logging.info("CPU sekmesi açıldı.")
        subprocess.run(["gnome-system-monitor"])

    def ram_ac(self):
        logging.info("RAM sekmesi açıldı.")
        subprocess.run(["gnome-system-monitor"])

    def disk_ac(self):
        logging.info("Disk sekmesi açıldı.")
        subprocess.run(["gnome-system-monitor"])

    def cikis_func(self):
        self.temizle_func()
        QApplication.quit()
        sys.exit(0)

    def temizle_func(self):
        if os.path.exists(log_file):
            os.remove(log_file)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    icon = QIcon(QPixmap("/home/kaan/Masaüstü/monL/nazar.png")) 
    tray = SystemMonitor(icon)
    tray.setIcon(icon)
    tray.setToolTip("monA")
    tray.show()

    sys.exit(app.exec_())
