from django.contrib import admin
from .models import avtorModel


# Register your models here.

class avtorAdmin(admin.ModelAdmin):
    list_display = ['kitob_nomi', 'avtori', 'yili','sifati']
    search_fields = ['avtori', 'kitob_nomi']


admin.site.register(avtorModel)
