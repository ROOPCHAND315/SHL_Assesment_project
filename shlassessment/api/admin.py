from django.contrib import admin
from .models import shlModel
@admin.register(shlModel)
class shlAdmin(admin.ModelAdmin):
    list_display=['id','title','technologies','frontend','backend','databases','infrastructure']



# Register your models here.
