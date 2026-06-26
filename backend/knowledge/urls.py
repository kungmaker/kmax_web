from rest_framework.routers import DefaultRouter

from knowledge.views import KnowledgeBaseViewSet

router = DefaultRouter()
router.register("knowledge-bases", KnowledgeBaseViewSet, basename="knowledge-base")

urlpatterns = router.urls
