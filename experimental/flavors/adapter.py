from plone.behavior.interfaces import IBehavior
from plone.dexterity.behavior import DexterityBehaviorAssignable
from zope.annotation.interfaces import IAnnotations
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
        self.flavor_names = []
        KEY = 'experimental.flavors.interfaces.IFlavors.content_flavors'
        self.context = context
        super(FlavorBehaviorAssignable, self).__init__(context)
        anno = IAnnotations(context)
        if KEY in anno:
            self.flavor_names = list(anno.get(KEY))
    
    def enumerateBehaviors(self):
        behaviors = list(self.fti.behaviors) + self.flavor_names
        for name in behaviors:
            behavior = queryUtility(IBehavior, name=name)
            if behavior is not None:
                yield behavior

