from zope.annotation.interfaces import IAnnotations

import interfaces


def flavor_aware_sync_flavors(context, event):
    """
    IObjectModifiedEvent handler for context providing
    IFlavorAware, copies the content_flavors saved on edit
    form into IFlavors['content_flavors'] adapter field to
    a distinct annotation.  This avoids "pulling the rug
    out from underneath" the content by removing a flavor
    that had behavior fields rendered into the edit form. The
    actual flavors used by the IBehaviorAssignable adapter
    in this package use the results of the last completed
    edit (saved by this handler), not the result of the
    in-progress save.
    """
    flavors = interfaces.IFlavors(context).content_flavors  # tuple of names
    anno = IAnnotations(context)
    anno[interfaces.FLAVORS_KEY] = flavors

