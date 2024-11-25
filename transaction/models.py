from django.db import models
from account.models import UserBankAccount
# Create your models here.

TRANSACTION_TYPE =(
    (1, 'Deposite'),
    (2, 'Withdrawl'),
    (3, 'Loan'),
    (4, 'Loan Paid'),
)
class Transaction(models.Model):
    account = models.ForeignKey(UserBankAccount, related_name='transaction', on_delete= models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transaction = models.DecimalField(decimal_places=2, max_digits=12)
    transaction_type = models.IntegerField(choices=TRANSACTION_TYPE, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['timestamp']