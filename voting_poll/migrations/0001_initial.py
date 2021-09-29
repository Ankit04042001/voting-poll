# Generated by Django 3.1.7 on 2021-09-29 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pics')),
                ('name', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=100)),
                ('nishan', models.CharField(max_length=100)),
                ('vote', models.BigIntegerField()),
                ('order', models.SmallIntegerField(default=0)),
            ],
            options={
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='TotalVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_vote', models.BigIntegerField()),
            ],
        ),
    ]
