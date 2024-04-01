from django.db import models

# Create your models here.
class Client(models.Model):
    nom = models.CharField(max_length=200, null=False)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nom