# -*- coding: utf-8 -*-
from plone import api
from plone.batching import Batch
from Products.Five import BrowserView


class FancySearchView(BrowserView):

    has_results = False

    def search(self):
        if not self.request.get('SearchableText'):
            return []
        catalog = api.portal.get_tool('portal_catalog')
        results = catalog(hl='true', **self.request.form)
        self.has_results = bool(len(results))
        b_start = self.request.get('b_start', 0)
        batch = Batch(results, size=20, start=b_start)
        return batch
