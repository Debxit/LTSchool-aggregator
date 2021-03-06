from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Item(models.Model):
    caption = models.CharField(verbose_name='Caption', db_index=True, max_length=256)
    date = models.DateField(verbose_name='Date')
    source = models.URLField(verbose_name='Source', max_length=512)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE, null=True)
