from forum.settings.base import Setting, SettingSet
from django.forms.widgets import Textarea
from django.core.urlresolvers import reverse
from forum.settings import APP_URL
from django.utils.translation import ugettext_lazy as _

ROBOTS_SET = SettingSet('robots', _('Robots txt'), _("Set up the robots.txt file."), 3000)

ROBOTS_FILE = Setting('ROBOTS_FILE',
"""Sitemap: %s/sitemap.xml

User-Agent: *
Disallow: /accounts/
Disallow: /users/
Disallow: /revisions/
Disallow: /search
Disallow: /matching_tags
Disallow: /*sort=
""" % APP_URL, ROBOTS_SET, dict(
label = _("Robots.txt file"),
help_text = _("""
The robots.txt file search engine spiders will see.
"""),
widget=Textarea(attrs={'rows': '20'})))