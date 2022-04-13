from django.db                  import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    gender     = models.CharField(max_length=2, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'


