# This file is the same as the standard repository's, but removing `current_lang`-related prerequisites, removing
# "Pre-build" and Build" tasks, replacing `standard/docs/en` with `docs`, `standard/docs/locale` with `locale`, and
# removing `standard/`.

# See https://github.com/datamade/data-making-guidelines

# See http://clarkgrubb.com/makefile-style-guide#prologue
MAKEFLAGS += --warn-undefined-variables
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

# See http://clarkgrubb.com/makefile-style-guide#phony-target-arg
FORCE:

# The space-separated, period-prefixed translations to build (for easier substitutions).
TRANSLATIONS=.es .fr
# The source language and translations to build.
LANGUAGES=.en $(TRANSLATIONS)

# Directory of documentation files to build with Sphinx.
DOCS_DIR=docs
# Directory of catalog files.
CATALOGS_DIR=locale
# Directory in which to build documentation files.
BUILD_DIR=build
# Directory in which to build .pot files.
LOCALE_DIR=$(BUILD_DIR)/locale

# http://blog.jgc.org/2007/06/escaping-comma-and-space-in-gnu-make.html
COMMA := ,
SPACE :=
SPACE +=
COMMA_SEPARATED_TRANSLATIONS=$(subst $(SPACE),$(COMMA),$(TRANSLATIONS:.%=%))

# See http://clarkgrubb.com/makefile-style-guide#phony-targets
.PHONY: clean
clean:
	rm -rf $(BUILD_DIR)
	rm -rf docs/_static/codelists
	rm -f docs/_static/release-schema.json
	rm -f $(CATALOGS_DIR)/*/LC_MESSAGES/*.mo
	rm -f $(CATALOGS_DIR)/*/LC_MESSAGES/*/*.mo

### Message catalogs

$(LOCALE_DIR):
	mkdir -p $(LOCALE_DIR)

.PHONY: extract_codelists
extract_codelists: $(LOCALE_DIR)
	pybabel -q extract -F .babel_codelists . -o $(LOCALE_DIR)/codelists.pot

.PHONY: extract_schema
extract_schema: $(LOCALE_DIR)
	pybabel -q extract -F .babel_schema . -o $(LOCALE_DIR)/schema.pot

# The codelist CSV files and JSON Schema files must be present for the `csv-table-no-translate` and `jsonschema`
# directives to succeed, but the contents of the files have no effect on the generated .pot files.
# See http://www.sphinx-doc.org/en/stable/builders.html#sphinx.builders.gettext.MessageCatalogBuilder
.PHONY: extract_markdown
extract_markdown:
	sphinx-build -q -b gettext $(DOCS_DIR) $(LOCALE_DIR)

.PHONY: extract
extract: extract_codelists extract_schema extract_markdown

### Transifex

# Builds and pushes the .pot files (`source_file` in .tx/config) to Transifex.
.PHONY: push
push: extract
	tx push -s

# Also pushes the translation .po files (`file_filter` in .tx/config) to Transifex.
.PHONY: force_push_all
force_push_all: extract
	tx push -s -t -l $(COMMA_SEPARATED_TRANSLATIONS) -f --no-interactive

pull.%: FORCE
	tx pull -l $* -f

.PHONY: pull
pull:
	tx pull -l $(COMMA_SEPARATED_TRANSLATIONS) -f
