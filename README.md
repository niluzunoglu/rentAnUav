# RentUAV

RentUAV, farklı İHA modellerinin kaydını tutabilen ve bu İHA'ların kiralanabilmesine imkan veren bir web projesidir. **Django** ile yazılmıştır. 

Veritabanı olarak **PostgreSQL** kullanılmıştır. 

Arayüz için **Bootstrap**, **Tailwind** ve HTML dosyalarında kod tekrarını önlemek amacıyla **Slippers** kütüphanesi kullanılmıştır.

Üyelik işlemleri için (kullanıcı girişi ve yeni kullanıcı oluşturma) django.contrib.auth kütüphanesi kullanılmıştır. Google ile giriş yapabilme özelliğini uygulamaya ekleyebilmek amacıyla **django.allauth** kütüphanesinin Google eklentisi kullanılmıştır. 

PostgreSQL üzerinde her bir İHA Markası(core.brand) ve İHA Kategorisi(core.category) için birer tablo oluşturulmuştur. İHA Modelleri(core.brandmodel) ve Marka tabloları(core.brand) birbirine bağlanmış ve her bir modelin bir markayla birlikte tutulması sağlanmıştır. 

Her bir İHA'nın kaydında marka, model, kategori bilgilerinin yanı sıra, İHA'yı uygulamaya ekleyen kullanıcının bilgileri, İHA'nın maksimum hızı, kanat açıklığı, uçuş saati, endurance bilgileri gibi bilgiler tutulmaktadır.

Her bir İHA için oluşturulan ve boolean değeri alan isRented alanı ile hangi İHA'nın kiralamak için uygun olup olmadığı belirlenmiştir. Ayrıca core.rentoperations tablosunda her bir kiralama işlemi için o işlemi yapan kullanıcı, işlemin ne zaman yapıldığı ve kullanıcının hangi İHA'yı kiraladığı bilgileri tutulmaktadır. 

Uygulama ve veritabanı üzerinden ekran görüntüleri aşağıdadır:

