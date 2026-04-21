from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import loan_types, users, loanapplication, payment_schedule, report, loan_documents
from .serializers import loan_typesSerializer, usersSerializer, loanapplicationSerializer, payment_scheduleSerializer, reportSerializer, loan_documentsSerializer

# loan_types API
class loan_typesViewSet(viewsets.ModelViewSet):
    queryset = loan_types.objects.all()
    serializer_class = loan_typesSerializer
    permission_classes = [IsAuthenticated]

# users API
class usersViewSet(viewsets.ModelViewSet):
    queryset = users.objects.all()
    serializer_class = usersSerializer
    permission_classes = [IsAuthenticated]

# loanapplication API
class loanapplicationViewSet(viewsets.ModelViewSet):
    queryset = loanapplication.objects.all()
    serializer_class = loanapplicationSerializer
    permission_classes = [IsAuthenticated]

# payment_schedule API
class payment_scheduleViewSet(viewsets.ModelViewSet):
    queryset = payment_schedule.objects.all()
    serializer_class = payment_scheduleSerializer
    permission_classes = [IsAuthenticated]

# report API
class reportViewSet(viewsets.ModelViewSet):
    queryset = report.objects.all()
    serializer_class = reportSerializer
    permission_classes = [IsAuthenticated]


# loan_documents API
class loan_documentsViewSet(viewsets.ModelViewSet):
    queryset = loan_documents.objects.all()
    serializer_class = loan_documentsSerializer
    permission_classes = [IsAuthenticated]

