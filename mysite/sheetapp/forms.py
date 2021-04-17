from django import forms
from .models import Post

class UploadModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widget = {

            'labor_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'test'}),
            
            #'labor_ID' : forms.TextInput(attrs={'class': 'form-control',}),
            #'ID_front' : forms.FileInput(attrs={'class':'form-control', 'type':'file', 'id':'formFile' })
        }
