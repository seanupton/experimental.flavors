from zope.interface import Interface
from zope import schema
from zope.configuration import fields as config_fields
from zope.component.zcml import utility

from interfaces import IFlavor, IFlavorAware
from info import FlavorInfo


class IFlavorDirective(Interface):
    """
    Directive that registers a flavor a named IFlavor utility, named
    with the same interface dotted name for the behavior the flavor
    represents.
    """
    
    title = config_fields.MessageID(
        title=u'Title',
        description=u'A display label and readable title for flavor.',
        required=True,
        )
    
    description = config_fields.MessageID(
        title=u'Description',
        description=u'More detailed description of what flavor provides.',
        required=False,
        )
    
    behavior = config_fields.GlobalObject(
        title=u'Behavior interface',
        description=u'The interface of the behavior that flavor provides.',
        required=True,
        )
    
    for_ = config_fields.Tokens(
        title=u'Flavor contexts',
        description=u'List of interfaces for which the flavor applies. '\
                    u'At the time of this writing, plone.behavior only '\
                    u'supports a singular interface, so any multiple '\
                    u'interfaces specified here should share a common '\
                    u'parent class in an interface specified in '\
                    u'behavior.  If this is not supplied in directive, '\
                    u'plone.dexterity.interfaces.IDexterityContent '\
                    u'should be used as a context.',
        required=False,
        value_type=config_fields.GlobalObject(
            missing_value=object(),
            )
        )
    
    icon = config_fields.MessageID(
        title=u'Icon',
        description=u'Path, name, or URI to icon for flavor.',
        required=False,
        )


def flavorDirective(
        _context,
        title,
        behavior,
        description=None,
        for_=None,
        icon=None,
        ):
    info = FlavorInfo(behavior)
    info.title = title
    info.description = description
    info.icon = icon
    if for_:
        info.interfaces = for_
    else:
        info.interfaces = (IFlavorAware,)
    
    # register a utility, used in vocabularies of flavors:
    utility(
        _context,
        provides=IFlavor,
        name=info.identifier,
        component=info,
        )


