from django.db import models

categorychoice = [
    ('9A', '9A 執行業務所得'),
    ('9B', '9B 稿費'),
]
memberchoice = [
    ('yes', '是'),
    ('no', '否'),
]

class Post(models.Model):

    labor_name = models.CharField(max_length=20, blank=False, null=False)
    labor_ID = models.CharField(max_length=20, blank=False, null=False)
    labor_email = models.CharField(max_length=20, blank=False, null=False)
    labor_Phone = models.CharField(max_length=20, blank=False, null=False)

    category_choice = models.CharField(max_length=3, choices=categorychoice)
    member_choice = models.CharField(max_length=3, choices=memberchoice)
    
    labor_ResidentAddress = models.CharField(max_length=60, blank=False, null=False)
    labor_CurrentAddress = models.CharField(max_length=60, blank=False, null=False)
    labor_bank = models.CharField(max_length=20, blank=False, null=False)
    labor_bankname = models.CharField(max_length=20, blank=False, null=False)
    labor_bankaccount = models.CharField(max_length=20, blank=False, null=False)

    project_name = models.CharField(max_length=20, blank=False, null=False)

    price = models.IntegerField()
    
    ID_front = models.ImageField(upload_to='image/', blank=False, null=False)
    ID_back = models.ImageField(upload_to='image/', blank=False, null=False)
    bank_cover = models.ImageField(upload_to='image/', blank=False, null=False)
    labor_signature = models.ImageField(upload_to='image/', blank=False, null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.labor_name