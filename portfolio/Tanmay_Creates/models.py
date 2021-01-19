from django.db import models
import PIL
from froala_editor.fields import FroalaField

class Projects(models.Model):
    name = models.CharField(max_length=250)
    pic = models.ImageField()
    about = models.CharField(null=True, blank=True, max_length=250)
    git = models.URLField()
    link = models.URLField(default="/projects#")
    show = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name


class PageForm(models.Model):
    name = models.CharField(max_length=560)
    email = models.EmailField()
    content = FroalaField(options={
    'toolbarInline': True,
    'theme':'dark'
        })
    read = models.BooleanField(default=False) 

    def __str__(self) -> str:
        return "Name: "+ self.name + " | Read: "+ str(self.read )