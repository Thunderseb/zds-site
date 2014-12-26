# coding: utf-8

from django.contrib.syndication.views import Feed
from django.conf import settings

from django.utils.feedgenerator import Atom1Feed

from models import PublishableContent
from zds.settings import ZDS_APP

class LastContentFeedRSS(Feed):
    """
    RSS feed for any type of content.
    """
    title = u"Contenu sur {}".format(settings.ZDS_APP['site']['litteral_name'])
    description = u"Les derniers contenus parus sur {}.".format(settings.ZDS_APP['site']['litteral_name'])
    link = ""
    content_type = None

    def items(self):
        """
        :return: The last (typically 5) contents (sorted by publication date). If `self.type` is not `None`, the contents will only
        be of this type.
        """
        contents = PublishableContent.objects.filter(sha_public__isnull=False)
        if self.content_type is not None:
            contents.filter(type=self.content_type)
        return contents.order_by('-pubdate')[:ZDS_APP['tutorial']['feed_length']]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.pubdate

    def item_description(self, item):
        return item.description

    def item_author_name(self, item):
        authors_list = item.authors.all()
        authors = []
        for authors_obj in authors_list:
            authors.append(authors_obj.username)
        authors = ", ".join(authors)
        return authors

    def item_link(self, item):
        return item.get_absolute_url_online()


class LastTutorialsFeedRSS(LastContentFeedRSS):
    """
    Redefinition of `LastContentFeedRSS` for tutorials only
    """
    content_type = "TUTORIAL"
    link = "/tutoriels/"
    title = u"Tutoriels sur {}".format(settings.ZDS_APP['site']['litteral_name'])
    description = u"Les derniers tutoriels parus sur {}.".format(settings.ZDS_APP['site']['litteral_name'])


class LastTutorialsFeedATOM(LastTutorialsFeedRSS):
    feed_type = Atom1Feed
    subtitle = LastTutorialsFeedRSS.description

class LastArticlesFeedRSS(Feed):
    title = u"Articles sur {}".format(settings.ZDS_APP['site']['litteral_name'])
    link = "/articles/"
    description = u"Les derniers articles parus sur {}.".format(settings.ZDS_APP['site']['litteral_name'])

    def items(self):
        return PublishableContent.objects\
            .filter(type="ARTICLE")\
            .filter(sha_public__isnull=False)\
            .order_by('-pubdate')[:5]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.pubdate

    def item_description(self, item):
        return item.description

    def item_author_name(self, item):
        authors_list = item.authors.all()
        authors = []
        for authors_obj in authors_list:
            authors.append(authors_obj.username)
        authors = ", ".join(authors)
        return authors

    def item_link(self, item):
        return item.get_absolute_url_online()


class LastTutorialsFeedATOM(LastArticlesFeedRSS):
    feed_type = Atom1Feed
    subtitle = LastTutorialsFeedRSS.description


class LastArticlesFeedRSS(LastContentFeedRSS):
    """
    Redefinition of `LastContentFeedRSS` for articles only
    """
    content_type = "ARTICLE"
    link = "/articles/"
    title = u"Articles sur {}".format(settings.ZDS_APP['site']['litteral_name'])
    description = u"Les derniers articles parus sur {}.".format(settings.ZDS_APP['site']['litteral_name'])


class LastArticlesFeedATOM(LastArticlesFeedRSS):
    feed_type = Atom1Feed
    subtitle = LastArticlesFeedRSS.description