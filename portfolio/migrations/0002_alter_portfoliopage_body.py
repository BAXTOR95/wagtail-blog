# Generated by Django 5.0.7 on 2024-07-23 01:02

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='body',
            field=wagtail.fields.StreamField([('heading_block', wagtail.blocks.StructBlock([('heading_text', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4')], required=False))])), ('paragraph_block', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image_block', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('embed_block', wagtail.embeds.blocks.EmbedBlock(help_text='Insert a URL to embed. For example, https://www.youtube.com/watch?v=xvFZjo5PgG0', icon='media')), ('card', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link'])), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))], group='Sections')), ('featured_posts', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link'], required=False)), ('posts', wagtail.blocks.ListBlock(wagtail.blocks.PageChooserBlock(page_type=['blog.BlogPage'])))], group='Sections'))], blank=True, help_text='Use this section to list your projects and skills.'),
        ),
    ]
