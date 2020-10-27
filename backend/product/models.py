from django.db import models
from django.core.files import File

from urllib.request import urlopen
from tempfile import NamedTemporaryFile

class Keyword(models.Model):
	name = models.CharField(max_length = 20)

	def __str__(self):
		return self.name


class Product(models.Model):
	product_pid = models.CharField(max_length=20,unique=True)
	brand_name = models.CharField(max_length=50)
	name = models.CharField(max_length=120)
	offer_price=models.CharField(max_length=120)
	mrp=models.CharField(max_length=120)
	product_link=models.URLField()
	image_file=models.ImageField(upload_to='products', null=True)
	image_url = models.URLField()
	keywords = models.ManyToManyField(Keyword, blank=True, related_name='products')

	def save(self, *args, **kwargs):
		if self.image_url and not self.image_file:
			img_temp = NamedTemporaryFile(delete=True)
			img_temp.write(urlopen(self.image_url).read())
			img_temp.flush()
			self.image_file.save(f"image_{self.pk}", File(img_temp))
		super(Product, self).save(*args, **kwargs)


	def __str__(self):
		return self.name



