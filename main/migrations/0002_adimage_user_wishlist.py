<<<<<<< HEAD
# Generated by Django 4.0.5 on 2022-12-18 17:58
=======
# Generated by Django 4.0.3 on 2022-12-19 04:47
>>>>>>> ac4f7d741ed7b447d66eb733b0c9036b5f007cc6

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adimage',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('ads', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ads')),
            ],
        ),
    ]
