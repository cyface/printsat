"""Django REST Framework API Definitions"""

from rest_framework import routers, serializers, viewsets
from printsat_app.models import Telemetry


class TelemetrySerializer(serializers.HyperlinkedModelSerializer):
    """Telemetry API Serializer"""

    class Meta:
        model = Telemetry


class TelemetryPanelSerializer(serializers.HyperlinkedModelSerializer):
    """Telemetry API Serializer"""

    class Meta:
        model = Telemetry
        fields = ('ps_time_seconds', 'bat_v', 'sp1_i_5', 'sp2_i_6', 'sp3_i_7', 'sp4_i_8', 'sp1_v_5', 'sp2_v_6',
                  'sp3_v_7', 'sp4_v_8')


class TelemetryViewSet(viewsets.ModelViewSet):
    """ViewSets define the view behavior."""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetrySerializer


class TelemetryPanelViewSet(viewsets.ModelViewSet):
    """ViewSets define the view behavior."""
    queryset = Telemetry.objects.all()
    serializer_class = TelemetryPanelSerializer

# Routers provide an easy way of automatically determining the URL conf.
api_router = routers.DefaultRouter()
api_router.register(r'telemetry', TelemetryViewSet)
api_router.register(r'telemetry_panel', TelemetryPanelViewSet)