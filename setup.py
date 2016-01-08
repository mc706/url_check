from setuptools import setup
import re

## Get the release number
VERSIONFILE = 'webmon/_version.py'
with open(VERSIONFILE, 'rt') as vsf:
    version_string = vsf.read()
version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
match = re.search(version_regex, version_string, re.M)
if match:
    version = match.group(1)
    major, minor, patch = version.split('.')
    release = "{0}.{1}".format(major, minor)
else:
    raise RuntimeError('Unable to find version string in {0}'.format(VERSIONFILE))

## setup
setup(
    name='webmon',
    version=version,
    url='https://github.com/mc706/webmon',
    author='Ryan McDevitt',
    author_email='mcdevitt.ryan@gmail.com',
    license='MIT License',
    packages=['webmon'],
    include_package_data=True,
    description='Monitor websites for visual changes',
    download_url='https://github.com/mc706/webmon/tarball' + release,
    keywords=['web monitoring', 'screenshots', 'website diff'],
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Communications :: Email",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    install_requires=[
        'click',
        'configparser',
        'Pillow',
        'splinter',
        'colorama',
    ],
    entry_points='''
        [console_scripts]
        webmon=webmon.main:run
    '''
)