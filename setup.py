import os
from setuptools import setup, find_packages

version = '0.1'

setup(name='shiji.theme',
      version=version,
      description="ShiJi Theme",
      long_description=open("README.rst").read() + "\n\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),    

      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        ],
      keywords='web zope plone theme diazo',
      author='TsungWei Hu',
      author_email='marr.tw@gmail.com',
      url='http://themes.quintagroup.com/product/sunrain',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['shiji'],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'plone.app.theming',
                        'plone.app.themingplugins',
                        ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
