# Generated by Django 3.1.14 on 2022-07-14 08:19

from django.db import migrations
import home.blocks
import messaging.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20220422_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='body',
            field=wagtail.core.fields.StreamField([('download', wagtail.core.blocks.StructBlock([('available_text', wagtail.core.blocks.CharBlock(help_text='This text appears when it is possible for the user to install the app on their phone.')), ('unavailable_text', wagtail.core.blocks.CharBlock(form_classname='red-help-text', help_text='This text appears when the user is using a feature phone and thus cannot install the app (the button will be disabled in this case). [Currently not implemented]', required=False)), ('offline_text', wagtail.core.blocks.CharBlock(help_text="This text appears when the user is navigating the site via the offline app and thus it doesn't make sense to install the offline app again (the button will be disabled in this case).", required=False)), ('page', wagtail.core.blocks.PageChooserBlock(page_type=['wagtailcore.Page'])), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image']))]))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title', template='blocks/heading.html')), ('paragraph', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image'])), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('paragraph_v1_legacy', home.blocks.RawHTMLBlock(icon='code')), ('image', wagtail.images.blocks.ImageChooserBlock(template='blocks/image.html')), ('list', wagtail.core.blocks.ListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('numbered_list', home.blocks.NumberedListBlock(wagtailmarkdown.blocks.MarkdownBlock(icon='code'))), ('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('embedded_poll', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('poll', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Poll']))])), ('embedded_survey', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('survey', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Survey']))])), ('embedded_quiz', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('quiz', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Quiz']))])), ('media', home.blocks.MediaBlock(icon='media')), ('chat_bot', wagtail.core.blocks.StructBlock([('subject', wagtail.core.blocks.CharBlock()), ('button_text', wagtail.core.blocks.CharBlock()), ('trigger_string', wagtail.core.blocks.CharBlock()), ('channel', messaging.blocks.ChatBotChannelChooserBlock())])), ('download', wagtail.core.blocks.StructBlock([('available_text', wagtail.core.blocks.CharBlock(help_text='This text appears when it is possible for the user to install the app on their phone.')), ('unavailable_text', wagtail.core.blocks.CharBlock(form_classname='red-help-text', help_text='This text appears when the user is using a feature phone and thus cannot install the app (the button will be disabled in this case). [Currently not implemented]', required=False)), ('offline_text', wagtail.core.blocks.CharBlock(help_text="This text appears when the user is navigating the site via the offline app and thus it doesn't make sense to install the offline app again (the button will be disabled in this case).", required=False)), ('page', wagtail.core.blocks.PageChooserBlock(page_type=['wagtailcore.Page'])), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image']))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='home_featured_content',
            field=wagtail.core.fields.StreamField([('page_button', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=255, required=False))])), ('embedded_poll', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('poll', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Poll']))])), ('embedded_survey', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('survey', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Survey']))])), ('embedded_quiz', wagtail.core.blocks.StructBlock([('direct_display', wagtail.core.blocks.BooleanBlock(required=False)), ('quiz', home.blocks.EmbeddedQuestionnaireChooserBlock(page_type=['questionnaires.Quiz']))])), ('article', wagtail.core.blocks.StructBlock([('display_section_title', wagtail.core.blocks.BooleanBlock(required=False)), ('article', wagtail.core.blocks.PageChooserBlock(page_type=['home.Article']))])), ('download', wagtail.core.blocks.StructBlock([('available_text', wagtail.core.blocks.CharBlock(help_text='This text appears when it is possible for the user to install the app on their phone.')), ('unavailable_text', wagtail.core.blocks.CharBlock(form_classname='red-help-text', help_text='This text appears when the user is using a feature phone and thus cannot install the app (the button will be disabled in this case). [Currently not implemented]', required=False)), ('offline_text', wagtail.core.blocks.CharBlock(help_text="This text appears when the user is navigating the site via the offline app and thus it doesn't make sense to install the offline app again (the button will be disabled in this case).", required=False)), ('page', wagtail.core.blocks.PageChooserBlock(page_type=['wagtailcore.Page'])), ('description', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image']))]))], blank=True, null=True),
        ),
    ]
