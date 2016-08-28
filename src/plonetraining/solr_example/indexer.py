from plone.indexer import indexer
from plonetraining.solr_example.interfaces import ITask 

@indexer(ITask)
def fullname_indexer(obj):
    """ Construct a fullname for Solr from Dexterity fields """
    return getattr(obj, 'firstname', '') + ' ' + getattr(obj, 'sirname', '') 


