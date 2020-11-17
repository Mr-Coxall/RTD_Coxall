# -*- coding: utf-8 -*-

import sys, os

sys.path.insert(0, os.path.abspath('extensions'))

#extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
#              'sphinx.ext.coverage', 'sphinx.ext.pngmath', 'sphinx.ext.ifconfig',
#              'epub2', 'autoimage', 'code_example']
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.todo', 'sphinx_tabs.tabs']

todo_include_todos = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
exclude_patterns = []
add_function_parentheses = True
#add_module_names = True
# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

project = u'qwerty'
copyright = u'2020, Mr. Coxall'

version = ''
release = ''

# -- Options for HTML output ---------------------------------------------------

#html_theme = 'book'
#html_theme_path = ['themes']
#html_title = "qwerty"
#html_short_title = None
html_logo = "images/cs-logo.png"
#html_favicon = None
#html_static_path = ['_static']
#html_domain_indices = False
#html_use_index = False
#html_show_sphinx = False
#htmlhelp_basename = 'MusicforGeeksandNerdsdoc'
#html_show_sourcelink = False




################################################################################


def setup(app):
     from sphinx.util.texescape import tex_replacements
     tex_replacements += [(u'♮', u'$\\natural$'),
                          (u'ē', u'\=e'),
                          (u'♩', u'\quarternote'),
                          (u'↑', u'$\\uparrow$'),
                          ]