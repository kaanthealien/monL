# monL [TR]
   "Linux için küçük sistem monitörü"

## Özellikler

- CPU, RAM, Disk kullanımını gösterir
- Gönderilen ve alınan veri hızlarını gösterir (KB/s)
- Sistemin çalışma süresini gösterir
- Görev Yöneticisini açma (Activity Monitor) kısayolları
  
## Kurulum
Uygulamayı çalıştırmak için aşağıdaki adımları takip edin.

### Gereksinimler
- Python 3.9+
- PyQt5
- psutil
- Linux ortamında çalıştırılmak üzere tasarlanmıştır

- ### Gerekli paketleri yükleyin:
```bash
 pip install pyqt5 psutil
```
# Not:
* Programı Linux GNOME ortamında çalıştırıyorsanız, subprocess.run(["gnome-system-monitor"]) kısmı GNOME Sistem Monitörü'nü açar. Başka bir masaüstü ortamı kullanıyorsanız, bu kısmı değiştirebilirsiniz (örneğin, KDE'de ksysguard kullanabilirsiniz).


# monL[EN]
   "A small system monitor for Linux"

   ## Features
- Displays CPU, RAM, and Disk usage
- Shows data transfer rates (KB/s) for sent and received data
- Displays system uptime
- Shortcuts to open the Task Manager (Activity Monitor)

  ## Installation
  Follow these steps to run the application.

  ### Requirements
- Python 3.9+
- PyQt5
- psutil
- Designed to run in a Linux environment

  ### Install the required packages:
  ```bash
     pip install pyqt5 psutil
  ```
  # Note:
* If you are running the program in a GNOME environment on Linux, the subprocess.run(["gnome-system-monitor"]) line opens the GNOME System Monitor. If you are using a different desktop environment, you may need to modify this part (e.g., use ksysguard for KDE).


  # Ekran görüntüleri/Screenshots
  ![Ekran Görüntüsü - 2024-09-19 00-57-14](https://github.com/user-attachments/assets/7169bc8a-8ee3-488c-a6f6-85620b9432b0)
  
  ![Ekran Görüntüsü - 2024-09-19 01-07-50](https://github.com/user-attachments/assets/a10734c1-1d99-4a7b-8e75-3f7795176ea2)


  
   
