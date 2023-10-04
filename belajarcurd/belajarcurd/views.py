from belajarcurd import serialize
from belajarcurd.models import Hero
from belajarcurd.serialize import HeroSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class HeroTable(APIView):
    def get(self, request):
        heroObj = Hero.objects.all()
        HeroSerializerObj = HeroSerializer(heroObj, many=True)
        return Response(HeroSerializerObj.data)

    def post(self, request):
        serializeobj = HeroSerializer(data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors, status=400)


class HeroUpdate(APIView):
    def post(self, request, pk):
        try:
            detailheroObj = Hero.objects.get(pk=pk)
        except:
            return Response(serializeobj.errors, status=400)

        serializeobj = HeroSerializer(detailheroObj, data=request.data)
        if serializeobj.is_valid():
            serializeobj.save()
            return Response(200)
        return Response(serializeobj.errors, status=400)


class HeroDelete(APIView):
    def post(self, request, pk):
        try:
            detailheroObj = Hero.objects.get(pk=pk)
        except:
            return Response("Not Found!", status=400)
        detailheroObj.delete()
        return Response(200)
