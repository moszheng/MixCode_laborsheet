from django import forms
from .models import Post

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {

            'labor_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'姓名'}),
            'labor_ResidentAddress' : forms.TextInput(attrs={'class': 'form-control', 'id': 'ResidentAddress', 'placeholder':'戶籍地址'}),
            'category_choice' : forms.Select(attrs={'class': 'form-select'}),
            'member_choice' : forms.Select(attrs={'class': 'form-select'}),
            'price' : forms.TextInput(attrs={'class': 'form-control', 'id': 'price','placeholder':'給付總額'}),
            'ID_front' : forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile', 'onchange':'loadFile(event)'})
        }
