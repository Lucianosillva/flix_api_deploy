from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
        
    
    class Meta:
        model = Movie
        fields = '__all__'
    
      
        
    # validações...
    def validate_release_date(self, value):
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser inferior a 1990')
        return value
    
    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O tamanho máximo deste campo deve ser 200 caracteres.')
        return value
    
# para tratar os dados para o front-end...   
class MovieListDetailSerializer(serializers.ModelSerializer):
    genre = GenreSerializer() # usamos um serializer que já existe...
    actors = ActorSerializer(many=True)
    rate = serializers.SerializerMethodField(read_only=True)
    
    # método para retornar o valor de rate...
    def get_rate(self, obj):
        # aggregate cria um campo a mais, no caso stars__avg
        # ['stars__avg'] o ORM cria uma variável com o nome do campo dunder avg e retorna somente ele
        # rate busca no model Review related_name='reviews' o campo stars
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
            
        if rate:
            return round(rate, 1)
        return None
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']