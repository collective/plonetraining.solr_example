# -*- coding: utf-8 -*-
from plone.dexterity.content import Item
from plonetraining.solr_example.interfaces import ITask
from zope.interface import implementer


@implementer(ITask)
class Task(Item):
    """ """
