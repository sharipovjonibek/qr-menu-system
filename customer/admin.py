from django.contrib import admin
from .models import Table, Category, MenuItem
# Register your models here.

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    readonly_fields = ("qr_code","token")

admin.site.register(Category)
admin.site.register(MenuItem)