from django.db import models
# In Django, the User model is a pre-built model that represents a user account.
# It contains fields such as username, email, password, and more, which are commonly
# used to manage user authentication and access control in web applications.
from django.contrib.auth.models import User
# CloudinaryField is a special field provided by the "django-cloudinary-storage"
# library. By using CloudinaryField, you can easily handle image and media uploads,
# transformations, and optimizations without the need for additional server-side code.
from cloudinary.models import CloudinaryField

# STATUS variable is used to define a tuple of choices for the status of a model instance
# These status choices can be used as options for a field in your model to represent the
# state of the instances. For example, if you have a BlogPost model, you might have a
# field like status = models.IntegerField(choices=STATUS, default=0) to represent the
# status of each blog post.
STATUS = ((0, "Черновик"), (1, "Опубликовано"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, choices=STATUS)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.body} by {self.name}'
