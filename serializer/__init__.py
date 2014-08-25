from marshmallow import Serializer, fields


class MoodSerializer(Serializer):
    class Meta:
        fields = ('level', 'created')
