# -*- coding: utf-8 -*-

from __future__ import unicode_literals, division, absolute_import
from django.contrib.sitemaps import Sitemap
from django.db.models import Max
from ishappening.models import Document


class DocumentsSitemap(Sitemap):
    limit = 800
    changefreq = "daily"

    def items(self):
        self.approx_traffic_max = Document.objects.aggregate(Max('approx_traffic'))['approx_traffic__max']
        return Document.objects.all().only('timestamp_modified', 'approx_traffic')

    def lastmod(self, obj):
        return obj.timestamp_modified

    def location(self, obj):
        return obj.get_absolute_url()

    def priority(self, obj):
        return obj.approx_traffic / self.approx_traffic_max


sitemap_dict = {
    'documents': DocumentsSitemap
}