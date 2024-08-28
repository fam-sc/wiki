# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FAM Wiki'
copyright = '2024, FAM Student Council'
author = 'FAM Student Council'

master_doc = "index"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

language = 'uk_UA'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_title = project
html_static_path = ['_static']
html_theme_options = {
    "search_bar_text": "Пошук по вікі...",
    "show_nav_level": 4,
    "show_prev_next": False,
    "icon_links": [
        {
            "name": "Telegram",
            "url": "https://primat_kpi.t.me/",
            "icon": "fa-brands fa-telegram"
        }
    ],
}

html_css_files = [
    'styles.css',
]
