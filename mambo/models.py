from django.db import models

# Create your models here.

class Category(models.Model):

    CATEGORY_OPTIONS = [
        ("M D", "MAIN DISH"),
        ("C D", "COLD DRINKS"),
        ("T", "TEA"),
        ("D", "DISSERTS"),
    ]
    name_of_category = models.CharField(max_length=50, verbose_name="MEALS")
    no_of_category = models.IntegerField()
    items_in_a_category = models.CharField(max_length=50)
    date_of_categorysale = models.DateTimeField(auto_now=False,auto_now_add=False)
    address = models.CharField(max_length=100, null=True,blank=True,default="N/A")
    category_type =   models.CharField(max_length=100, choices= CATEGORY_OPTIONS)
    description = models.TextField()
    
    #contact = models.CharField(max_length=10)
    #email = models.EmailField()
    #birth_date = models.DateField(auto_now=False,auto_now_add=False)
    #no_of_sales = models.IntegerField()


class Dish(models.Model):
    dish_details = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, verbose_name="Your choice", on_delete=models.CASCADE )

class Customer_Table(models.Model):

    TABLE_OPTIONS = [
        ("S", "SINGLE"),
        ("D", "DOUBLE"),
        ("G", "GROUP"),
    ]
    STATUS_CHOICE = [
        ("O", "OCCUPIED"),
        ("V", "VACCANT"),
    ]

    table_type = models.CharField(max_length=25, choices=TABLE_OPTIONS)
    status = models.CharField(max_length=20, choices= STATUS_CHOICE)

class order(models.Model):
    order_date = models.DateField(auto_now=False)
    dish = models.ForeignKey(Dish,verbose_name="Your dish", on_delete=models.CASCADE )
    quantity = models.IntegerField()
    table = models.ForeignKey(Customer_Table,verbose_name="Your table", on_delete=models.CASCADE)
    served_by = models.CharField(max_length=20)

class payment(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    received_by = models.CharField(max_length=20)
    






