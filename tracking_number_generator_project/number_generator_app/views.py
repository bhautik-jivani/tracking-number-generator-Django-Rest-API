from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from number_generator_app.models import generate_unique_string, TrackingDetail, TrackingSubDetail
from number_generator_app.serializers import TrackingDetailSerialiser

# Create your views here.
class NextTrackingNumberView(APIView):
    serializer_class = TrackingDetailSerialiser

    def get(self, request, *args, **kwargs):
        data = request.GET
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            resp = {
                "msg": "Tracking number generated successfully.",
                "data": serializer.data.get('tracking_detail', {}),
            }
            return Response(resp, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrackingDetailsView(ModelViewSet):
    serializer_class = TrackingDetailSerialiser
    queryset = TrackingDetail.objects.all().order_by("-id")
    lookup_field = 'id'