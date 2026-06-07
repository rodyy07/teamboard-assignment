from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import KBEntry
from rest_framework import status
from .serializers import KBEntrySerializer
from .models import QueryLog
from accounts.models import Company

from authentication import APIKeyAuthentication

from django.db import transaction

from django.db.models import Count
from rest_framework.permissions import IsAuthenticated

from accounts.permissions import IsAdminUser
from .models import QueryLog

class SearchView(APIView):

    def post(self, request):

        search_term = request.data.get("search")

        if not search_term:
            return Response(
                {"error": "search field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        with transaction.atomic():

            results = KBEntry.objects.filter(
                Q(question__icontains=search_term) |
                Q(answer__icontains=search_term)
            )

            results_count = results.count()

            QueryLog.objects.create(
                company=request.user.company,
                search_term=search_term,
                results_count=results_count
            )

        serializer = KBEntrySerializer(
            results,
            many=True
        )

        return Response(
            {
                "search": search_term,
                "count": results_count,
                "results": serializer.data
            }
        )
class UsageSummaryView(APIView):

    
    

    permission_classes = [IsAdminUser]

    def get(self, request):

        total_queries = QueryLog.objects.count()

        active_companies = (
            QueryLog.objects
            .values("company")
            .distinct()
            .count()
        )

        top_search_terms = (
            QueryLog.objects
            .values("search_term")
            .annotate(count=Count("id"))
            .order_by("-count")[:5]
        )

        return Response({
            "total_queries": total_queries,
            "active_companies": active_companies,
            "top_search_terms": list(top_search_terms)
        })   

# Create your views here.
