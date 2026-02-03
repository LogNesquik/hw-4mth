from django.db import models

class Category(models.Model):
    type_category = models.CharField(max_length=35)

    def __str__(self):
        return self.type_category
    
class Person(models.Model):
    name = models.CharField(max_length=35, default='Владимир')
    tag_category = models.ManyToManyField(Category, null=True)

    def __str__(self):
        return self.name

# Отношение 1 к many
class Tourning(models.Model):
    choice_tour = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='tour')
    tour = models.CharField(max_length=60, default='.... тур!')

    def __str__(self):
        return f"{self.choice_tour} записался на {self.tour}"

class StarsReview(models.Model):
    STARS = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    choice_stars = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='stars')
    star = models.CharField(max_length=100, choices=STARS, default=5)
    comments_stars = models.CharField(max_length=50, default='Хороший турист!')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.choice_stars} - {self.comments_stars} - {self.star}"