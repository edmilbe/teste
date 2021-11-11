from django.contrib import admin
# Register your models here.
from epardal.models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'color','height')