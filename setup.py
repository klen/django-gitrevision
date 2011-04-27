import os

from setuptools import setup, find_packages

from gitrevision import version, PROJECT, LICENSE


MODULE_NAME = 'gitrevision'

def read( fname ):
    try:
        return open( os.path.join( os.path.dirname( __file__ ), fname ) ).read()
    except IOError:
        return ''


META_DATA = dict(
    name = PROJECT,
    version = version,
    description = read('DESCRIPTION'),
    long_description = read('README.rst'),
    license=LICENSE,

    author = "Kirill Klenov",
    author_email = "horneds@gmail.com",
    url = "http://github.com/klen/django-gitrevision.git",

    keywords= 'git django',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python',
    ],

    packages = find_packages(),

    install_requires = [ 'gitpython' ],
)

if __name__ == "__main__":
    setup( **META_DATA )
