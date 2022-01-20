# Project KNN 👷🏼‍♂️👷🏼‍♂️
# <a href="https://docs.google.com/presentation/d/1SFpUq5J7zwIf8QWHdqhZPs3aQibQitUH-7Y0SF9IWTc/edit?usp=sharing">Klasifikasi Penyakit Jagung melalui Citra Daun Menggunakan Algoritma KNN🌽</a>

Daftar Anggota :
1. <a href="https://github.com/ppabimanyu" target="_blank">Putra Prassiesa Abimanyu (E41192178)</a>
2. <a href="https://github.com/Bagusbachtiar" target="_blank">Bagus Bachtiar Rizki (E41192340)</a>
3. <a href="https://github.com/arinmitaunziyah" target="_blank">Mita Unziyah Fajrina (E41192433)</a>
4. <a href="https://github.com/devanFerdiansyah" target="_blank">Devan Ferdiansyah (E41191971)</a>
5. <a href="https://github.com/AfrizalSA" target="_blank">Sofyan Arif Af Rizal (E41192160)</a>


## 🤖Starter Guide
## Step 1: Instalasi Miniconda
### **Windows user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Windows 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Ketika ada pilihan `install for`, pilih `Just Me (recommended)`
    - Untuk `Advanced Options`, silahkan centang `Register Anaconda as my default Python 3.7`
    - Tunggu hingga instalasi selesai

- Jalankan `Anaconda Prompt`

### **Mac user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Mac OS X 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.pkg)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.

- Install miniconda
    - Install tanpa mengubah opsi apapun
    - Tunggu hingga instalasi selesai

- Jalankan terminal

### **Linux user**
- Download miniconda untuk Python 3.7
    - Klik link ini untuk download: [Miniconda Linux 64-bit](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh)
    - Note: skip step ini apabila kamu sudah menggunakan Anaconda sebelumnya. Walau demikian, saya akan jelaskan alasan kenapa kamu sebaiknya menggunakan miniconda nanti di course ini.
    
- Install miniconda
    - jalankan terminal
    - Install miniconda menggunakan command berikut
        ```
        bash Miniconda3-latest-Linux-x86_64.sh
        ```
    - Ketik `yes` untuk agree dengan license nya, kemudian `yes` lagi untuk `prepend miniconda install location to PATH`
    - Tunggu hingga instalasi selesai
    
- hanya untuk memastikan, tutup dan buka terminal lagi

## Step 2: Instalasi Environment
- Change directory `cd` ke folder kerja ini
    ```
    cd APP/
    ```
- Jalankan command ini untuk menginstall environment `knn`
    ```
    conda env create -f env_knn.yml
    ```
- activate env -> "conda activate knn"

## 🗂️Dataset Description:<br>
0: Common Rust - 300 images <br>
1: Gray Leaf Spot - 300 images <br>
2: Blight - 300 images <br>
3: Healthy - 300 images

## 📝Note: <br>
This dataset has been made using the popular ✨ <a href="https://www.kaggle.com/abdallahalidev/plantvillage-dataset/version/1" target="blank">PlantVillage</a> ✨ datasets. During the formation of the dataset certain images have been removed which were not found to be useful.

##
## 📈Best Test Score <br>
## 🏆87.9%🥇
<img src="https://github.com/ppabimanyu/Tugas---KNN/blob/master/src/best_score_test.png" width="50%">
<br>

## 🚀Tools
<img src="https://analyticsdrift.com/wp-content/uploads/2021/04/Scikit-learn-free-course.jpg" width="50%">
<img src="https://3.bp.blogspot.com/-yvrV6MUueGg/ToICp0YIDPI/AAAAAAAAADg/SYKg4dWpyC43AAfrDwBTR0VYmYT0QshEgCPcBGAYYCw/s1600/OpenCV_Logo.png" width="50%">


