# Flag Downloader

`flagsapi.com` üzerinden belirli bir ülkenin bayrağını seçilen bir çözünürlükte indirmenizi sağlar. Kullanıcıdan ülke kodunu (`US`, `TR`, `DE` gibi) ve istenilen çözünürlük boyutunu (`16`, `24`, `32`, `48`, `64` gibi) girmesini bekler.

## Kullanımı

1. **Kütüphaneleri Yükleyin**

    ```bash
    pip install requests pillow
    ```

2. **Kodu Çalıştırmak İçin**

    ```bash
    python3 main.py
    ```

3. **Ülke Kodu ve Boyut Seçimi**

    Program çalıştırıldığında, istenen ülke kodunu ve bayrağın çözünürlük boyutunu girmeniz istenecek.

    Örnek:

    ```
    Ülke kodunu girin (Örn: US, TR, DE): TR
    Resim kalitesini seçin (16/24/32/48/64): 32
    ```

4. **Kaydedilen Bayrak**

    Seçilen çözünürlükteki bayrak, `images/selected_sizepx_images/TR_flag_selected_sizepx.png` konumunda kaydedilecek.
   
   ```
   
   Örneğin, `images/32px_images/TR_flag_32px.png`
   
   ```
