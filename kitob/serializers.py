from rest_framework.serializers import ModelSerializer
from .models import avtorModel

class Serializer(ModelSerializer):
    class Meta:
        model = avtorModel
        fields = ('id','kitob_nomi','janri','sifati','avtori','yili')