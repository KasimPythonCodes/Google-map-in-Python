from django.contrib import admin
from .models import Rentall
# Register your models here.
class AdminRental(admin.ModelAdmin):
   pass
 

admin.site.register(Rentall)
