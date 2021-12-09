from django.urls import path
from rest_framework import routers

from .views import (
    get_comments,
    post_comments,
    CommentViewSet
)

router = routers.DefaultRouter()
router.register('all', CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    # path('all/', get_comments),
    # path('', post_comments)
]
