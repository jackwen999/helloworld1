from django.db import models

# Create your models here.
class Article(models.Model):
    postid = models.IntegerField()
    title = models.CharField(max_length=200,blank=True)
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    class Meta:
        db_table = "article"

    def __str__(self):
        return self.title