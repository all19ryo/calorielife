from django.contrib import admin
from .models import Calorie,TOP,Choice

# Register your models here.

class CalorieAdmin(admin.ModelAdmin):
    list_display=('name','cal')

class TOPAdmin(admin.ModelAdmin):
    list_display=('date','get_total')
    
    

    def get_total(self, row):
        return ', '.join([x.name for x in row.total_cal.all()])
        # return row.total_cal.objects.all().count()
admin.site.register(TOP,TOPAdmin)
admin.site.register(Calorie,CalorieAdmin)

admin.site.register(Choice)
