from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    monthly_salary = models.FloatField()
    approved_limit = models.FloatField()
    current_debt = models.FloatField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.customer_id})"


class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    loan_id = models.CharField(max_length=20, unique=True)
    loan_amount = models.FloatField()
    tenure = models.IntegerField()  # in months
    interest_rate = models.FloatField()
    monthly_payment = models.FloatField()
    emis_paid_on_time = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Loan {self.loan_id} for {self.customer}"
