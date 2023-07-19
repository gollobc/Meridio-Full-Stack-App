from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('market/', views.market_index, name='index'),
    path('market/<int:post_id>/', views.market_detail, name='detail'),
    path('market/create/', views.PostCreate.as_view(), name='post_create'),
    path('market/<int:pk>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('market/<int:pk>/delete', views.PostDelete.as_view(), name='post_delete'),
    path('market/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),

]