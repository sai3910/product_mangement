from django.contrib import admin
from .models import Product, Keyword

class ProductAdmin(admin.ModelAdmin):  
	list_display = ('product_pid','brand_name','name', 'offer_price', 'mrp', 'image_url','get_keys') 

	def get_keys(self, obj):
		return "\n".join([p.name for p in obj.keywords.all()])


admin.site.register(Product, ProductAdmin)
admin.site.register(Keyword)