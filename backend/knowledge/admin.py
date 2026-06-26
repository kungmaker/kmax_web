from django.contrib import admin

from knowledge.models import KnowledgeBase


@admin.register(KnowledgeBase)
class KnowledgeBaseAdmin(admin.ModelAdmin):
    list_display = ["name", "status", "document_count", "updated_at"]
    list_filter = ["status"]
    search_fields = ["name", "description"]
