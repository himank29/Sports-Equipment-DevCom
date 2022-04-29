from django.contrib import admin

# Register your models here.
from .models import Borrower, Equip, EquipmentTable
admin.site.register(EquipmentTable)
admin.site.register(Borrower)
admin.site.register(Equip)
