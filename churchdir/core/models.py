from django.contrib.auth.models import AbstractUser
from django.db import models

TF_CHOICES = [
    ("KT", "KT"),
    ("KF", "KF"),
    ("Fta", "Fta"),
    ("Ffe", "Ffe"),
]

STATUS_CHOICES = [
    ("Active", "Active"),
    ("Not Active", "Not Active"),
]

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Branch (Kolo)"
        verbose_name_plural = "Branches (Ngaahi Kolo)"

    def __str__(self):
        return self.name

class User(AbstractUser):
    branch = models.ForeignKey(Branch, null=True, blank=True, on_delete=models.SET_NULL)
    is_minister = models.BooleanField(default=False)

    def __str__(self):
        return self.get_full_name() or self.username

class Member(models.Model):
    first_name = models.CharField("Hingoa", max_length=100)
    last_name  = models.CharField("Fakaiku", max_length=100, blank=True)
    dob        = models.DateField("Aho Faʻeleʻi", null=True, blank=True)
    tf_code    = models.CharField("T/F", max_length=10, choices=TF_CHOICES, blank=True)
    branch     = models.ForeignKey(Branch, on_delete=models.PROTECT)
    status     = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Active")

    class Meta:
        unique_together = [("first_name", "last_name", "dob", "branch")]
        ordering = ["branch", "last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip()
