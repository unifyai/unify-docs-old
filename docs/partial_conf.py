from typing import List
import os

# Retrieve html_theme_options from docs/conf.py
from docs.conf import html_theme_options, extensions, html_static_path

html_theme_options["navbar_end"] = ["theme-switcher", "navbar-icon-links"]
html_theme_options.pop("switcher", None)  # Version switcher shouldn't be in model hub
html_sidebars = {"**": ["custom-toc-tree"]}

extensions.append("sphinxcontrib.video")

# Add any paths that contain custom static files (such as style sheets) here, relative to this directory.
html_static_path.append('./demos/demos/videos/')



project = "Unify"
html_title = "Unify Documentation"

# Removing kapa.ai integration
html_js_files: List[str] = []
