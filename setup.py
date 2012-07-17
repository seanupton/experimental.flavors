from setuptools import setup, find_packages
import os

version = '0.1dev'

setup(name='experimental.flavors',
      version=version,
      description="Plone add-on for form definitions and form instances.",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='',
      author='Sean Upton',
      author_email='sean.upton@hsc.utah.edu',
      url='http://github.com/seanupton/experiemental.flavors',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['experimental'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.dexterity',
          'plone.behavior',
          'z3c.autoinclude',
          'Products.CMFPlone',
          # -*- Extra requirements: -*-
      ],
      extras_require = {
          'test': [ 'plone.app.testing>=4.0', ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )

