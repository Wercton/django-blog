from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Perfil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # one to one relationship with user/profile
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")
    image.width = 300
    image.height = 300

    def __str__(self):
        return f'{self.user.username} Perfil'

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_tamanho = (300, 300)
            img.thumbnail(output_tamanho)
            img.save(self.image.path)


# CASCADE: if the user is deleted, also deletes the profile
# but if profile deleted, user can remain
