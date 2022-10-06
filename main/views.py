import json
from xmlrpc.client import ServerProxy
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from .models import *
from .serializer import *
# Create your views here.

class MbtiViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = MbtiLecture.objects.all()

    serializer_class = LectureSerializer

    @action(detail=False, method=['GET'])
    def recommand(self, request, *args, **kwargs):
        self.queryset = MbtiLecture.objects.all()
        mbti = request.query_params['mbti'].lower()
        mbti_field = {"E_I":-1, "S_N":-1, "T_F":-1, "P_J":-1}

        if "e" in mbti: mbti_field["E_I"] = 1
        if "s" in mbti: mbti_field["S_N"] = 1
        if "t" in mbti: mbti_field["T_F"] = 1
        if "p" in mbti: mbti_field["P_J"] = 1

        score_lecture = []
        for query in self.queryset:
            score = mbti_field["E_I"] * query.E_I \
                + mbti_field["S_N"] * query.S_N \
                + mbti_field["T_F"] * query.T_F \
                + mbti_field["P_J"] * query.P_J
            print(f"{query.lecture_id}, score: {score}")
            score_lecture.append([score, query.lecture_id])
        
        score_lecture.sort(reverse=True)
        recommand_id_list = score_lecture[:min(2, len(score_lecture))]
        recommand_id_list = [i[1] for i in recommand_id_list]
        serializer = self.get_serializer(recommand_id_list, many=True)
        return Response(serializer.data)


mbti = MbtiViewSet.as_view({
    'get': 'recommand',
})




