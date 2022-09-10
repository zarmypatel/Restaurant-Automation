
from django.db import models
# Create your models here.


#chef
class Chef(models.Model):
	chef_id=models.AutoField(primary_key=True)
	chef_name = models.CharField(max_length=100,blank=False,null=False)
	chef_email = models.EmailField(help_text='Your Email ID')
	chef_mobileNo = models.CharField(help_text='Contact phone number',max_length=10,)
	chef_password=models.CharField(max_length=15)

	class Meta:
		db_table='Chef'

#Customer
class Customer(models.Model):
	customer_id=models.AutoField(primary_key=True)
	customer_email = models.EmailField(default="",blank=True,null=True)
	customer_mobileNo = models.CharField(help_text='Contact phone number',max_length=10)
	customer_name = models.CharField(max_length=100,blank=False,null=False)
	
	class Meta:
		db_table='customer'
#MenuItems
class MenuItem(models.Model):
	item_id = models.AutoField(primary_key=True)
	item_name = models.CharField(max_length=100)
	item_price = models.FloatField(default=0)
	item_description = models.TextField(max_length=100)
	item_category = models.CharField(max_length=100)
	item_subcategory = models.CharField(max_length=100)
	
	class Meta:
		db_table='menuitem'
#Order
class Order(models.Model):
	order_id = models.AutoField(primary_key=True)
	order_no = models.IntegerField(null=False)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	menuitem = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
	item_quantity = models.IntegerField(default=0)
	date_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table='order'
#Bill
class Bill(models.Model):
	bill_id = models.AutoField(primary_key=True)
	customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	amount = models.FloatField(default=0)
	date_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table='bill'
#CurrentOrder
class CurrentOrder(models.Model):
	order_no =models.IntegerField(null=False)
	menu_item = models.CharField(max_length=100)
	item_quantity = models.IntegerField(default=0)
	customer_id = models.IntegerField(default=0)
	order_id = models.IntegerField(default=0)
	class Meta:
		db_table='currentorder'

#staff
class Staff(models.Model):
	member_id=models.AutoField(primary_key=True)
	member_name = models.CharField(max_length=100,blank=False,null=False)
	member_email = models.EmailField(help_text='Your Email ID')
	member_mobileNo = models.CharField(help_text='Contact phone number',max_length=10,)
	member_password=models.CharField(max_length=15)

	class Meta:
		db_table='Staff'
