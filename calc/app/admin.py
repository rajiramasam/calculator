from django.contrib import admin
from .models import CalculationHistory

@admin.register(CalculationHistory)
class CalculationHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'expression', 'result', 'timestamp')
