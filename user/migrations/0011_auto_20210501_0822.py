# Generated by Django 3.1.7 on 2021-05-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210501_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='agemax',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='agemin',
            field=models.CharField(default='', max_length=3),
        ),
        migrations.AlterField(
            model_name='profile',
            name='budget_lowerfilter',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='budget_upperfilter',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grad_yearmax',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grad_yearmin',
            field=models.CharField(default='', max_length=4),
        ),
    ]
