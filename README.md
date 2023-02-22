# RentUAV

RentUAV, farklı İHA modellerinin kaydını tutabilen ve bu İHA'ların kiralanabilmesine imkan veren bir web projesidir. **Django** ile yazılmıştır. 

Veritabanı olarak **PostgreSQL** kullanılmıştır. 

Arayüz için **Bootstrap**, **Tailwind** ve HTML dosyalarında kod tekrarını önlemek amacıyla **Slippers** kütüphanesi kullanılmıştır.


![7](https://user-images.githubusercontent.com/47059818/220786579-aff40dea-66dc-4840-b91b-eaa144806cde.PNG) 

Üyelik işlemleri için (kullanıcı girişi ve yeni kullanıcı oluşturma) django.contrib.auth kütüphanesi kullanılmıştır. Google ile giriş yapabilme özelliğini uygulamaya ekleyebilmek amacıyla **django.allauth** kütüphanesinin Google eklentisi kullanılmıştır. 


![resim_2023-02-23_022615518](https://user-images.githubusercontent.com/47059818/220786424-65108495-77a3-4b9e-85c1-b19c623f701a.png)

PostgreSQL üzerinde her bir İHA Markası(core.brand) ve İHA Kategorisi(core.category) için birer tablo oluşturulmuştur. İHA Modelleri(core.brandmodel) ve Marka tabloları(core.brand) birbirine bağlanmış ve her bir modelin bir markayla birlikte tutulması sağlanmıştır. 

Her bir İHA'nın kaydında marka, model, kategori bilgilerinin yanı sıra, İHA'yı uygulamaya ekleyen kullanıcının bilgileri, İHA'nın maksimum hızı, kanat açıklığı, uçuş saati, endurance bilgileri gibi bilgiler tutulmaktadır.

Her bir İHA için oluşturulan ve boolean değeri alan isRented alanı ile hangi İHA'nın kiralamak için uygun olup olmadığı belirlenmiştir. Ayrıca core.rentoperations tablosunda her bir kiralama işlemi için o işlemi yapan kullanıcı, işlemin ne zaman yapıldığı ve kullanıcının hangi İHA'yı kiraladığı bilgileri tutulmaktadır. 

Uygulama ve veritabanı üzerinden ekran görüntüleri aşağıdadır:


![1](https://user-images.githubusercontent.com/47059818/220786507-88800ae1-8cc4-4087-9c8e-433193f77b19.PNG)

![2](https://user-images.githubusercontent.com/47059818/220786566-00e700b7-2080-4133-b1c6-94dae3e5206e.PNG)
![3](https://user-images.githubusercontent.com/47059818/220786568-9e03a1d5-dc0a-4080-a47e-e70616ac7cea.PNG)
![4](https://user-images.githubusercontent.com/47059818/220786571-1ea93df8-c9ab-4a49-b099-5c253de80db2.PNG)
![5](https://user-images.githubusercontent.com/47059818/220786572-36964485-0175-49dc-913e-0a13879ac026.PNG)
![6](https://user-images.githubusercontent.com/47059818/220786574-b71e285a-65ab-47c1-aa90-977a16ca3d06.PNG)


