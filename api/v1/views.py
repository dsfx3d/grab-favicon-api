from rest_framework.views import APIView
from rest_framework.response import Response

from grabicon import FaviconGrabber

from frontend.forms import GrabFaviconForm
from . import serializers


class GrabiconView(APIView):


    def get(self, request):

        form = GrabFaviconForm(request.GET)

        if form.is_valid():
            url = form.cleaned_data['url']
            grabber = FaviconGrabber()
            try:
                favicons = grabber.grab(url)
            except Exception as e:
                return Response(dict(error=e))

            s = serializers.FaviconSerializer(favicons, many=True)
            return Response(s.data)

        return Response(dict(error=form.error))
