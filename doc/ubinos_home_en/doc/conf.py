# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


import pathlib
import sys
import os

source_path = os.path.join(pathlib.Path(__file__).parents[1].resolve().as_posix(), "source")
sys.path.insert(0, os.path.abspath(source_path))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ubinos'
copyright = 'Sungho Park'
author = 'Sungho Park'
release = '0.1'


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    ]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static', '../../ubinos_home_ko/doc/_static']


# -- Options for LaTeX output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-latex-output

latex_elements = {
    # kotex config
    'fontpkg': r'''
\usepackage{kotex}

''',
}
