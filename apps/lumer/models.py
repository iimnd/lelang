from django.utils.translation import gettext_lazy as _
from django.db import models


class Item(models.Model):
    # define status choices/options
    class Location(models.TextChoices):
        JAKARTA = 'jakarta', _('Jakarta')
        MALANG = 'malang', _('Malang')
        JAMBI = 'jambi', _('Jambi')
        BALI = 'bali', _('Bali')

    class Condition(models.TextChoices):
        GOOD = 'good', _('Good')
        WITH_NOTE = 'with_note', _('With Note')


    
    # define columns
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(
        max_length=20,
        choices=Location.choices
    )
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_delete = models.BooleanField(default=False)
    condition = models.CharField(
        max_length=20,
        choices=Condition.choices
    )
    barcode = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        # define table name
        db_table = 'item'