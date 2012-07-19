from zope.interface import Interface, alsoProvides
from zope.interface.interfaces import IInterface
from zope import schema
from plone.dexterity.interfaces import IDexterityContent
from plone.directives import form

from vocabulary import available_flavors


class IFlavors(form.Schema):
    """
    Behavior for marking configured flavors.  It is informally assumed
    that the first flavor listed is a primary flavor, should that be
    meaningful to the application use-case.
    
    Flavors should ALWAYS be registered as utilities using the same
    dotted-name-of-interface identifier as the behavior for which they
    front.
    """
    
    form.fieldset(
        'settings',
        label='Settings',
        fields=('content_flavors',),
        )
    
    content_flavors = schema.Tuple(
        title=u'Content Flavors',
        description=u'Bind flavors of additional behaviors and fields to '\
                    u'this content item.',
        value_type=schema.Choice(
            source=available_flavors,
            ),
        default=(),
        required=False,
        )


alsoProvides(IFlavors, form.IFormFieldProvider)


class IFlavorAware(Interface):
    """Marker interface for flavor-aware content item instance"""


class IFlavor(Interface):
    """
    Metadata component describing a flavor.  Flavors should always be
    identified by the dotted name of the interface class of a behavior
    interface.
    
    The metadata described in this interface is primarily for display
    and selection interfaces, and is not necessary for enumeration of
    behaviors.  Components of this interface are typically registered
    as utilities for the purpose of vocabulary generation.
    """
    
    identifier = schema.Id(
        title=u'Interface identifier',
        description=u'Dotted name for interface identifier for behavior.',
        required=True,
        )
    
    title = schema.TextLine(
        title=u'Title',
        description=u'Display name for the flavor/behavior.',
        required=False,
        )
    
    description = schema.Text(
        title=u'Description',
        description=u'Described purpose, use of the flavor/behavior.',
        required=False,
        )
    
    icon = schema.BytesLine(
        title=u'Icon identifier',
        description=u'Path, name, or URI to an icon image.',
        required=False,
        )
    
    interfaces = schema.Tuple(
        title=u'Context interfaces',
        description=u'Tuple of interface objects for which this flavor '\
                    u'is applicable to extend.  Default is any flavor-'\
                    u'aware content type, but this may be narrowed.',
        default=(IFlavorAware,),
        )

