from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, AssginmentViewSet, ExamViewSet, NotesViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet, basename="subjects")
router.register('assginment', AssginmentViewSet, basename="assginment")
router.register('exam', ExamViewSet, basename="exam")
router.register('notes', NotesViewSet, basename="notes")

urlpatterns = router.urls