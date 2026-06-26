from django.db.models import QuerySet
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from knowledge.models import KnowledgeBase
from knowledge.serializers import KnowledgeBaseSerializer


class KnowledgeBaseViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = KnowledgeBaseSerializer

    def get_queryset(self) -> QuerySet[KnowledgeBase]:
        queryset = KnowledgeBase.objects.all()
        status = self.request.query_params.get("status")
        search = self.request.query_params.get("search")

        if status:
            queryset = queryset.filter(status=status)
        if search:
            queryset = queryset.filter(name__icontains=search.strip())

        return queryset
