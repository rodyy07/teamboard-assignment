from django.contrib import admin

from .models import KBEntry, QueryLog

admin.site.register(KBEntry)


# Register your models here.
@admin.register(QueryLog)
class QueryLogAdmin(admin.ModelAdmin):
    list_display = (
        "company",
        "search_term",
        "results_count",
        "queried_at"
    )