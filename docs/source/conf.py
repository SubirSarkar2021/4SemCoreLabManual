# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = '4th Sem Lab Computational Physics'
copyright = '2025, Dr. Subir Sarkar'
author = 'Dr. Subir Sarkar'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sphinx_rtd_theme

extensions = [
    'sphinx_rtd_theme',
    'nbsphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.autodoc',
]

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]


templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme' 
html_static_path = ['_static']


# Optional: suppress warnings about Jupyter kernel metadata
nbsphinx_allow_errors = True