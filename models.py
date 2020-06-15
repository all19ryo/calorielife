from django.db import models
from datetime import datetime 
from django.db.models import Avg,Sum



class Choice(models.Model):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name


class Calorie(models.Model):
    class Meta:
        db_table="Calorie"
        verbose_name="商品管理"
        verbose_name_plural="商品管理"

    name=models.CharField(verbose_name="商品名",max_length=50,unique=True)
    category = models.ForeignKey(Choice, on_delete = models.PROTECT, verbose_name="ジャンル")
    cal=models.IntegerField(verbose_name="カロリー",help_text="単位はkcal(半角数字のみ可)")

    # def cals(self):
    #     Calorie.objects.all().aggregate(Avg('cal'))


    def __str__(self):
        return self.name
        # return Calorie.objects.all().count()



class TOP(models.Model):
    class Meta:
        db_table="TOP"
        verbose_name="データ"
        # verbose_name_plural="トップ表示"

    date=models.DateField(verbose_name="日付",default=datetime.now,unique=True)
    total_cal=models.ManyToManyField(Calorie, related_name='計カロリー',verbose_name="飲食したもの")
    
    def __str__(self):
        return str(self.date)
    # def cals(self):
    #     return "\n".join([p.total_cal for p in self.total_cal.all()])
    
    # def cals(self):
    #     return total_cal.objects.all().count()
    # def __str__(self):
    #     return str(self.date)