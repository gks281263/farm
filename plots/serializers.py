from rest_framework import serializers
from .models import Plot

class PlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plot
        fields = ['plot_id', 'plot_name', 'plot_location', 'plot_size', 'created_at', 'updated_at']
        read_only_fields = ['plot_id', 'created_at', 'updated_at']

    def validate(self, data):
        required_fields = ['plot_name', 'plot_location', 'plot_size']
        missing = [field for field in required_fields if not data.get(field)]
        if missing:
            raise serializers.ValidationError(
                f"Missing required fields: {', '.join(missing)}"
            )
        return data 