from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from .views import (
    BookViewSet,
    GenreViewSet,
    AuthorViewSet,

)
router = DefaultRouter()

router.register(r'book', BookViewSet)
router.register(r'genre', GenreViewSet)
router.register(r'genre', AuthorViewSet)



urlpatterns = [
   path('', include(router.urls))
]
























# urlpatterns = [
#     path('', views.book_list, name='book_list'),
#     path('book/<int:pk>/', views.book_detail, name='book_detail'),
#     path('book/create/', views.book_create, name='book_create'),
#     path('book/<int:pk>/update/', views.book_update, name='book_update'),
#     path('book/<int:pk>/delete/', views.book_delete, name='book_delete'),
# ]



