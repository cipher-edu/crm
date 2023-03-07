from django.db import models
from django.utils import timezone
from django.urls import reverse
import uuid
#savdo puli naq clik kuchirish

class Cash(models.Model):
    cash_value = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'To\'lov turui'
        verbose_name_plural = 'To\'lov turi'

    def __str__(self):
        return self.cash_value
# add workers model

class Ishchilar(models.Model):
    worker_name = models.CharField(max_length=45, verbose_name="Ismi")
    worker_surname = models.CharField(max_length=45, verbose_name="Familiya")
    worker_age = models.IntegerField(verbose_name="Yoshi")
    # worker_location = models.TextField(max_length=45, )
    # worker_brithday = models.DateField()
    worker_stage = models.IntegerField()
    

    class Meta:
        verbose_name = 'ishchilar nomi'
        verbose_name_plural = 'ishchilar nomi'
    def __str__(self):
        return self.worker_name
    
    #end worker model

# mahsulot yaratish model start

class Items(models.Model):
    items_brand = models.CharField(max_length=150, verbose_name="Brend nomi")
    items_name = models.CharField(max_length=150, verbose_name="Tovar nomi")
    items_inprice = models.IntegerField(verbose_name="Tovar narxi")
    items_incash_value = models.ForeignKey(Cash, on_delete=models.CASCADE, verbose_name="To'lov turi") 
    items_outprice = models.IntegerField(verbose_name="Sotilish narxi")
    items_value = models.IntegerField(verbose_name="Qiymati (dona)")
    items_color = models.CharField(max_length=50, verbose_name="Tovar rangi")
    items_creator = models.ForeignKey(Ishchilar, on_delete=models.CASCADE, default=1, verbose_name="Maxsulot qo'shuvchi xodim")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    class Meta:
        verbose_name = 'Mahsulot turlari'
        verbose_name_plural = 'Mahsulot turlarini yaratish'
    def __str__(self):
        return self.items_name

#end mahsulot qushish model

#xizmat turini shaklantirish
class Organizationsservice(models.Model):
    service_catetegory = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Xizmat turlari'
        verbose_name_plural = 'Xizmat turlari'
    def __str__(self):
        return self.service_catetegory
    
#ximat turlari end

#client bazni shakllantirish 
class Clientadd(models.Model):
    client_name = models.CharField(max_length=50, unique=True)
    client_phonenumber = models.IntegerField(unique=True)
    ovner = models.ForeignKey(Ishchilar, on_delete=models.CASCADE )
    client_reception_time = models.DateField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        verbose_name = 'Klient yaratish'
        verbose_name_plural = 'Klient yaratish'
    def __str__(self):
        return self.client_name
    
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Clientadd, self).save(*args, **kwargs)
    
    def kurish(self):
        return reverse('client', kwargs={'client_id':self.pk})

# klient baza model tugatish
#clientga servis xizmat ko'rsatish
class CerviseClient(models.Model):
    client_name = models.ForeignKey(Clientadd, on_delete=models.CASCADE, verbose_name="Mijozni tanlang")
    product_name = models.CharField(max_length=150, verbose_name="Maxsulot nomini kiriting")
    product_value = models.IntegerField(verbose_name="Maxsulot qiymatini kiriting")
    product_color = models.CharField(max_length=35, verbose_name="Maxsulot rangini kiriting")
    service_catetegory = models.ForeignKey(Organizationsservice, on_delete=models.CASCADE, verbose_name="Service xizmat turi"  )
    # product_defective = models.CharField(max_length=150, verbose_name="Maxsulot aybi")
    # product_repaired = models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlar")
    # produtct_not_repaired = models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlamaslik")
    # clien_service_price = models.IntegerField(verbose_name="Service narxi")
    # client_installed_product = models.ForeignKey(Items, on_delete=models.CASCADE, default=1)
    # service_time = models.DateTimeField()
    product_repairman = models.ForeignKey(Ishchilar,on_delete=models.CASCADE, verbose_name="Maxsulotni topshiruvchi" )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class Meta:
        verbose_name = 'Service xizmat ko\'rsatish'
        verbose_name_plural = 'Service xizmat ko\'rsatish'

    def __str__(self):
        return self.product_name
    
    def detail(self):
        return reverse('client', kwargs={'detail_id':self.pk})
#mahsulotni topshirish
class Mahsulottopshirish(models.Model):
    product_defective = models.CharField(max_length=150, verbose_name="Maxsulot aybi")
    product_repaired = models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlash")
    produtct_not_repaired = models.CharField(max_length=150, verbose_name="Maxsulotni ta'mirlamaslik")
    cervice_item_price = models.IntegerField(verbose_name="Ishlatilingan texnika narxi")
    clien_service_price = models.IntegerField(verbose_name="Service narxi")
    topshiruvchi = models.ForeignKey(Ishchilar, on_delete=models.CASCADE, verbose_name='xizmatni yakunlvchi')

    class Meta:
        verbose_name = 'Service xizmat yakunlash'
        verbose_name_plural = 'Service xizmat yakunlash'

    def __str__(self):
        return self.product_defective
# ishhonlarni kategoriya bo'yicha shakllantirish
class Organizationscategory(models.Model):
    categoryname = models.CharField(max_length=100)
    descriptions = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'kategoriyalar ro\'yxati'
    def __str__(self):
        return self.categoryname
# ishhonlarga hizmat ko'rsatish
class AddOrganization(models.Model):
    category = models.ForeignKey(Organizationscategory, on_delete=models.CASCADE, default=1)
    servise_name = models.ForeignKey(Clientadd, on_delete=models.CASCADE)
    service_soni = models.IntegerField()
    service_narxi= models.IntegerField()
    xizmat_haqida = models.TextField()
    service_date = models.DateField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Ishhona'
        verbose_name_plural = 'Ishhonalarga xizmat qo\'shish'

    def __str__(self):
        return self.xizmat_haqida

#pul kirim chiqim
class OrganizationPament(models.Model):
    category = models.ForeignKey(Organizationscategory, on_delete=models.CASCADE, default=1)
    payment_organizations = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True)
    payment_coment = models.TextField()

    class Meta:
        verbose_name = 'Tashkilot to\'lovi'
        verbose_name_plural = 'Tashkilotlar to\'lovi'
    def __str__(self):
        return self.payment_coment
#ishhona categoriya end

