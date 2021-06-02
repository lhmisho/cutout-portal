from django.db import models
from django.db.models import JSONField
# Create your models here.


class BaseModel(models.Model):
    created_by = models.CharField(max_length=100, null=True)
    updated_by = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Requirement(BaseModel):
    title = models.CharField(max_length=200)
    options = JSONField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Addons(BaseModel):
    title = models.CharField(max_length=200)
    options = JSONField(default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
