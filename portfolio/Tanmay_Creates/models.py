from django.db import models
import PIL

class Projects(models.Model):
    name = models.CharField(max_length=250)
    pic = models.ImageField()
    about = models.CharField(null=True, blank=True, max_length=250)
    git = models.URLField()
    link = models.URLField(default="/projects#")
    show = models.BooleanField(default=True)



    def __str__(self) -> str:
        return self.name

