from Products.Five import BrowserView
from plone.batching import Batch
from plone import api

class FancySearchView(BrowserView):

    has_results = False

    def search(self):
        catalog = api.portal.get_tool('portal_catalog')
        SearchableText = self.request.get('SearchableText', '')
        if not SearchableText:
            return []
        results = catalog(SearchableText=SearchableText, hl='true')
        self.has_results = bool(len(results))
        b_start = self.request.get('b_start', 0)
        batch = Batch(results, size=20, start=b_start)
        return batch

