"""
Fabric Commands Managing releases to Pypi
"""

from fabric.api import task, local


@task()
def deploy_test():
    """
    deploys repository to testing environment
    """
    local('python setup.py register -r pypitest')
    local('python setup.py sdist upload -r pypitest')


@task()
def deploy_prod():
    """
    deploys package to production pypi
    """
    local('python setup.py register -r pypi')
    local('python setup.py sdist upload -r pypi')
