from django.conf.urls.defaults import *
from storeathon.views import signup, tienda_new

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
     ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),

    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),
    ('^signup/$', 'storeathon.views.signup'),
    ('^store/(?P<slug>[-w]+)/$', 'storeathon.views.tienda'),
    ('^store/new/$', 'storeathon.views.tienda_new'),
)
