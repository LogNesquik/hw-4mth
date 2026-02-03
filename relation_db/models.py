from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Person(models.Model):
    people = models.CharField(max_length=35, default='Мирослав', verbose_name='Введите имя человека')
    tags = models.ManyToManyField(Tag, null=True)


    def __str__(self):
        return f"{self.people} ---- {', '.join(i.name for i in self.tags.all())}"
class Touring(models.Model):
    choice_tour = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='choice_tour')
    tour = models.CharField(max_length=70, default='.... тур', verbose_name='Введите название тура', null=True)


    def __str__(self):
        return self.tour
    
class Review(models.Model):
    STARS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5')
    )
    choice_tour = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='choice_review')
    stars = models.CharField(max_length=100, choices=STARS, default=5)
    comment = models.CharField(max_length=100, default='Хороший, не составил много проблем!')


    def __str__(self):
        return f"{self.comment} - {self.stars}"