# coding: utf-8

from crispy_forms.bootstrap import StrictButton
from crispy_forms.layout import Layout, ButtonHolder, Field, Div, HTML
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string


class CommonLayoutEditor(Layout):

    def __init__(self, *args, **kwargs):
        super(
            CommonLayoutEditor,
            self).__init__(
                Field('text', css_class='md-editor'),
                HelpMarkdown(),
                HTML("<div class='message-bottom'>"),
                HTML("<div class='message-submit'>"),
                StrictButton(
                    _(u'Envoyer'),
                    type='submit',
                    name='answer'),
                StrictButton(
                    _(u'Aperçu'),
                    type='submit',
                    name='preview',
                    css_class='btn-grey'),
                HTML("</div>"),
                HTML("</div>"),
            )


class CommonLayoutVersionEditor(Layout):

    def __init__(self, *args, **kwargs):
        super(
            CommonLayoutVersionEditor,
            self).__init__(
                Div(
                    Field('text', css_class='md-editor'),
                    Field('msg_commit'),
                    ButtonHolder(
                        StrictButton(
                            _(u'Envoyer'),
                            type='submit',
                            name='answer'),
                        StrictButton(
                            _(u'Aperçu'),
                            type='submit',
                            name='preview',
                            css_class='btn-grey'),
                    ),
                ),
            )


class CommonLayoutModalText(Layout):

    def __init__(self, *args, **kwargs):
        super(CommonLayoutModalText, self).__init__(
            Field('text'),
        )

class HelpMarkdown(object):

    def render(self, form, form_style, context):
        return render_to_string("forms/markdown_help.html")