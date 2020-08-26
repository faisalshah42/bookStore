from rest_framework import serializers
from api.models import *

# User        
# ------------------------------------------------
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

# Genre        
# ------------------------------------------------
class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'

# Author
# ------------------------------------------------
class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'

# Books Detials
# ------------------------------------------------
class BookDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookDetails
        fields = '__all__'

# Books
# ------------------------------------------------
class BooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Books
        fields = '__all__'

# Comments
# ------------------------------------------------
class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = '__all__'

# User Collection
# ------------------------------------------------
class UserCollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCollection
        fields = '__all__'

# UserActivity
# ------------------------------------------------
class UserActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = UserActivity
        fields = '__all__'

# User Profile
# ------------------------------------------------
class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'






