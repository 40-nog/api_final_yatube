from rest_framework import serializers
from rest_framework.relations import SlugRelatedField


from posts.models import Comment, Post, User, Follow, Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        model = Group
        fields = ('title', 'slug', 'description', 'author')
 

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
                serializers.UniqueTogetherValidator(
                    queryset=Follow.objects.all(),
                    fields=('user', 'following'),
                    message=('Вы уже подписаны на этого автора!')
                ),
        ]

    def validate(self, data):
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data
