from django.db import models
from django.db.models import JSONField


class BaseModel(models.Model):
    created_by = models.CharField(max_length=100, null=True, blank=True, default=None)
    updated_by = models.CharField(max_length=100, null=True, blank=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Requirement(BaseModel):
    title = models.CharField(max_length=200)
    options = JSONField(null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Addons(BaseModel):
    title = models.CharField(max_length=200)
    options = JSONField(default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Instruction(BaseModel):
    job_title = models.CharField(max_length=100)
    requirements = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    addons = models.ForeignKey(Addons, on_delete=models.CASCADE)


class Order(BaseModel):
    image_path = models.CharField(max_length=200)
    image_quantity = models.IntegerField(null=True, blank=True, default=None)
    IMAGE_TYPE = [(1, 'Image'), (2, 'Portrait/Headshot/Model'), (3, 'Others')]
    image_type = models.IntegerField(choices=IMAGE_TYPE, default=1)
    save_metadata = models.BooleanField(default=False)
    requirements = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    addons = models.ForeignKey(Addons, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
