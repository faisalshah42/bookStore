from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from api.models import *
from api.serializer import *


# User        
# ------------------------------------------------
class UserView(APIView):

    def get(self, request):
        users_list = User.objects.all()
        serialzer = UserSerializer(users_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = UserSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Genre        
# ------------------------------------------------
class GenreView(APIView):

    def get(self, request):
        genre_list = Genre.objects.all()
        serialzer = GenreSerializer(genre_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = GenreSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Author
# -----------------------------------------------
class AuthorView(APIView):

    def get(self, request):
        author_list = Author.objects.all()
        serialzer = AuthorSerializer(author_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = AuthorSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Books Detials
# -----------------------------------------------
class BookDetailsView(APIView):

    def get(self, request):
        book_details_list = BookDetails.objects.all()
        serialzer = BookDetailsSerializer(book_details_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = BookDetailsSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Books        
# ------------------------------------------------
class BooksView(APIView):

    def get(self, request):
        book_list = Books.objects.all()
        serialzer = BooksSerializer(book_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = BooksSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Comments       
# ------------------------------------------------
class CommentsView(APIView):

    def get(self, request):
        comments_list = Comments.objects.all()
        serialzer = CommentsSerializer(comments_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = CommentsSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Collection     
# ------------------------------------------------
class UserCollectionView(APIView):

    def get(self, request):
        user_collection_list = UserCollection.objects.all()
        serialzer = UserCollectionSerializer(user_collection_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = UserCollectionSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Activity     
# ------------------------------------------------
class UserActivityView(APIView):

    def get(self, request):
        user_activity_list = UserActivity.objects.all()
        serialzer = UserActivitySerializer(user_activity_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = UserActivitySerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Profile    
# ------------------------------------------------
class UserProfileView(APIView):

    def get(self, request):
        user_activity_list = UserProfile.objects.all()
        serialzer = UserProfileSerializer(user_activity_list, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serialzer = UserProfileSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        