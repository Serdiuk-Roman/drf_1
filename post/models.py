from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(unique=True, max_length=20)
    description = models.CharField(max_length=250)
    is_active = models.BooleanField(default=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):

    STATUS_DRAFT = 0
    STATUS_PUBLISHED = 100
    STATUS_REJECTED = 20
    STATUS_TRASHED = 25
    STATUS_AUTHORIZED = 80

    STATUSES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_TRASHED, 'Trashed'),
        (STATUS_AUTHORIZED, 'Authorized')
    )

    status = models.SmallIntegerField(choices=STATUSES, default=STATUS_DRAFT)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
