from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('painting', 'Painting'),
        ('drawing', 'Drawing'),
        ('digital_art', 'Digital Art'),
        ('sculptures', 'Sculptures'),
        ('pottery', 'Pottery'),
        ('textile_art', 'Textile Art'),
        ('jewellery_crafting', 'Jewellery Crafting'),
        ('fashion_designing', 'Fashion Designing'),
        ('others', 'Others'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/',blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES,default='others')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.blog_post.title}'


    def __str__(self):
        return f"{self.user.username} liked {self.post.title}"
    

