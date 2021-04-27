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

    labor_name = models.CharField(max_length=20, verbose_name='領款人姓名',blank=False, null=False)
    labor_ID = models.CharField(max_length=20, verbose_name='身分證字號', blank=False, null=False)
    labor_email = models.EmailField(max_length=60, verbose_name='電子信箱', blank=False, null=False)
    labor_Phone = models.CharField(max_length=15, verbose_name='連絡電話', blank=False, null=False)

    category_choice = models.CharField(max_length=3, verbose_name='申報類別', default='9A',choices=categorychoice)
    member_choice = models.CharField(max_length=3, verbose_name='職業工業會員', default='yes',choices=memberchoice)
    labor_ResidentAddress = models.CharField(max_length=60, verbose_name='戶籍地址', blank=False, null=False)
    
    labor_bank = models.CharField(max_length=20, verbose_name='銀行名(含分行)', blank=False, null=False)
    labor_bankname = models.CharField(max_length=20, verbose_name='銀行戶名', blank=False, null=False)
    labor_bankaccount = models.CharField(max_length=20, verbose_name='銀行帳號', blank=False, null=False)

    project_name = models.CharField(max_length=20, verbose_name='專案名稱', blank=False, null=False)

    price = models.IntegerField(verbose_name='專案金額')
    
    ID_front = models.ImageField(upload_to='image/', verbose_name='身份證正面', blank=False, null=False)
    ID_back = models.ImageField(upload_to='image/', verbose_name='身份證正面', blank=False, null=False)
    bank_cover = models.ImageField(upload_to='image/', verbose_name='銀行存摺封面', blank=False, null=False)
    labor_signature = models.FileField(upload_to='image/',verbose_name='簽名')

    pay_complete = models.BooleanField(blank=True, verbose_name='付款完成', default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.labor_name