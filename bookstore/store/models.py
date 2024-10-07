# models.py
from django.db import models

class UploadedFile(models.Model):
    CATEGORY_CHOICES = [
        ('self', 'Self Improvement'),
        ('financial', 'Financial Improvement'),
        ('skills', 'Skills'),
        ('skill', 'Skill'),
        ('guide', 'Guide'),
        ('tutorial', 'Tutorials'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    file = models.FileField(upload_to='upload/', blank=True, null=True)  # File upload field (optional)
    url = models.URLField(blank=True, null=True)  # New field for links
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.file.name if self.file else self.url} ({self.get_category_display()})'
