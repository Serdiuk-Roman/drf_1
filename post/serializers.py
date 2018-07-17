from django.contrib.auth.models import User
from rest_framework import serializers

from post.models import Category, Post


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         # fields = "__all__"
#         fields = (
#             'url',
#             'id',
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'is_staff',
#             'is_active',
#             'date_joined'
#         )


class UserSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail')
    id = serializers.IntegerField(label='ID', read_only=True)
    username = serializers.CharField(max_length=150)
    first_name = serializers.CharField(allow_blank=True, max_length=30, required=False)
    last_name = serializers.CharField(allow_blank=True, max_length=150, required=False)
    email = serializers.EmailField(
        allow_blank=True,
        label='Email address',
        max_length=254,
        required=False
    )
    is_staff = serializers.BooleanField(label='Staff status', required=False)
    is_active = serializers.BooleanField(label='Active', required=False)
    date_joined = serializers.DateTimeField(required=False)



class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=250)
    is_active = serializers.BooleanField()
    user = serializers.IntegerField(source='user_id', read_only=True)
    # cat_link = serializers.HyperlinkedIdentityField(
    #     view_name='category-detail',
    #     read_only=True
    # )


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(choices=Post.STATUSES, default=0)
    category = serializers.IntegerField(source='category_id', read_only=True)
    user = serializers.IntegerField(source='user_id')
    title = serializers.CharField(max_length=255, required=True)
    content = serializers.CharField(required=True)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)
    # post_link = serializers.HyperlinkedIdentityField(
    #     view_name='post-detail',
    #     read_only=True
    # )

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.category = validated_data.get('category', instance.category)
        instance.user = validated_data.get('user', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('context', instance.context)
        instance.save()
        return instance

