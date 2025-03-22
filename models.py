from django.db import models

# Create your models here.
from django.db import models

class Review(models.Model):
    user = models.CharField(max_length=100) 
    rating = models.IntegerField() 
    comment = models.TextField()  
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.user} - {self.rating}"