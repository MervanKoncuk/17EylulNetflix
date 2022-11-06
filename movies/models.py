from django.db import models
import uuid
# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim

class Movie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to='filmler/')
    video = models.FileField(upload_to='filmler/', null=True)
    def __str__(self):
        return self.isim
