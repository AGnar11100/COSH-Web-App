from django.db import models

class NewsItem(models.Model):
    image_url = models.ImageField(upload_to='imgs')
    title = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} on {self.start_datetime.strftime('%Y-%m-%d')}"
