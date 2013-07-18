from setuptools import setup
from os.path import join, dirname

import gawande 

setup(name='gawande',
      version = gawande.__version__,
      author = gawande.__author__ , 
      author_email = gawande.__email__,
      url = 'http://github.com/johnjosephhorton/gawande',
      packages = [''],
      package_data = {'':['*.md', 'checklists/*.md']},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['gawande = gawande:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      install_requires=['Jinja2>=2.6'],
      )
