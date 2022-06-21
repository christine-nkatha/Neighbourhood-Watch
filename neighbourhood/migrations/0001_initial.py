# Generated by Django 4.0.5 on 2022-06-21 04:30

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Neighbourhood Title')),
                ('description', models.TextField(blank=True, max_length=254, verbose_name='Description')),
                ('location', models.CharField(blank=True, max_length=150, null=True, verbose_name='Neighbourhood Location')),
                ('county', models.CharField(blank=True, choices=[('', 'Choose'), ('Baringo', 'Baringo'), ('Bomet', 'Bomet'), ('Bungoma ', 'Bungoma '), ('Busia', 'Busia'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Embu', 'Embu'), ('Garissa', 'Garissa'), ('Homa Bay', 'Homa Bay'), ('Isiolo', 'Isiolo'), ('Kajiado', 'Kajiado'), ('Kakamega', 'Kakamega'), ('Kericho', 'Kericho'), ('Kiambu', 'Kiambu'), ('Kilifi', 'Kilifi'), ('Kirinyaga', 'Kirinyaga'), ('Kisii', 'Kisii'), ('Kisumu', 'Kisumu'), ('Kitui', 'Kitui'), ('Kwale', 'Kwale'), ('Laikipia', 'Laikipia'), ('Lamu', 'Lamu'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Mandera', 'Mandera'), ('Meru', 'Meru'), ('Migori', 'Migori'), ('Marsabit', 'Marsabit'), ('Mombasa', 'Mombasa'), ('Muranga', 'Muranga'), ('Nairobi', 'Nairobi'), ('Nakuru', 'Nakuru'), ('Nandi', 'Nandi'), ('Narok', 'Narok'), ('Nyamira', 'Nyamira'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Samburu', 'Samburu'), ('Siaya', 'Siaya'), ('Taita Taveta', 'Taita Taveta'), ('Tana River', 'Tana River'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Trans Nzoia', 'Trans Nzoia'), ('Turkana', 'Turkana'), ('Uasin Gishu', 'Uasin Gishu'), ('Vihiga', 'Vihiga'), ('Wajir', 'Wajir'), ('West Pokot', 'West Pokot')], max_length=150, null=True, verbose_name='Neighbourhood County')),
                ('neighbourhood_logo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='neighbourhood_logo')),
                ('health_department', models.CharField(blank=True, max_length=15, null=True, verbose_name='Health Department')),
                ('police_department', models.CharField(blank=True, max_length=15, null=True, verbose_name='Police Department')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('neighbourhood_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Neighbourhood Admin')),
            ],
            options={
                'verbose_name_plural': 'NeighbourHoods',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=254, verbose_name='Bio')),
                ('national_id', models.CharField(blank=True, max_length=10, verbose_name='National ID')),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='profile_picture')),
                ('email_confirmed', models.BooleanField(default=False, verbose_name='Is Confirmed?')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('neighbourHood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood', verbose_name='NeighbourHood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, null=True, verbose_name='Post Title')),
                ('description', models.TextField(null=True, verbose_name='Post Description')),
                ('category', models.CharField(choices=[('1', 'Crimes and Safety'), ('2', 'Health Emergency'), ('3', 'Recommendations'), ('4', 'Fire Breakouts'), ('5', 'Lost and Found'), ('6', 'Death'), ('7', 'Event')], max_length=120, verbose_name='Post Category')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.profile', verbose_name='Post Author')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood', verbose_name='Rlated NeighbourHood')),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neighbourhood_membership', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood_member', to='neighbourhood.neighbourhood', verbose_name='NeighbourHood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.profile', verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Members',
            },
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Business Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('email', models.CharField(blank=True, max_length=150, null=True, verbose_name='Business Email Address')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
                ('neighbourhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.neighbourhood', verbose_name='NeighbourHood')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neighbourhood.profile', verbose_name='Business Owner')),
            ],
            options={
                'verbose_name_plural': 'Businesses',
            },
        ),
    ]
