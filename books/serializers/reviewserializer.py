from rest_framework import serializers
from ..models.reviews import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'reviewer', 'rating', 'comment', 'created_at']