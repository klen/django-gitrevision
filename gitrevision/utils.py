from git import Repo, InvalidGitRepositoryError

from django.conf import settings


def gitrevision():
    try:
        # specify GIT_PATH = os.path.dirname(__file__) in your settings.py 
        # if you get an InvalidGitRepositoryError
        path = getattr(settings, "GIT_PATH", None)
        return Repo(path).head.commit.hexsha

    except InvalidGitRepositoryError:
        return 'unknown'


# Calculate revision once at compile
GIT_REVISION = gitrevision()
