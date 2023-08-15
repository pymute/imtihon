from rest_framework.serializers import ModelSerializer
from .models import avtorModel

class Serializer(ModelSerializer):
    class Meta:
        model = avtorModel
        fields = ('id','kitob_nomi','janri','sifati','avtori','yili')

class AvtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = avtorModel
        fields = ('kitob_id','avtor_ismi','avtor_familiyasi','kitoblari','tugulgan_sana')
