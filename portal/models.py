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
    is_product = models.BooleanField(default=False)
    is_portrait = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Addons(BaseModel):
    title = models.CharField(max_length=200)
    options = JSONField(default=None, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_product = models.BooleanField(default=False)
    is_portrait = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Instruction(BaseModel):
    job_title = models.CharField(max_length=100)
    # requirements = models.ForeignKey(Requirement, on_delete=models.CASCADE)
    requirement = JSONField(blank=True, null=True, default=None)
    # addons = models.ForeignKey(Addons, on_delete=models.CASCADE)
    addon = JSONField(blank=True, null=True, default=None)


class Order(BaseModel):
    image_path = models.CharField(max_length=200)
    image_quantity = models.IntegerField(null=True, blank=True, default=None)
    IMAGE_TYPE = [(1, 'Image'), (2, 'Portrait/Headshot/Model'), (3, 'Others')]
    image_type = models.IntegerField(choices=IMAGE_TYPE, default=1)
    job_title = models.CharField(max_length=200, null=True, blank=True, default=None)
    need_clipping_path = models.BooleanField(default=False)
    save_metadata = models.BooleanField(default=False)
    requirement = JSONField(blank=True, null=True, default=None)
    addon = JSONField(blank=True, null=True, default=None)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.id)


class Quotation(BaseModel):
    image_path = models.CharField(max_length=200)
    image_quantity = models.IntegerField(null=True, blank=True, default=None)
    IMAGE_TYPE = [(1, 'Image'), (2, 'Portrait/Headshot/Model'), (3, 'Others')]
    image_type = models.IntegerField(choices=IMAGE_TYPE, default=1)
    job_title = models.CharField(max_length=200, null=True, blank=True, default=None)
    need_clipping_path = models.BooleanField(default=False)
    save_metadata = models.BooleanField(default=False)
    requirement = JSONField(blank=True, null=True, default=None)
    addon = JSONField(blank=True, null=True, default=None)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return str(self.id)
