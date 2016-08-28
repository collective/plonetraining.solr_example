# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetraining.solr_example


class PlonetrainingSolrExampleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetraining.solr_example)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetraining.solr_example:default')


PLONETRAINING_SOLR_EXAMPLE_FIXTURE = PlonetrainingSolrExampleLayer()


PLONETRAINING_SOLR_EXAMPLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETRAINING_SOLR_EXAMPLE_FIXTURE,),
    name='PlonetrainingSolrExampleLayer:IntegrationTesting'
)


PLONETRAINING_SOLR_EXAMPLE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETRAINING_SOLR_EXAMPLE_FIXTURE,),
    name='PlonetrainingSolrExampleLayer:FunctionalTesting'
)


PLONETRAINING_SOLR_EXAMPLE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETRAINING_SOLR_EXAMPLE_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonetrainingSolrExampleLayer:AcceptanceTesting'
)
