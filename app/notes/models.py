from django.db import models
from django.contrib.auth import get_user_model


class Note(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    class Meta:
        db_table = 'notes'
        ordering = ('-created_at', )
