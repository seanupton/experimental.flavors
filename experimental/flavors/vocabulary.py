from five import grok
from zope.interface import implements, providedBy
from zope.interface.interfaces import IInterface
from zope.component import getUtilitiesFor
from zope.schema import getFieldNamesInOrder
from zope.schema.fieldproperty import FieldProperty
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

import interfaces


@grok.provider(IContextSourceBinder)
def available_flavors(context):
    """
    Filter all flavors registered by an intersection of interfaces provided
    by the context, return any matching flavors.
    
    Flavor names are dotted names of interfaces corresponding 1:1 with a
    behavior.
    """
    enumerated = getUtilitiesFor(interfaces.IFlavor)
    context_ifaces = set(providedBy(context).flattened())
    _term = lambda name, title: SimpleTerm(name, title=unicode(title))
    # trivia:   CPython's set intersection is effectively as efficient
    #           regardless of  relative size of first/second set.
    vocab = [
        _term(name, flavor.title or name) for name, flavor in enumerated
            if context_ifaces.intersection(flavor.interfaces)
        ]
    return vocab

