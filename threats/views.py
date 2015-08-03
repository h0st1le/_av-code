from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from threat import IPDetails
from serializers import DetailsSerializer
from helpers import get_epoch_timestamp, create_random_string
from rest_framework import generics
from threats.models import Visitor, Visit
from threats.serializers import VisitorSerializer, VisitSerializer
from ipware.ip import get_ip


class APIRoot(APIView):
    def get(self, request):
        return Response({
            'Visitor Traffic': reverse('visitor_traffic', request=request),
            'Threat List': reverse('threat_list', request=request),
        })


class IPDetailsView(APIView):
    def get(self, request, *args, **kw):
        ip = args[0]
        details_request = IPDetails(ip, *args, **kw)
        result = DetailsSerializer(details_request)
        response = Response(result.data, status=status.HTTP_200_OK)

        visit = Visit()
        visit.endpoint = '/api/details/' + ip
        visit.timestamp = get_epoch_timestamp()
        visit.address = get_ip(request)

        cookie = request.COOKIES.get("alienvaultid", None)
        if cookie is None:
            ck_val = create_random_string()
            # set this cookie to expire in one year
            response.set_cookie('alienvaultid', ck_val, max_age=31536000)
            visitor = Visitor()
            visitor.alienvaultid = ck_val
            visitor.save()
        else:
            visitor = Visitor.objects.get(alienvaultid=cookie)

        visit.visitor_id = visitor.id
        visit.save()
        return response


class VisitorList(generics.ListAPIView):
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer


class VisitList(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


# TODO: add links to the endpoints for api navigation
class IPList(APIView):
    def get(self, request, *args, **kw):
        host = request.get_host()
        visits = Visit.objects.all()
        ips = set()
        for v in visits:
            ips.add(host + v.endpoint)
        response = Response(list(ips), status=status.HTTP_200_OK)
        return response
