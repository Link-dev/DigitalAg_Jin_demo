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
import os
import sys
import shlex
sys.path.insert(0, os.path.abspath('..'))
import recommonmark
from recommonmark.transform import AutoStructify

source_suffix = ['.rst', '.md']

# -- Project information -----------------------------------------------------

project = 'DigitalAg_Jin'
copyright = '2022, Junxiong Zhou'
author = 'Junxiong Zhou'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
    'recommonmark',
]

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The short X.Y version.
version = '0.1' #recommonmark.__version__
# The full version, including alpha/beta/rc tagss
release = version #recommonmark.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en_us'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Output file base name for HTML help builder.
htmlhelp_basename = 'Recommonmarkdoc'

# app setup hook
def setup(app):
    app.add_config_value('recommonmark_config', {
        #'url_resolver': lambda url: github_doc_root + url,
        'auto_toc_tree_section': 'Contents',
        'enable_math': False,
        'enable_inline_math': False,
        'enable_eval_rst': True,
        'enable_auto_doc_ref': True,
    }, True)
    app.add_transform(AutoStructify)