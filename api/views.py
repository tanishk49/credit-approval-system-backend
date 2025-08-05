from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
import math

@api_view(['POST'])
def register_customer(request):
    data = request.data
    monthly_salary = data.get("monthly_salary")

    # Calculate approved limit
    approved_limit = math.floor(36 * monthly_salary / 100000) * 100000

    # Save customer
    customer = Customer.objects.create(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        phone_number=data.get("phone_number"),
        monthly_salary=monthly_salary,
        approved_limit=approved_limit,
        current_debt=0
    )

    return Response({
        "customer_id": customer.customer_id,
        "name": f"{customer.first_name} {customer.last_name}",
        "approved_limit": approved_limit,
        "message": "Customer registered successfully!"
    }, status=status.HTTP_201_CREATED)
