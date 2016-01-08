"""
Main Fabric File
"""

from fabric.api import local, task

import release
from bootstrap import bootstrap


# === Freeze ===
@task()
def freeze():
    """
    Shortcut for freezing the python package requirements
    """
    local("pip freeze > requirements.txt")


# === Setup ===
@task()
def setup():
    """
    Sets up the project locally
    """
    local('pip install -r requirements.txt')
