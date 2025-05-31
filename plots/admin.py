from django.contrib import admin
from .models import Plot

@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('plot_id', 'plot_name', 'plot_location', 'plot_size', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('plot_id', 'plot_name', 'plot_location')
    readonly_fields = ('plot_id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {'fields': ('plot_id',)}),
        ('Plot Information', {'fields': ('plot_name', 'plot_location', 'plot_size')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    ) 