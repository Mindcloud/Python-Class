from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^recipes/$', 'recipes.views.index'),
    (r'^recipes/(?P<recipe_id>\d+)/$', 'recipes.views.detail'),
    (r'^recipes/category/$', 'recipes.views.category'),
    (r'^recipes/search/$', 'recipes.views.search'),
    (r'^recipes/search-form/$', 'recipes.views.search_form'),
    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
