# Generated by Django 3.1.7 on 2021-04-24 16:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('streamers', '0002_auto_20210409_0110'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stream',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('stream_id', models.CharField(max_length=64)),
                ('game_id', models.CharField(max_length=64)),
                ('game_name', models.CharField(max_length=64)),
                ('type', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=255)),
                ('viewer_count', models.IntegerField()),
                ('started_at', models.DateTimeField()),
                ('language', models.CharField(max_length=16)),
                ('thumbnail_url', models.CharField(max_length=255)),
                ('tag_ids', models.CharField(max_length=255)),
                ('is_mature', models.BooleanField()),
                ('streamer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streamers.streamer')),
            ],
        ),
    ]