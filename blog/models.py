from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

"""
一個文章有多個 tag，一對多的關係
"""
class Tag(models.Model):
    contact = models.ForeignKey(Post,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name