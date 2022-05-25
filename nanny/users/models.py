
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from cities_light.models import City
from cities_light.models import Region 
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import User



# Create your models here.
class NannyProfile(models.Model):
  RELIGION_CATEGORY=(
    ('Christian', 'Christian'),
    ('Islam', 'Islam'),
    ('Hindu', 'Hindu'),
  )
  LEVEL_OF_EDUCATION=(
    ('Bachelors', 'Bachelors'),
    ('HighSchool', 'HighSchool'),
    ('Primary', 'Primary'),
  )
  ETHINICITY=(
    ('Luhya', 'Luhya'),
    ('Luo', 'Luo'),
    ('Kisii', 'Kisii'),
  )
  nanny_user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
  phone_number=models.CharField(max_length=15, null=False)
  state=models.ForeignKey(Region, default=1, on_delete=models.CASCADE)
  city=ChainedForeignKey(City, chained_field="state", chained_model_field="region", default='1')
  religion=models.CharField(max_length=10, choices=RELIGION_CATEGORY)
  education=models.CharField(max_length=10, choices=LEVEL_OF_EDUCATION)
  ethinicity=models.CharField(max_length=10, choices=ETHINICITY)
  date_of_birth=models.DateField(null=True)
  image=models.ImageField(default="default.png", upload_to='media/')

def _str_(self):
  return f'{self.nanny_user.username}-NannyProfile'




  
