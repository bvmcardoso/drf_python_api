from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform



class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'title', 'description', 'length_name', 'description_backwards']
        # exclude = ['active']
    # Object level validation
    def validate(self, data):
        if data["title"] == data["description"]:
            raise serializers.ValidationError(
                "Title and description can not be equal"
            )

class StreamPlatformSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StreamPlatform




# def name_length(value):
#     if len(value) < 2 :
#         raise serializers.ValidationError("Naaame is too short")


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get(
#             "description", instance.description
#         )
#         instance.active = validated_data.get("active", instance.active)
#         instance.save()
#         return instance


#         return data

#     # Field level validation
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     return value
