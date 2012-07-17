from plone.behavior.interfaces import IBehavior
from plone.dexterity.behavior import DexterityBehaviorAssignable
from zope.component import adapts, queryUtility

import interfaces


class FlavorBehaviorAssignable(DexterityBehaviorAssignable):
    """
    Locally stored flavors for instance plus behaviors for FTI.
    
    Flavor names are behavior names: both reference the same dotted
    name of behavior interface, so enumeration can just use the
    flavor name without looking up an IFlavor utility to get
    metadata (since that metadata is for display, its primary use
    is in vocabularies, not here).
    """
    adapts(interfaces.IFlavorAware)
    
    def __init__(self, context):
        super(FlavorBehaviorAssignable, self).__init__(context)
        self.flavor_names = interfaces.IFlavors(self.context).flavors
    
    def enumerateBehaviors(self):
        behaviors = self.fti.behaviors + self.flavor_names
        for name in behaviors:
            behavior = queryUtility(IBehavior, name=name)
            if behavior is not None:
                yield behavior

