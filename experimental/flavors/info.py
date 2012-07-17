from zope.interface import implements
from zope.interface.interfaces import IInterface
from zope.schema import getFieldNamesInOrder
from zope.schema.fieldproperty import FieldProperty
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

import interfaces


class FlavorInfo(object):
    implements(interfaces.IFlavor)
    
    # field property descriptors, provides validation and default values:
    identifier = FieldProperty(interfaces.IFlavor['identifier'])
    title = FieldProperty(interfaces.IFlavor['title'])
    description = FieldProperty(interfaces.IFlavor['description'])
    icon = FieldProperty(interfaces.IFlavor['icon'])
    interfaces = FieldProperty(interfaces.IFlavor['interfaces'])
    
    def __init__(self, schema, **kwargs):
        self.identifier = str(schema)
        if IInterface.providedBy(schema):
            self.identifier = self.schema.__identifier__
        for name in getFieldNamesInOrder(interfaces.IFlavor):
            if name in kwargs:
                setattr(self, name, kwargs.get(name))

