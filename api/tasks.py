from celery import shared_task
import pandas as pd
from .models import Customer, Loan
from datetime import datetime

@shared_task
def load_customer_data(file_path="customer_data.xlsx"):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        Customer.objects.update_or_create(
            customer_id=row['customer_id'],
            defaults={
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'phone_number': str(row['phone_number']),
                'monthly_salary': row['monthly_salary'],
                'approved_limit': row['approved_limit'],
                'current_debt': row['current_debt']
            }
        )
    return "Customer data loaded."

@shared_task
def load_loan_data(file_path="loan_data.xlsx"):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        try:
            customer = Customer.objects.get(customer_id=row['customer_id'])
            Loan.objects.update_or_create(
                loan_id=row['loan_id'],
                defaults={
                    'customer': customer,
                    'loan_amount': row['loan_amount'],
                    'tenure': row['tenure'],
                    'interest_rate': row['interest_rate'],
                    'monthly_payment': row['monthly_payment'],
                    'emis_paid_on_time': row['EMIs paid on time'],
                    'start_date': datetime.strptime(str(row['start_date']), '%Y-%m-%d'),
                    'end_date': datetime.strptime(str(row['end_date']), '%Y-%m-%d'),
                }
            )
        except Customer.DoesNotExist:
            continue  # Skip if customer not found
    return "Loan data loaded."

@shared_task
def test_task():
    return "Task completed successfully"
