from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
    )

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet
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
class BookDetailsView(RetrieveAPIView):

    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer
    lookup_field = 'pk'

    def post(self, request):
        serialzer = BookDetailsSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return JsonResponse(serialzer.data, status = status.HTTP_201_CREATED)
        return JsonResponse(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)

# Books        
# ------------------------------------------------
class BooksView(ListAPIView):

    queryset = Books.objects.all().order_by('id')
    serializer_class = BooksSerializer
    pagination_class = LimitOffsetPagination
        
# Books Search by Book Name || Author Name       
# ------------------------------------------------
class BooksSearchView(ListAPIView):

    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [SearchFilter]
    search_fields = ['book_name', 'author__author_name']

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

        
        