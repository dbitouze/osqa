from forum.settings import EXT_KEYS_SET
from forum.settings.base import Setting
from django.utils.translation import ugettext_lazy as _

FB_API_KEY = Setting('FB_API_KEY', '', EXT_KEYS_SET, dict(
label = _("Facebook API key"),
help_text = _("""
Get this key at the <a href="http://www.facebook.com/developers/">Facebook developers network</a> to enable
authentication in your site through facebook.
"""),
required=False))

FB_APP_SECRET = Setting('FB_APP_SECRET', '', EXT_KEYS_SET, dict(
label = _("Facebook APP secret"),
help_text = _("""
This your facebook app secret that you'll get in the same place as the API key.
"""),
required=False))
