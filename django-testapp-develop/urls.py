from django.conf.urls.defaults import *
from storeathon.views import signup, tienda_new

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
     ('^$', 'django.views.generic.simple.direct_to_template',
     {'template': 'home.html'}),

    ('^login/$', 'django.contrib.auth.views.login'),
    ('^logout/$', 'django.contrib.auth.views.logout'),
    ('^signup/$', 'storeathon.views.signup'),
    
    ('^store/(?P<slug>[-\w]+)$', 'storeathon.views.tienda'),
    ('^store/new/$', 'storeathon.views.tienda_new'),

    ('^item/new/$', 'storeathon.views.item_new'),
    ('^item/(?P<slug>[-\w]+)$', 'storeathon.views.item'),

    ('^categoria/new/$', 'storeathon.views.categoria_new'),
    ('^categoria/list/$', 'storeathon.views.categoria_list'),

    ('^kart/add/(?P<slug>[-\w]+)$', 'storeathon.views.kart_add'),
    ('^kart/remove/(?P<slug>[-\w]+)$', 'storeathon.views/kart_remove'),
    ('^kart/$', 'storeathon.views.kart'),
    ('^kart/remove/all', 'storeathon.views.kart_remove_all'),
    ('^kart/checkout/$', 'storeathon.views.kart_checkout'),
)
