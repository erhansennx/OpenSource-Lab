# Projeler Navigasyonu

Bu depo, içerisinde iki farklı projeyi barındırmaktadır: Biri Flask ile API kullanarak kullanıcı yönetimi, diğeri ise ülke bayraklarını indiren bir program.

## Proje 1: Flask API Kullanıcı Yönetimi

Bu proje, Flask ve pandas kütüphaneleriyle geliştirilmiş bir API sunar. Kullanıcı yönetimini sağlar ve şu API endpoint'leri bulunur:

- **GET `/users`**: Tüm kullanıcıları listeler ve yaşlarına göre sınıflandırır.
- **POST `/users`**: Yeni bir kullanıcı kaydı ekler.
- **GET `/users/<name>`**: Belirli bir kullanıcı adına göre bilgi getirir.
- **GET `/cities`**: Şehirleri listeler.

### Kullanım

1. `users.csv` dosyası, mevcut kullanıcı verilerini içermelidir.
2. API endpoint'lerine HTTP istekleri göndererek işlemler yapılabilir.

## Proje 2: Flag Downloader

Bu proje, bayrak indirmek için dış bir API'yi kullanan basit bir programdır.

### Kullanım

1. Program başlatıldığında, kullanıcıdan ülke kodu ve bayrak kalitesi istenir.
2. İndirilen bayraklar, `images/<selected_size>px_images` klasörüne kaydedilir.




