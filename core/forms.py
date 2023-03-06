from django import forms
from .models import  Ishchilar, Items,  Clientadd, CerviseClient,Mahsulottopshirish


class ClientsForm(forms.ModelForm):

    class Meta:
        model = Clientadd
        fields = '__all__'
        widgets ={
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'ovner': forms.Select(attrs={'class': 'form-control custom-select'})
            # 'client_reception_time': forms.TextInput()
        }

class CerviseClientForm(forms.ModelForm):
    class Meta:
        model = CerviseClient
        fields = '__all__'
        widgets = {
            'client_name': forms.Select(attrs={'class': 'form-control custom-select'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_value': forms.NumberInput(attrs={'class': 'form-control number'}),
            'product_color': forms.TextInput(attrs={'class': 'form-control'}),
            'service_catetegory': forms.Select(attrs={'class': 'form-control custom-select'}),
            #'product_defective': forms.TextInput(attrs={'class':'form-control'}),
            #'product_repaired' : forms.TextInput(attrs={'class':'form-control'}),
            #'produtct_not_repaired': forms.TextInput(attrs={'class':'form-control'}),
            #'clien_service_price' : forms.NumberInput(attrs={'class':'form-control'}),
            'product_repairman' :   forms.Select(attrs={'class':'form-control custom-select'}),
        }

class Cerviceendform(forms.ModelForm):
    class Meta:
        model = Mahsulottopshirish
        fields = '__all__'
        widgets = {
            'product_defective': forms.TextInput(attrs={'class':'form-control'}),
            'product_repaired' : forms.TextInput(attrs={'class':'form-control'}),
            'produtct_not_repaired': forms.TextInput(attrs={'class':'form-control'}),
            'clien_service_price' : forms.TextInput(attrs={'class':'form-control'}),
            'cervice_item_price' : forms.TextInput(attrs={'class':'form-control'}),
            'topshiruvchi': forms.Select(attrs={'class':'form-control custom-select'}),
        }

class AddWorkerForm(forms.ModelForm):
    
    class Meta:
        model = Ishchilar
        fields = '__all__'
        # widgets = {
        #     'worker_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'worker_surname': forms.TextInput(attrs={'class': 'form-control'}),
        #     'worker_age' : forms.NumberInput(attrs={'class':'form-control'}),
        #     'worker_stage' :forms.NumberInput(attrs={'class':'form-control'}),
        # }
class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'
        # widgets = {
            
        #     'items_name': forms.TextInput(attrs={'class': 'form-control'}),
        #     'items_inprice': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'items_incash_value': forms.Select(attrs={'class': 'form-control select2'}),
        #     'items_outprice': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'items_value': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'items_color': forms.TextInput(attrs={'class': 'form-control'}),
        #     'items_creator': forms.Select(attrs={'class': 'form-control select2'}),
        #     'items_brand':forms.TextInput(attrs={'class':'form-control'}),

        # }