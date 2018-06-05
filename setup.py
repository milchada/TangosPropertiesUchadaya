from __future__ import absolute_import
install_requires = [
    'setuptools',
    'numpy >= 1.10.0',
    'sqlalchemy >= 1.0.10',
    'pyparsing >= 2.1.0',
    'WebOb >= 1.7.0rc2', # Response.has_body
    'repoze.lru >= 0.4', # py3 compat
    'zope.interface >= 3.8.0',  # has zope.interface.registry
    'zope.deprecation >= 3.5.0', # py3 compat
    'venusian >= 1.0a3', # ``ignore``
    'translationstring >= 0.4', # py3 compat
    'PasteDeploy >= 1.5.0', # py3 compat
    'plaster',
    'plaster_pastedeploy',
    'hupper',
    'six',
    ]

tests_require = [
    'nose >= 1.3.0',
    'pynbody >= 0.40'
    ]

from setuptools import setup, find_packages


setup(name='tangos-properties-uchadaya',
      version='1.0.dev0',
      description='Milas TANGOS properties',
      classifiers=[
          "Development Status :: 1 - Beta",
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Framework :: Pyramid",
          "License :: GNU Public License",
      ],
      author="Mila Chadayammuri",
      author_email="uchadaya@gmail.com",
      license="GNUv3",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite="nose.collector"
      )
