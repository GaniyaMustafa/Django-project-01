# Generated by Django 2.2.4 on 2020-02-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kategori', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='produk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produk', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='kategori',
            old_name='Kategori',
            new_name='kategori',
        ),
    ]
