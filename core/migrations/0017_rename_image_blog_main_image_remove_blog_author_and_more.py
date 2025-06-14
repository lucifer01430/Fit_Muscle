# Generated by Django 5.1.1 on 2025-06-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_appointment_blog_subscription_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='main_image',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description',
        ),
        migrations.AddField(
            model_name='blog',
            name='checklist_items',
            field=models.TextField(blank=True, help_text='One checklist item per line'),
        ),
        migrations.AddField(
            model_name='blog',
            name='content_section',
            field=models.TextField(default='This is placeholder content. Please update it from the admin panel.', help_text='Main HTML content block (use linebreaks or WYSIWYG)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='gallery_image1',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/gallery/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='gallery_image2',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/gallery/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='gallery_image3',
            field=models.ImageField(blank=True, null=True, upload_to='blogs/gallery/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='intro_text',
            field=models.TextField(default='This is placeholder content. Please update it from the admin panel.', help_text='Short intro paragraph shown in hero section'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='quote',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='blog',
            name='quote_author',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.CharField(max_length=100),
        ),
    ]
