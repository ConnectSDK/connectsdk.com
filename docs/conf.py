# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_rtd_theme

import recommonmark
from recommonmark.transform import AutoStructify



# -- Project information -----------------------------------------------------

project = 'connectSDK'
author = 'LG Electronics'
copyright = '2020 LG Silicon Valley Lab. All Rights Reserved. All trademarks and logos beling to their respective owners.'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'recommonmark',
    'sphinx.ext.autosectionlabel',
    "sphinx_rtd_theme",
]

autosectionlabel_prefix_document = True

# html_logo = 'img/logo.svg'
# html_theme_options = {
#     'logo_only': True,
#     'display_version': False,
# }



# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
html_logo = '_static/image/logo.svg'
html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'sticky_navigation': True,
}
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# you have your own conf.py file, it overrides Read the Doc's default conf.py.
# By default, Sphinx expects the master doc to be contents.
# Read the Docs will set master doc to index instead (or whatever it is
# you have specified in your settings).
master_doc = 'index'

# for AutoStructify
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
