from django import forms
from .models import Post

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {

            'labor_name' : forms.TextInput(attrs={'placeholder':'姓名'}),
            'labor_ID' : forms.TextInput(attrs={'placeholder':'身分證字號'}),
            'labor_email' : forms.TextInput(attrs={'placeholder':'電子信箱'}),
            'labor_Phone' : forms.TextInput(attrs={'placeholder':'連絡電話'}),
            'labor_ResidentAddress' : forms.TextInput(attrs={'placeholder':'戶籍地址'}),
            
            'labor_bank' : forms.TextInput(attrs={'placeholder':'銀行名(含分行)'}),
            'labor_bankname' : forms.TextInput(attrs={'placeholder':'銀行戶名'}),
            'labor_bankaccount' : forms.TextInput(attrs={'placeholder':'銀行帳號'}),
            'bank_cover' : forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile', 'onchange':'loadFile_bank(event)'}),

            'category_choice' : forms.Select(attrs={'class': 'form-select'}),
            'member_choice' : forms.Select(attrs={'class': 'form-select'}),
            'price' : forms.TextInput(attrs={'placeholder':'實領金額'}),
            'ID_front' : forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile', 'onchange':'loadFile_front(event)'}),
            'ID_back' : forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile', 'onchange':'loadFile_back(event)'}),
        }
