from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cash)
admin.site.register(Ishchilar)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('id','items_brand','items_name','items_inprice','items_incash_value','items_outprice','items_value','items_color','items_creator',)
admin.site.register(Items,ItemsAdmin)
admin.site.register(Organizationsservice)
class AddClient(admin.ModelAdmin):
    list_display = ('id','client_name','client_phonenumber','ovner', 'client_reception_time')
admin.site.register(Clientadd,AddClient)

admin.site.register(Organizationscategory)
admin.site.register(AddOrganization)
admin.site.register(OrganizationPament)
admin.site.register(CerviseClient)
admin.site.register(Mahsulottopshirish)
