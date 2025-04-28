from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model): 
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta : 
        abstract = True

class Transaction(BaseModel) : 
    descriptions = models.CharField(max_length=300)
    amount = models.FloatField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank= True)

    def is_negetive(self) : 
        return self.amount < 0
