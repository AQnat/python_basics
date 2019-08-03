from github import Github

from src.local_settings import GITHUB_ACCESS_TOKEN


class GithubApi:
    """
    Facade for PyGithub
    """
    def __init__(self):
        self._g = Github(GITHUB_ACCESS_TOKEN)

    def get_user_repositories(self, user_id):
        return self._g.get_user(user_id).get_repos()

    def get_repository_topics(self, repo_id):
        repo = self._g.get_repo(repo_id)
        return repo.get_topics()
Collapse