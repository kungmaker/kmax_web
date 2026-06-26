from rest_framework import serializers

from knowledge.models import KnowledgeBase


class KnowledgeBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KnowledgeBase
        fields = [
            "id",
            "name",
            "description",
            "status",
            "document_count",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "document_count", "created_at", "updated_at"]

    def validate_name(self, value: str) -> str:
        name = value.strip()
        if not name:
            raise serializers.ValidationError("Knowledge base name cannot be empty.")
        return name
