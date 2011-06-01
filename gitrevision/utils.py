from git import Repo, InvalidGitRepositoryError

from gitrevision import settings


def gitrevision():
    try:
        # specify GIT_PATH = os.path.dirname(__file__) in your settings.py
        # if you get an InvalidGitRepositoryError
        return Repo(settings.GIT_PATH).head.commit.hexsha

    except InvalidGitRepositoryError:
        return 'unknown'


# Calculate revision once at compile
GIT_REVISION = gitrevision()
