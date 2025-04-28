from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Transaction
from django.db.models import Sum
import uuid as uuid_lib
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
@login_required(login_url='login')
def expense(request):
    if request.method == "POST":
        description = request.POST.get('description')
        amount = request.POST.get('amount')
        
        if not description or not amount:
            messages.info(request, "Please fill all fields")
            return redirect('/')
        
        try:
            amount = float(amount)
        except (TypeError, ValueError):
            messages.error(request, "Amount must be a number")
            return redirect('/')

        Transaction.objects.create(descriptions=description, amount=amount, created_by = request.user)
        messages.success(request, "Transaction added successfully!")
        return redirect('/')
    
    context = {
        "transactions" : Transaction.objects.filter(created_by = request.user),
        "balance" : Transaction.objects.filter(created_by = request.user).aggregate(balance = Sum('amount'))['balance'] or 0,
        "expense" : Transaction.objects.filter(created_by = request.user, amount__lte = 0).aggregate(expense = Sum('amount'))['expense'] or 0,
        "income" : Transaction.objects.filter(created_by = request.user, amount__gte = 0 ).aggregate(income = Sum('amount'))['income'] or 0
               }

    return render(request, 'expense.html', context)


def delete_item(request, uuid) : 
    try:
        # Validate that uuid is a real UUID
        uuid_obj = uuid_lib.UUID(str(uuid))
    except ValueError:
        return HttpResponseBadRequest("Invalid UUID.")

    # If uuid is valid, continue
    Transaction.objects.get(uuid=uuid_obj).delete()
    return redirect('/')


def home(request) : 
    return render(request, 'home.html')
