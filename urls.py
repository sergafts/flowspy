from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^fod/flowspy/', include('flowspy.foo.urls')),
    (r'^fod/poll/', include('flowspy.poller.urls')),
#    url(r'^fod/?$', 'flowspy.flowspec.views.user_routes', name="user-routes"),
    url(r'^fod/?$', 'flowspy.flowspec.views.group_routes', name="group-routes"),
    url(r'^fod/profile/?$', 'flowspy.flowspec.views.user_profile', name="user-profile"),
    url(r'^fod/add/?$', 'flowspy.flowspec.views.add_route', name="add-route"),
    #url(r'^fod/addrl/?$', 'flowspy.flowspec.views.add_rate_limit', name="add-rate-limit"),
    url(r'^fod/addport/?$', 'flowspy.flowspec.views.add_port', name="add-port"),
    url(r'^fod/edit/(?P<route_slug>[\w\-]+)/$', 'flowspy.flowspec.views.edit_route', name="edit-route"),
    url(r'^fod/delete/(?P<route_slug>[\w\-]+)/$', 'flowspy.flowspec.views.delete_route', name="delete-route"),
    url(r'^fod/login/?', 'flowspy.flowspec.views.user_login', name="login"),
    url(r'^fod/welcome/?', 'flowspy.flowspec.views.welcome', name="welcome"),
    url(r'^fod/logout/?', 'flowspy.flowspec.views.user_logout', name="logout"),
    (r'^fod/setlang/?$', 'django.views.i18n.set_language'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^fod/admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^fod/load_js/(?P<file>[\w\s\d_-]+)/$', 'flowspy.flowspec.views.load_jscript', name="load-js"), 

    # Uncomment the next line to enable the admin:
    (r'^fod/admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^fod/static/(?P<path>.*)', 'django.views.static.serve',\
            {'document_root':  settings.STATIC_URL}),
    )
