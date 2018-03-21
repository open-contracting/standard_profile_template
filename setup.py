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
        # Sphinx
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

        # sphinxcontrib-jsonschema
        'jsonpointer==1.10',
        'jsonref==0.1',
        'CommonMark==0.5.4',
    ],
    extras_require={
        'utils': [  # not pinned, not part of the build
            'transifex-client',
        ],
        'test': [
            'flake8==3.3.0',
              'mccabe==0.6.1',
              'pycodestyle==2.3.1',
              'pyflakes==1.5.0',
        ],
    },
)
