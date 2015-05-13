print '''
Installing stencil....

                         _
_._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
|  a    a    /              |
\   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
          
'''
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


import versioneer
import sys


config = {
    'description': 'Stencil is a simple example python package',
    'author': 'Jason Shiverick',
    'url': 'here',
    'download_url': 'Where to download it.',
    'author_email': 'jshiv00@gmail.com',
    'version': versioneer.get_version(),
    'cmdclass': versioneer.get_cmdclass(),
    
    'install_requires': [
    'numpy',
    'pandas',
    'nose',
    ],

    'packages': find_packages(),#['stencil'],
    'scripts': [],
    'name': 'stencil'
}



print "system is: "+sys.platform
print ''
print "installing stencil dependencies... "
print config['install_requires']

setup(**config)