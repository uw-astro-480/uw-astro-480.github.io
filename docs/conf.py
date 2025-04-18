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

myst_enable_extensions = [
    "attrs_block",
    "colon_fence",
    "attrs_inline",
    "dollarmath",
    "amsmath",
    "strikethrough",
]
myst_heading_anchors = 3
myst_dmath_allow_labels = True

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
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/uw-astro-480/uw-astro-480.github.io/",
            "html": """
                <svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">
                    <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"></path>
                </svg>
            """,
            "class": "",
        },
    ],
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
