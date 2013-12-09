# coding: utf-8

import bleach
from django import template
from django.utils.safestring import mark_safe
import markdown
import time

import cssstyles


md_cssstyle = cssstyles.StyleExtension()

register = template.Library()

@register.filter('humane_time')
def humane_time(t, conf={}):
    tp = time.localtime(t)
    return time.strftime("%A %d %B %Y %H:%M:%S", tp)

@register.filter(needs_autoescape=False)
def emarkdown(value):
    # Allowed output tags from user raw HTML input and markdown generation
    allowed_tags = ['div', 'span', 'p', 'pre', 'hr', 'img', 'br',
                    'strong', 'em', 'i', 'b', 'code', 'sub', 'sup', 'del',
                    'a', 'abbr', 'blockquote',
                    'ul', 'ol', 'li',
                    'table', 'thead', 'tbody', 'tr', 'td', 'th']

    # Add h1…h6 titles, have a more beautiful way to do it?
    [allowed_tags.append('h{}'.format(i + 1)) for i in range(6)]

    allowed_attrs = {
        '*': ['class', 'id'],
        'a': ['href', 'title'],
        'img': ['src', 'alt'],
    }

    return mark_safe('<div class="markdown">{0}</div>'.format(
        bleach.clean(
            markdown.markdown(value, extensions=[
                              md_cssstyle,
                              'codehilite(force_linenos=True)',
                              'extra']),
            tags=allowed_tags,
            attributes=allowed_attrs)
        .encode('utf-8')))