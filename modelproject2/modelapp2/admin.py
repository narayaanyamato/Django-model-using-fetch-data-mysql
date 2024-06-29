from django.contrib import admin
from modelapp2.models import Fruits 
class FruitsAdmin(admin.ModelAdmin):
    list_display=['fno','fname','fprice','fseller','fcate']

admin.site.register(Fruits,FruitsAdmin)    
