# Compare this file to:
# https://github.com/open-contracting/standard_profile_template/blob/master/schema/apply-extensions.py

import os
import sys

from ocds_documentation_support import apply_extensions

basedir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(basedir, '..', 'docs'))

apply_extensions(basedir, 'TODO', {
    # 'extension_id_in_registry': 'version',
})
