class UrlsUpdateSource:
    def __init__(self):
        self.urls_import = [
"""
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
"""
        ]

        self.system_info = [
"""
admin.site.site_header = "<_REPLACE_DATA>"
""",
"""
admin.site.site_title = "<_REPLACE_DATA>"
""",
"""
admin.site.index_title = "<_REPLACE_DATA>"
"""
        ]

        self.urls_patterns = [
"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""
        ]
