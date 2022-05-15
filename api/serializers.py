from rest_framework import serializers
from project.models import *


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TodoModel
        fields = ['id', 'task', 'created_date', 'complete']