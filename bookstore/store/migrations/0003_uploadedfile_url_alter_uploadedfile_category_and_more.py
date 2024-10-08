# Generated by Django 5.1.1 on 2024-10-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_uploadedfile_delete_resource'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='category',
            field=models.CharField(choices=[('self', 'Self Improvement'), ('financial', 'Financial Improvement'), ('skills', 'Skills'), ('skill', 'Skill'), ('guide', 'Guide'), ('tutorial', 'Tutorials'), ('links', 'Links')], max_length=50),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='upload/'),
        ),
    ]
