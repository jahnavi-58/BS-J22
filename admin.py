from django.contrib import admin
from .models import Company, IPOData

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'sector', 'founded_year', 'created_at')
    search_fields = ('name', 'sector')
    list_filter = ('sector', 'founded_year')

@admin.register(IPOData)
class IPODataAdmin(admin.ModelAdmin):
    list_display = ('company', 'status', 'price_band_low', 'price_band_high', 'open_date', 'close_date')
    search_fields = ('company__name', 'status')
    list_filter = ('status', 'open_date', 'close_date')
    readonly_fields = ('created_at', 'updated_at')