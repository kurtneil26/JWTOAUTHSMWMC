from rest_framework import serializers
from .models import loan_types, users, loanapplication, payment_schedule, report, loan_documents



class loan_typesSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan_types
        fields = '__all__'


class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = '__all__'

class loanapplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanapplication
        fields = '__all__'

class payment_scheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment_schedule
        fields = '__all__'


class reportSerializer(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = '__all__'

class loan_documentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan_documents
        fields = '__all__'

