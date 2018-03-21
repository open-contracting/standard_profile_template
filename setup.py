# This file is the same as the standard repository's, but removing `standard.`.

from setuptools import setup, find_packages

setup(
    name="ocds-TODO",
    long_description=__doc__,
    packages=find_packages(),
    entry_points="""
        [babel.extractors]
        jsonschema_text = schema.utils.jsonschema_extract:extract
        codelists_text = schema.utils.codelists_extract:extract
        """
)
