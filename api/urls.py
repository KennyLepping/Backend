from rest_framework import routers

from .views import HeroViewset, ContactMessageViewset, ProjectViewset

router = routers.DefaultRouter()
router.register('api/heroes', HeroViewset)
router.register('api/contact-messages', ContactMessageViewset)
router.register('api/projects', ProjectViewset)


urlpatterns = router.urls
