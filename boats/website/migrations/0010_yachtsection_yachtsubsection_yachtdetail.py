# Generated by Django 5.1.7 on 2025-04-08 08:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_remove_yachtsection_yacht_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='YachtSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.sectiontemplate')),
                ('yacht', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yacht_sections', to='website.yacht')),
            ],
        ),
        migrations.CreateModel(
            name='YachtSubSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subsection_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.subsectiontemplate')),
                ('yacht_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yacht_subsections', to='website.yachtsection')),
            ],
        ),
        migrations.CreateModel(
            name='YachtDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.TextField(blank=True, null=True)),
                ('detail_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.detailtemplate')),
                ('yacht_subsection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yacht_details', to='website.yachtsubsection')),
            ],
        ),
    ]
