print '''
Installing stencil....
                         
 ____ _____ _____ _   _  ____ ___ _     
/ ___|_   _| ____| \ | |/ ___|_ _| |    
\___ \ | | |  _| |  \| | |    | || |    
 ___) || | | |___| |\  | |___ | || |___ 
|____/ |_| |_____|_| \_|\____|___|_____|
                                        
'''
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


import versioneer
import sys


config = {
    'description': 'stencil is a simple example python package',
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
