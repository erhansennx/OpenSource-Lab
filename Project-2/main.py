from PIL import Image
import requests
from io import BytesIO
import os

country_code = input("Ülke kodunu girin (Örn: US, TR, DE): ").upper()

selected_size = input("Resim kalitesini seçin (16/24/32/48/64): ")

flag_url = f"https://flagsapi.com/{country_code}/flat/{selected_size}.png"

response = requests.get(flag_url)

if response.status_code == 200:
    img = Image.open(BytesIO(response.content))

    folder_path = f"images/{selected_size}px_images"
    os.makedirs(folder_path, exist_ok=True)

    file_path = f"{folder_path}/{country_code}_flag_{selected_size}px.png"
    img.save(file_path)

    print(f"{country_code} bayrağı {selected_size}px çözünürlükle '{folder_path}' klasörüne kaydedildi.")

else:
    print("Bayrak bulunamadı veya bir hata oluştu.")

