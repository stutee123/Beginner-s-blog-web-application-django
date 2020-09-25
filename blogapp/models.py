from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Blog(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE, related_name="blogs",default=False)
    body=models.TextField()
    created_at=models.DateTimeField(default=datetime.now, blank=True)
    status=models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Blogs"


