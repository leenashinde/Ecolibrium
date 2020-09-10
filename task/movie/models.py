from django.db import models
# Create your models here.

class Director(models.Model):

    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "director"

    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)

class Category(models.Model):

    title = models.CharField(max_length=100)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "category"

    def __str__(self):
        return self.title


class Movie(models.Model):

    name = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    popularity = models.FloatField()
    imdb_score = models.FloatField()
    genre = models.ManyToManyField(Category,related_name='movie_category')

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "Movie"
