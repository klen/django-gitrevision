from git import Repo, InvalidGitRepositoryError


def gitrevision():
    try:
        return Repo().head.commit.hexsha

    except InvalidGitRepositoryError:
        return 'unknown'


# Calculate revision once at compile
GIT_REVISION = gitrevision()
