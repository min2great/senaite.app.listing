# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

version = "1.5.3rc11"

with open("docs/About.rst", "r") as fh:
    long_description = fh.read()

with open("docs/Changelog.rst", "r") as fh:
    long_description += "\n\n"
    long_description += "Changelog\n"
    long_description += "=========\n"
    long_description += fh.read()

setup(
    name="valer.core.listing",
    version=version,
    description="ReactJS powered listing tables for SENAITE LIMS",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope2",
    ],
    keywords=['senaite', 'lims', 'opensource', 'reactjs'],
    
    author="Valer Group LLC",
    author_email="valerio.zhang@valer.us",
    url="https://github.com/valeriozhang/senaite.core.listing",
    
    license="GPLv2",
    packages=find_packages("src", exclude=["ez_setup"]),
    package_dir={"": "src"},
    namespace_packages=["senaite", "senaite.core"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "valer.core>=1.3.5rc11",
    ],
    extras_require={
        "test": [
            "Products.PloneTestCase",
            "plone.app.testing",
            "unittest2",
        ]
    },
    entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
