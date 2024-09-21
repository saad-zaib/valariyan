from django.db import models
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from PIL import Image as PilImage
import io

class Review(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    content = models.TextField()
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Compress the image before saving
        if self.avatar:
            img = PilImage.open(self.avatar)
            img_io = io.BytesIO()

            # Resize and compress the image
            img = img.convert('RGB')
            img.thumbnail((800, 800))  # Resize to fit within 800x800

            # Save the image to a BytesIO object
            img.save(img_io, format='JPEG', quality=85)  # Compress image to JPEG format
            img_file = ContentFile(img_io.getvalue(), name=self.avatar.name)

            # Save the compressed image
            self.avatar.save(self.avatar.name, img_file, save=False)

        super().save(*args, **kwargs)
