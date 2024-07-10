# Generated by Django 5.0 on 2024-07-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0028_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now_add=True)),
                ('Title', models.CharField(max_length=100)),
                ('Image', models.ImageField(null=True, upload_to='Premiums')),
                ('Description', models.TextField(blank=True, null=True)),
                ('Content', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
            options={
                'verbose_name': 'blog',
                'verbose_name_plural': 'blogs',
                'ordering': ['Title'],
            },
        ),
    ]