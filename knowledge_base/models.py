from django.db import models

from accounts.models import Company

# Create your models here.

class KBEntry(models.Model):
    class Category(models.TextChoices):

        API = "api","API",
        DATABASE = "database","Database",
        CLOUD = "cloud","Cloud",
        FRAMEWORK = "framework","Framework",
        GENERAL = "general","General",

    question = models.TextField()

    answer = models.TextField()

    category = models.CharField(
        max_length = 20,
        choices = Category.choices,
    )

    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.company.company_name} - {self.question[:80]}"


class QueryLog(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete = models.CASCADE,
        related_name = "query_logs"
    )

    search_term = models.CharField(
        max_length = 255
    )

    results_count = models.IntegerField()

    queried_at = models.DateTimeField(auto_now_add = True)