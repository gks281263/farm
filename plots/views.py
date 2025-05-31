from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Plot
from .serializers import PlotSerializer
from django.shortcuts import get_object_or_404

class AddPlotView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PlotSerializer(data=request.data)
        if serializer.is_valid():
            plot = serializer.save()
            return Response({
                "status": "success",
                "message": "Plot added successfully.",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "status": "error",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST) 

class EditPlotView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, plot_id):
        plot = get_object_or_404(Plot, plot_id=plot_id)
        serializer = PlotSerializer(plot, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": "success",
                "message": "Plot updated successfully.",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "status": "error",
            "message": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class DeletePlotView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, plot_id):
        plot = get_object_or_404(Plot, plot_id=plot_id)
        plot.delete()
        return Response({
            "status": "success",
            "message": "Plot deleted successfully."
        }, status=status.HTTP_200_OK)

class ListPlotsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        plots = Plot.objects.all()
        serializer = PlotSerializer(plots, many=True)
        return Response({
            "status": "success",
            "data": serializer.data
        }, status=status.HTTP_200_OK) 