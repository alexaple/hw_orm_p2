# Generated by Django 4.2.5 on 2023-10-01 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_scope'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='articles',
            field=models.ManyToManyField(related_name='tags', through='articles.Scope', to='articles.article'),
        ),
        migrations.AlterField(
            model_name='scope',
            name='is_main',
            field=models.BooleanField(verbose_name='Основной'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Раздел'),
        ),
    ]
