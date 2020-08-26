from django.contrib import admin
from .models import Books, Author, Genre, User, UserActivity, UserCollection, UserProfile, BookDetails, Comments
# Register your models here.

myModels = [Books, Author, Genre, User, UserActivity, UserCollection, UserProfile, BookDetails, Comments]

admin.site.register(myModels)