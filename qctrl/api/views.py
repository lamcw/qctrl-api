from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.settings import api_settings
from rest_framework_csv.parsers import CSVParser

from .models import Control
from .renderers import ControlCSVRenderer
from .serializers import ControlSerializer


class SmallResultSetPagination(PageNumberPagination):
    """Limits results to 5 per page."""

    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5


class ControlViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows control to be viewed and edited.

    This ViewSet implments the following functionalities:

    1. Create a new control
    2. List all controls (five per page)
    3. Get a specific control
    4. Update a specific control
    5. Delete a specific control
    6. Bulk upload controls in CSV format
    7. Download controls in CSV format
    """

    queryset = Control.objects.order_by('id')
    serializer_class = ControlSerializer
    pagination_class = SmallResultSetPagination

    @action(detail=False,
            methods=['post'],
            parser_classes=[CSVParser] + api_settings.DEFAULT_PARSER_CLASSES,
            renderer_classes=[ControlCSVRenderer] +
            api_settings.DEFAULT_RENDERER_CLASSES)
    def upload(self, request, *args, **kwargs):
        """
        Bulk upload controls in CSV format.

        With curl,
            curl -X POST -i
            --data-binary @dir/to/foo.csv
            -H 'Content-Type: text/csv'
            -H 'Accept: text/csv' http://domain.name/api/controls/upload/
        """
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,
                        status=status.HTTP_303_SEE_OTHER,
                        headers={
                            'Location':
                            reverse_lazy('control-list', request=request)
                        })

    @action(detail=False,
            methods=['get'],
            renderer_classes=[ControlCSVRenderer] +
            api_settings.DEFAULT_RENDERER_CLASSES)
    def download(self, request):
        """
        Export all controls in CSV format.

        The CSV header is in order of: name, type, maximum_rabi_rate,
        polar_angle
        """
        content = [{
            'name': control.name,
            'type': control.type,
            'maximum_rabi_rate': control.maximum_rabi_rate,
            'polar_angle': control.polar_angle
        } for control in self.queryset]
        return Response(content)
