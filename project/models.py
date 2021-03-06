from django.db import models
# from django.contrib.auth.models import User


class TodoModel(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    task = models.CharField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    timestamps = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-timestamps']


    def __str__(self):
        return self.task