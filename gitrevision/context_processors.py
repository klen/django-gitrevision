from gitrevision.utils import GIT_REVISION


def gitrevision(request):
    """ Add current GIT_REVISION in context.
    """
    return dict(GIT_REVISION = GIT_REVISION)
