from rest_framework import routers
from .api import *

router = routers.DefaultRouter()
router.register('api/lists', ListsViewSet, 'lists')
router.register('api/listitem', ListItemViewSet, 'listitem')
router.register('api/group', GroupViewSet, 'group')
router.register('api/category', CategoryViewSet, 'category')

urlpatterns = router.urls

