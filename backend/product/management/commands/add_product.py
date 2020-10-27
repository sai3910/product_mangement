from django.core.management.base import BaseCommand, CommandError
from backend.product.models import Product, Keyword

from bs4 import BeautifulSoup as soup
from selenium import webdriver





class Command(BaseCommand):
    help = 'Add products in the database.'

    def handle(self, *args, **options):
        #product url
        url="https://www.flipkart.com/search?q=jewellery&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        site_domain = 'https://www.flipkart.com'
        driver = webdriver.Chrome("/usr/bin/chromedriver")
        driver.get(url)

        html = driver.page_source
        page = soup(html)
        #find through the related class 
        jobs = page.find_all('div',{"class":"IIdQZO _1SSAGr"})

        for job in jobs:
            brand_name = job.find('div',{'class':'_2B_pmu'})
            brand_name = brand_name.text if brand_name else "No Brand"
            product_name = job.find('a',{'class':'_2mylT6'})
            product_name = product_name.text if product_name else "No Name"
            product_offer_price = job.find('div',{'class':'_1vC4OE'})
            product_offer_price = product_offer_price.text if product_offer_price else "N/A"
            product_mrp = job.find('div',{'class':'_3auQ3N'})
            product_mrp = product_mrp.text if product_mrp else "N/A"
            product_link = job.find('a',{'class':'_3dqZjq'})
            product_link = product_link.get('href') if product_link else "N/A"
            product_link = site_domain+product_link
            product_pid = str(product_link.split('pid=')[1][:16])
            product_img = job.find('div',{'class':'_3ZJShS _31bMyl'}).find('img')['src']

            try:
               self.__create_code(brand_name,product_name, product_offer_price,product_mrp,product_link,product_img,product_pid)
            
            except Exception as e:
                raise CommandError(str(e))


        self.stdout.write( 'Products data added successfully' )


    def __create_code(self,brand_name,
        product_name, 
        product_offer_price,
        product_mrp,
        product_link,
        product_img,
        product_pid
        ):
    
        keyword_name = product_name.partition(' ')[0]
        product_obj, is_product_new = Product.objects.get_or_create(product_pid=product_pid)
        key_obj, is_key_new = Keyword.objects.get_or_create(name=keyword_name)
        product_obj.brand_name = brand_name
        product_obj.name = product_name
        product_obj.offer_price = product_offer_price
        product_obj.mrp = product_mrp
        product_obj.product_link = product_link
        product_obj.image_url = product_img

        product_obj.keywords.add(key_obj)

        product_obj.save()
