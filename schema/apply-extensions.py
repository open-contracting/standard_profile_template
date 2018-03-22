import os
import sys

from ocds_documentation_support import apply_extensions

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(basedir, '..', 'docs'))

from conf import extension_registry_git_ref  # noqa

apply_extensions(basedir, extension_registry_git_ref, 'TODO', [
])
