from setuptools import setup, find_packages

setup(  # noqa: E131
    name="ocds-TODO",
    long_description=__doc__,
    packages=find_packages(),
    entry_points='''
[babel.extractors]
codelists_text = ocds_sphinx_directives:codelists_extract
jsonschema_text = ocds_sphinx_directives:jsonschema_extract
''',
    # The dependency trees are determined by `pipdeptree -fl`
    install_requires=[
        # Build

        'sphinx-intl==0.9.9',
          'Babel==2.3.4',
            'pytz==2016.10',
          'click==6.7',
          'setuptools==38.4.0',
          'six==1.10.0',
          'Sphinx==1.5.1',
            'alabaster==0.7.10',
            'docutils==0.13.1',
            'imagesize==0.7.1',
            'Jinja2==2.9.5',
              'MarkupSafe==1.0',
            'Pygments==2.2.0',
            'requests==2.13.0',
            'snowballstemmer==1.2.1',
        'sphinxcontrib-jsonschema==0.9.4',  # see below
          'jsonpointer==1.10',
          'jsonref==0.1',
          'recommonmark==0.4.0',  # see below
            'CommonMark==0.5.4',
        'ocds_sphinx_directives==0.0.0',  # see below
        'sphinxcontrib-opendataservices==0.0.0',  # see below
        'standard_theme==0.0.0',  # see below

        # Tests

        'flake8==3.3.0',
          'mccabe==0.6.1',
          'pycodestyle==2.3.1',
          'pyflakes==1.5.0',

        # Utils

        'transifex-client',
    ],
    dependency_links=[
      'git+https://github.com/open-contracting/standard_theme.git@open_contracting#egg=standard_theme-0.0.0',
      'git+https://github.com/open-contracting/ocds_sphinx_directives.git@91b4de9d3e354db461ae93e65035b45738f56e15#egg=ocds_sphinx_directives-0.0.0',  # noqa: E501
      'git+https://github.com/jpmckinney/sphinxcontrib-jsonschema.git@f6614d5c1fd39cf7e7e908fd42b6b0f870f6d8cb#egg=sphinxcontrib-jsonschema-0.9.4',  # noqa: E501
      'git+https://github.com/OpenDataServices/sphinxcontrib-opendataservices.git@fab0ff0167d32ec243d42f272e0e50766299c078#egg=sphinxcontrib-opendataservices-0.0.0',  # noqa: E501
      'git+https://github.com/rtfd/recommonmark.git@81d7c6f7b37981ac22571dd91a7cc9d24c3e66a1#egg=recommonmark-0.4.0',
    ]
)
