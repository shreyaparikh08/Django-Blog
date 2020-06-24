from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model): #models.Model means that it's a django model and should be stored in the database

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #links to another model
    title = models.CharField(max_length=200) #define text w/ limited # of characters
    text = models.TextField() #for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    #DateTimeField is for date and time

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

