import os

# Are we building in RTD?
on_rtd = os.environ.get("READTHEDOCS") == "True"


# matplotlib.use('agg')


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
    "sphinx_autodoc_typehints",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.mathjax",
    "sphinx.ext.intersphinx",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_new_tab_link",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

pygments_style = "gruvbox-light"
pygments_dark_style = "nord-darker"

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

source_parsers = {
    # '.md': 'recommonmark.parser.CommonMarkParser',
}

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "astr-480"
copyright = "{0}, {1}".format("2025-", "José Sánchez-Gallego")
author = "José Sánchez-Gallego"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The full version, including alpha/beta/rc tags.
release = "0.1.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "obj"

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# Intersphinx mappings
intersphinx_mapping = {}

autodoc_mock_imports = ["_tkinter"]
autodoc_member_order = "groupwise"
autodoc_default_options = {"members": None, "show-inheritance": None}
# autodoc_typehints = "description"

simplify_optional_unions = True
typehints_use_signature_return = True

# napoleon_use_rtype = False
# napoleon_use_ivar = True

copybutton_prompt_text = r">>> |\$ "
copybutton_prompt_is_regexp = True

myst_heading_anchors = 3
myst_enable_extensions = ["attrs_block", "colon_fence", "attrs_inline"]

new_tab_link_show_external_link_icon = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "furo"
html_title = "ASTR 480"
html_logo = "_static/UW_logo.png"
html_favicon = "./_static/favicon.ico"
html_theme_options = {
    "source_repository": "https://github.com/astr-480/astr-480-sp-25/",
    "source_branch": "main",
    "source_directory": "src/",
    "sidebar_hide_name": True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# See https://github.com/rtfd/readthedocs.org/issues/1776 for why we do this
if on_rtd:
    html_static_path = []
else:
    html_static_path = ["_static"]

html_css_files = [
    "styles.css",
]
