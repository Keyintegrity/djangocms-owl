from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwlCarousel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('pagination', models.BooleanField(default=False, help_text='Show pagination. (dot dot dot)')),
                ('pagination_numbers', models.BooleanField(default=False, help_text='Show numbers inside pagination buttons')),
                ('navigation', models.BooleanField(default=False, help_text='Display "next" and "prev" buttons.')),
                ('autoplay', models.BooleanField(default=False, help_text='Slides cycle automatically every 5 seconds')),
                ('stop_on_hover', models.BooleanField(default=False, help_text='Stop autoplay on mouse hover')),
                ('items', models.PositiveSmallIntegerField(default=1, help_text='maximum amount of items displayed at a time')),
                ('auto_height', models.BooleanField(default=False, help_text='Add height to owl-wrapper-outer so you can use different heights on slides.')),
                ('style', models.CharField(default='default', help_text='CSS class', max_length=255, verbose_name='style', choices=[('default', 'Default')])),
                ('template', models.CharField(default='default', max_length=255, verbose_name='template', choices=[('default', 'Default')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
