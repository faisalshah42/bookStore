from django.urls import path
from .views import *

urlpatterns = [
    path('api/login/', UserView.as_view()),
    path('api/genres/', GenreView.as_view()),
    path('api/authors/', AuthorView.as_view()),
    path('api/bookDetails/<int:pk>', BookDetailsView.as_view()),
    path('api/books/', BooksView.as_view()),
    path('api/comments/', CommentsView.as_view()),
    path('api/userCollection/', UserCollectionView.as_view()),
    path('api/userActivity/', UserActivityView.as_view()),
    path('api/userProfile/', UserProfileView.as_view()),

    # Book Search by book name and by book author
    path('api/search/', BooksSearchView.as_view()),
]