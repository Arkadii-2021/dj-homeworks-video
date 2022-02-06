# Generated by Django 4.0.2 on 2022-02-05 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default='Разное', max_length=32)),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрикатор',
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.CreateModel(
            name='RelationShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to='articles.article')),
                ('heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relationships', to='articles.tag')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='scopes',
            field=models.ManyToManyField(related_name='articles', through='articles.RelationShip', to='articles.Tag'),
        ),
    ]