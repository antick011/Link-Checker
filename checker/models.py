from django.db import models  

class URLCheck(models.Model):
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    is_safe = models.BooleanField(default=True)

    def __str__(self):
        return self.url

