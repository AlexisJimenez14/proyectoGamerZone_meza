# Generated by Django 5.1.3 on 2024-11-22 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_app', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(choices=[('Asus', 'Asus'), ('HP', 'HP'), ('Dell', 'Dell'), ('Alienware', 'Alienware')], default='Asus', max_length=20),
        ),
    ]
