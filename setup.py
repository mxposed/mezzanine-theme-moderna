import os
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

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
    download_url='https://github.com/mxposed/mezzanine-theme-moderna/archive/0.1.tar.gz',
)
