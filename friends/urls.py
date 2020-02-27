from django.urls import path
from friends import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('friends/<int:id>/',views.friend_list),
    path('users/',views.user_list),
    path('users/<int:id>/',views.user),
]

urlpatterns = format_suffix_patterns(urlpatterns)
