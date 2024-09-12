from rest_framework import serializers

from number_generator_app.models import TrackingDetail, TrackingSubDetail

class TrackingSubDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingSubDetail
        fields = ['id', 'tracking_number', 'created_at']

class TrackingDetailSerialiser(serializers.ModelSerializer):
    tracking_detail = TrackingSubDetailSerializer(read_only=True, source='trackingsubdetail')

    class Meta:
        model = TrackingDetail
        fields = ['id', 'origin_country_id', 'destination_country_id', 'weight', 'customer_id', 'customer_name', 'customer_slug', 'created_at', 'tracking_detail']
    
    def create(self, validated_data):
        obj = super().create(validated_data)
        TrackingSubDetail.objects.create(tracking_detail=obj)
        return obj