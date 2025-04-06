from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from country import views

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('country/', views.CountryList.as_view(), name='country-list'),
    path('country/<int:pk>/', views.CountryDetail.as_view(), name='country-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

  ])


