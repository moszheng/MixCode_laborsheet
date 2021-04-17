from django import forms
from .models import Post

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {

            'labor_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'姓名'}),
            
            'ID_front' : forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile' })
        }
