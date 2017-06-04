import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

setup(
    name='mezzanine-theme-moderna',
    version='0.1',
    url='https://github.com/mxposed/mezzanine-theme-moderna',
    description='Mezzanine CMS theme: Moderna',
    long_description=README,
    author='Jay Bird',
    author_email='a4blank@yahoo.com',
    license='MIT',
    packages=['moderna'],
    package_data=dict(moderna=package_files('moderna/static') + package_files('moderna/templates')),
    download_url='https://github.com/mxposed/mezzanine-theme-moderna/archive/v0.1.tar.gz',
)
