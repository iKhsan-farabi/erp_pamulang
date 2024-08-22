from django.db import models

# Kelas Nama Bahan

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# Kelas Nama Mesin Produksi

class Machine(models.Model):
    machine_id = models.AutoField(primary_key=True)
    machine_name = models.CharField(max_length=100)

# Kelas Info Customer

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

# Kelas Nama Pekerjaan

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=100)

# Kelas Orders

class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    orders_invoice = models.CharField(max_length=100, unique=True)
    orders_date = models.DateField()
    orders_pick = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

# Kelas Order Item

class Order_Item(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    product_id = models. ForeignKey(Product, on_delete=models.CASCADE)
    size_print = models.DecimalField(max_digits=5, decimal_places=2)
    size_media = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)