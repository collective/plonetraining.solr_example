# -*- coding: utf-8 -*-
from plone import api
from plone.app.contentlisting.interfaces import IContentListing
from plone.batching import Batch
from Products.Five import BrowserView
from urllib import urlencode
from zope.component import getMultiAdapter
import json


class FancySearchView(BrowserView):

    has_results = False

    def search(self):
        if not self.request.get('SearchableText'):
            return []
        catalog = api.portal.get_tool('portal_catalog')
        results = IContentListing(catalog(hl='true', **self.request.form))
        self.has_results = bool(len(results))
        b_start = self.request.get('b_start', 0)
        batch = Batch(results, size=20, start=b_start)
        return batch

    def suggest(self):
        self.request.form['term'] = self.request.get('SearchableText')
        suggest_view = getMultiAdapter((self.context, self.request),
                                       name='suggest-terms')
        suggestions = json.loads(suggest_view())
        if suggestions:
            word = suggestions[0]['value']['word']
            query = self.request.form.copy()
            query['SearchableText'] = word
            return {'word': word,
                    'url': '{0}?{1}'.format(self.request.getURL(),
                                            urlencode(query, doseq=1))}
        return ''
