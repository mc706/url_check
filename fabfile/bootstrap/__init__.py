"""
Bootstrapping the project and development environment
"""
from fabric.api import task, local


# === bootstrap ===
@task(default=True)
def bootstrap():
    """
    Sets up git flow and git commit template
    """
    local('git config commit.template fabfile/bootstrap/git-commit-template.txt')
    local('git config gitflow.origin origin')
    local('git config gitflow.branch.master master')
    local('git config gitflow.branch.develop development')
    local('git config gitflow.prefix.feature feature/')
    local('git config gitflow.prefix.release release/')
    local('git config gitflow.prefix.hotfix hotfix/')
    local('git config gitflow.prefix.support support/')
    local('git config gitflow.prefix.versiontag v')
    local('git config branch.development.remote origin')
    local('git checkout -b development || git checkout development')