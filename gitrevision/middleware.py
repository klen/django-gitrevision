from gitrevision.utils import GIT_REVISION


class GitRevision():
    """ Simple add git revision attribute to request object.
    """
    def process_request(self, request):
        request.git_revision = GIT_REVISION
