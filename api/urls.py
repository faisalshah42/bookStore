from django.urls import path
from .views import *

urlpatterns = [
    path('api/users/', UserView.as_view()),
    path('api/genres/', GenreView.as_view()),
    path('api/authors/', AuthorView.as_view()),
    path('api/bookDetails/', BookDetailsView.as_view()),
    path('api/books/', BooksView.as_view()),
    path('api/comments/', CommentsView.as_view()),
    path('api/userCollection/', UserCollectionView.as_view()),
    path('api/userActivity/', UserActivityView.as_view()),
    path('api/userProfile/', UserProfileView.as_view()),
]