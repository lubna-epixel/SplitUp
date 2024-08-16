from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    id=models.CharField(max_length=200,primary_key=True,unique=True,auto_created=True,)
    name=models.CharField(max_length=200)
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    email=models.CharField(max_length=200)
    password=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
class Group(models.Model):
    group_name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='expense_groups')
class Expense(models.Model):
    SPLIT_METHOD_CHOICES = [
        ('Equal', 'Equal'),
        ('Custom', 'Custom'),
    ]

    amount_spent = models.IntegerField()
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)  
    paid_by = models.ForeignKey(User, on_delete=models.CASCADE)  
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  
    split_method = models.CharField(max_length=20, choices=SPLIT_METHOD_CHOICES)

    def __str__(self):
        return f"{self.description} - {self.amount_spent}"