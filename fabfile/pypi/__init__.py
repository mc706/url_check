"""
Fabric Commands Managing releases to Pypi
"""

from fabric.api import task, local
import shutil

@task(default=True)
def deploy():
    """
    deploys package to production pypi
    """
    local('python setup.py bdist_wheel')
    local('twine upload dist/*')
    shutil.rmtree('build')
    shutil.rmtree('dist')
    shutil.rmtree('webmon.egg-info')
