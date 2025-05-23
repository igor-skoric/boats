# Generated by Django 5.1.7 on 2025-04-08 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_sectiontemplate_remove_yacht_length_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yachtsection',
            name='yacht',
        ),
        migrations.RemoveField(
            model_name='yachtsubsection',
            name='section',
        ),
        migrations.AlterField(
            model_name='detailtemplate',
            name='label',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='subsectiontemplate',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='YachtDetail',
        ),
        migrations.DeleteModel(
            name='YachtSection',
        ),
        migrations.DeleteModel(
            name='YachtSubSection',
        ),
    ]
