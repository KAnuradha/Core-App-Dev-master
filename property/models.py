from django.db import models
import uuid

# Create your models here.
HOME_TYPE = (
    ('present type', 'present type'),
    ('past type', 'pasttype')
)

class Property_details(models.Model):
	property_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	property_title = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	city = models.CharField(max_length=20)
	state = models.CharField(max_length=20)
	zip_code = models.IntegerField()
	home_type = models.CharField(max_length=20,choices = HOME_TYPE)
	beds = models.IntegerField()
	baths = models.IntegerField()
	rooms = models.IntegerField()
	property_size = models.CharField(max_length=20)
	description = models.TextField()
	other_features = models.TextField()