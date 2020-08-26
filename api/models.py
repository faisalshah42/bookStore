from django.db import models


# User        
# ------------------------------------------------
class User(models.Model):

    user_email              = models.EmailField(max_length=100)
    user_member             = models.CharField(max_length=254)

    def __str__(self):
        return self.user_email

# Genre        
# ------------------------------------------------
class Genre(models.Model):

    genre_name              = models.CharField(max_length=500)
    app_id                  = models.BigIntegerField

    def __str__(self):
        return self.genre_name

# Author
# ------------------------------------------------        
class Author(models.Model):

    author_name             = models.CharField(max_length=500)
    book_count              = models.IntegerField
    app_id                  = models.BigIntegerField

    def __str__(self):
        return self.author_name

# Books Detials
# ------------------------------------------------
class BookDetails(models.Model):

    view                    = models.CharField(max_length=100)
    upvote                  = models.CharField(max_length=100)
    downvote                = models.CharField(max_length=100)

# Books
# ------------------------------------------------
class Books(models.Model):

    book_name               = models.CharField(max_length=254)
    book_cover_url          = models.URLField(max_length=500)
    chapters                = models.IntegerField
    book_url                = models.URLField(max_length=500)
    view                    = models.CharField(max_length=100)
    published_time          = models.DateField(auto_now=True)
    user_count              = models.CharField(max_length=100)
    ranking                 = models.CharField(max_length=100)
    state                   = models.CharField(max_length=100)
    book_brief_info         = models.CharField(max_length=100)
    genre_id                = models.ForeignKey(Genre, on_delete=models.CASCADE, default=1)
    author_id               = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    book_details_id         = models.ForeignKey(BookDetails, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.book_name

# Comments
# ------------------------------------------------
class Comments(models.Model):

    comment                 = models.CharField(max_length=500)
    book_id                 = models.ForeignKey(Books, on_delete=models.CASCADE, default=1)
    user_id                 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    app_id                  = models.BigIntegerField

    def __str__(self):
        return self.comment      

# User Collection
# ------------------------------------------------
class UserCollection(models.Model):

    book_id                 = models.ForeignKey(Books, on_delete=models.CASCADE, default=1)
    logged_in_time          = models.TimeField(auto_now=True)

    def __str__(self):
        return self.book_id

# UserActivity
# ------------------------------------------------
class UserActivity(models.Model):

    user_id                 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    book_id                 = models.ForeignKey(Books, on_delete=models.CASCADE, default=1)
    logged_in_time          = models.TimeField(auto_now=True)
    date                    = models.DateField(auto_now=True)
    unlocked_chapter        = models.BooleanField

    def __str__(self):
        return self.book_id

# User Profile
# ------------------------------------------------
class UserProfile(models.Model):

    user_name               = models.CharField(max_length=254)
    coins                   = models.IntegerField
    logged_date             = models.DateField(auto_now=True)
    user_profile            = models.DateField(auto_now=True)
    user_id                 = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    user_activity_id        = models.ForeignKey(UserActivity, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.user_name