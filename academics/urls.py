from rest_framework.routers import DefaultRouter
from .views import SubjectViewSet, AssignmentViewSet, ExamViewSet, NotesViewSet

router = DefaultRouter()
router.register('subjects', SubjectViewSet, basename="subjects")
router.register('assignment', AssignmentViewSet, basename="assignment")
router.register('exam', ExamViewSet, basename="exam")
router.register('notes', NotesViewSet, basename="notes")

urlpatterns = router.urls