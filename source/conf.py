# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
import git
import semver
import sphinx

from sphinx_revealjs.themes import get_theme_path as revealjs_theme_path
from sphinx_rtd_theme import get_html_theme_path as rtd_theme_path


# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# sys.path.insert(0, os.path.abspath('.'))

logcfg = sphinx.util.logging.getLogger(__name__)
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
on_windows = sys.platform.startswith('win')

if "DOCSRC" not in os.environ:
    DOCSRC = os.path.abspath(os.getcwd())
else:
    DOCSRC = os.path.abspath(os.environ["DOCSRC"])

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# Preselect different manifest and meta data for specific brandings
if tags.has('mpulnx'):    # pylint: disable=undefined-variable
    branding = 'mpulnx'
    publisher = 'UL Method Park GmbH and Navimatix GmbH'
    author = 'TiaC Systems Team'
    docnumb = 'MPNX-TST-2306001'
    contactaddr = 'Erlangen / Jena, Germany'
    contactemail = 'info@tiac-systems.net'
    contactweb = 'https://tiac-systems.net'
elif tags.has('mpul'):    # pylint: disable=undefined-variable
    branding = 'mpul'
    publisher = 'UL Method Park GmbH'
    author = 'IoT Labs Team'
    docnumb = 'MP-QMS-2306001'
    contactaddr = 'Erlangen, Germany'
    contactemail = 'info@methodpark.de'
    contactweb = 'https://methodpark.de'
elif tags.has('nx'):      # pylint: disable=undefined-variable
    branding = 'nx'
    publisher = 'Navimatix GmbH'
    author = 'IoT Engineering Team'
    docnumb = 'NX-QMS-2306001'
    contactaddr = 'Jena, Germany'
    contactemail = 'info@navimatix.de'
    contactweb = 'https://navimatix.de'
else:
    branding = 'tiac'
    publisher = 'TiaC Systems'
    author = 'Consulting Team'
    docnumb = 'TIAC-DOC-2306001'
    contactaddr = 'Jena, Germany'
    contactemail = 'info@tiac-systems.net'
    contactweb = 'https://tiac-systems.net'

project = 'A Bridle for Your Kite'
headline = 'Best Practices for Downstream Development with Zephyr'
category = 'Presentation'
doctype = 'Handbook'
docstat = 'preliminary (:emphasis:`some mature, much in progress`)'
copyright = '2022‒2023 ' + publisher + ' and individual contributors'
about = project + ' – ' + doctype + '.'
keywords = docnumb + ',' + doctype + ',' + project + ',Zephyr,Bridle'

# Preselect different DeckTape parameters for specific content
if not tags.has('with_more_notyet'):  # pylint: disable=undefined-variable
    decktape_slides = '1-60'
    decktape_pause ='10'  # milliseconds, set to 32000 if needed / final
else:
    decktape_slides = '1-60'
    decktape_pause ='10'  # milliseconds, set to 32000 if needed / final

decktape_size = '1125x795'  # DIN A4
# decktape_size = '1590x1125'  # DIN A3

# Define basic strings that will be used in the dictionary of external sites.
# gxp/GXP stands for GitX (Hub/Lab) Pages
gxp_base = 'https://github.com/tiacsys/'
gxp_slug = 'zds23-bridlekite'
gxp_name = publisher + ', ' + doctype + ', ' + project

if on_rtd:
    git_describe = ('--dirty=+RTDS', '--broken=+broken')
else:
    git_describe = ('--dirty=+dirty', '--broken=+broken')

try:
    repo = git.Repo(search_parent_directories=True)
    semv = semver.VersionInfo.parse(repo.git.describe(git_describe))
    sha1 = repo.head.object.hexsha.lower()
except:
    # fallback to unknown version / release
    semv = semver.VersionInfo.parse('0.0.0-invalid+unknown')
    sha1 = '0000000000000000000000000000000000000000'

# The short SHA1 for identification
identify = repo.git.rev_parse(sha1, short=8)

# The short X.Y.Z version
version = str(semv.finalize_version())
genvers = str(semv.major)

# The full version, including alpha/beta/rc tags
release = str(semv)

# Combined document title and subtitle
# title = project + ' ' + version
title = project
subtitle = doctype

# Single target file names
namespace = 'net.tiac-systems.doc.presentation.template.spxrjs.zds.' + version + '.'
basename = 'zds23-bridlekite'

logcfg.info(project + ' ' + release, color='yellow')

# Define external webfont server
wfs_base = 'https://tiacsys.github.io/'
wfs_slug = 'sphinx_static/fonts'
wfs_addr = wfs_base + wfs_slug

# -- Specific configuration --------------------------------------------------

if (tags.has('latex') or tags.has('latexpdf')) and not tags.has('html'):
    tags.add('with_indexlol')
    tags.add('with_indexlot')
    tags.add('with_indexlof')
    tags.add('with_indexloe')
    tags.add('with_indexloi')

if tags.has('html') and not (tags.has('latex') or tags.has('latexpdf')):
    tags.add('with_indexlod')
    tags.add('with_indexloi')

logcfg.info('Build with tags: ' + ':'.join(map(str, tags)), color='red')

logcfg.info('Themes for:', color='yellow')

path_rtd_theme = os.path.join(rtd_theme_path(), 'sphinx_rtd_theme')
logcfg.info('-- HTML    path is: "{}"'.format(path_rtd_theme), color='yellow')

path_revealjs_theme = revealjs_theme_path('sphinx_revealjs')
path_revealjs_sass =os.path.join(path_revealjs_theme, 'static', 'revealjs4', 'css', 'theme')
logcfg.info('-- Reveal  path is: "{}"'.format(path_revealjs_theme), color='yellow')
logcfg.info('-- SASS include is: "{}"'.format(path_revealjs_sass), color='yellow')

path_extra = os.path.join(DOCSRC, '_extra')
logcfg.info('EXTRAS     path is: "{}"'.format(path_extra), color='green')

path_images = os.path.join(DOCSRC, '_images')
logcfg.info('IMAGES     path is: "{}"'.format(path_images), color='green')

path_videos = os.path.join(DOCSRC, '_videos')
logcfg.info('VIDEOS     path is: "{}"'.format(path_videos), color='green')

path_templates = os.path.join(DOCSRC, '_templates')
logcfg.info('TEMPLATE   path is: "{}"'.format(path_templates), color='green')

path_html_templates = os.path.join(path_templates, 'html')
logcfg.info('-- HTML    path is: "{}"'.format(path_html_templates), color='green')

path_revealjs_templates = os.path.join(path_templates, 'revealjs')
logcfg.info('-- Reveal  path is: "{}"'.format(path_revealjs_templates), color='green')

path_latex_templates = os.path.join(path_templates, 'latex')
logcfg.info('-- LaTeX   path is: "{}"'.format(path_latex_templates), color='green')

path_dictionaries = os.path.join(path_templates, 'dicts')
logcfg.info('DICTS      path is: "{}"'.format(path_dictionaries), color='green')

path_static = os.path.join(DOCSRC, '_static')
logcfg.info('STATIC     path is: "{}"'.format(path_static), color='green')

path_bibtex = os.path.join(DOCSRC, '_bibliography')
logcfg.info('BibTeX     path is: "{}"'.format(path_bibtex), color='green')

logcfg.info('Web Font   addr is: "{}"'.format(wfs_addr), color='green')

addr_dejavu = '/'.join([wfs_addr, 'DejaVu'])
logcfg.info('    DejaVu addr is: "{}"'.format(addr_dejavu), color='green')

addr_wenquanyi = '/'.join([wfs_addr, 'WenQuanYi'])
logcfg.info(' WenQuanYi addr is: "{}"'.format(addr_wenquanyi), color='green')

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

build_sphinx = sphinx.__version__

needs_sphinx = '5.3.0'
needs_extensions = {
    'sphinx.ext.autosectionlabel':                  needs_sphinx,
    'sphinx.ext.extlinks':                          needs_sphinx,
    'sphinx.ext.ifconfig':                          needs_sphinx,
    'sphinx.ext.intersphinx':                       needs_sphinx,
    'sphinx.ext.todo':                              needs_sphinx,
#   'sphinx_immaterial':                            '0.11.0',      # versioning not (yet) supported
    'sphinx_revealjs':                              '2.4.1',
#   'sphinx_rtd_theme':                             '1.1.1',       # versioning not (yet) supported
    'sphinxcontrib.bibtex':                         '2.5.0',
    'sphinxcontrib.spelling':                       '7.7.0',
#   'sphinxcontrib.sass':                           '0.3.4',       # versioning not (yet) supported
    'sphinxcontrib.svgbob':                         '0.2.1',
#   'sphinxcontrib.video':                          '0.0.1',       # versioning not (yet) supported
#   'sphinxext.remoteliteralinclude':               '0.4.0',       # versioning not (yet) supported
    'sphinx_selective_exclude.eager_only':          '1.0.2',
    'sphinx_selective_exclude.modindex_exclude':    '1.0.2',
    'sphinx_selective_exclude.search_auto_exclude': '1.0.2',
    'oembedpy.ext.sphinx':                          '0.4.0',
}

extensions = [
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.extlinks',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
#   'sphinx_immaterial',  # The Sphinx immaterial HTML theme needs more evaluation.
    'sphinx_revealjs',
    'sphinx_rtd_theme',
    'sphinxcontrib.bibtex',
    'sphinxcontrib.spelling',
    'sphinxcontrib.sass',
    'sphinxcontrib.svgbob',
    'sphinxcontrib.video',
    'sphinxext.remoteliteralinclude',
    'sphinx_selective_exclude.eager_only',
    'sphinx_selective_exclude.modindex_exclude',
    'sphinx_selective_exclude.search_auto_exclude',
    'oembedpy.ext.sphinx',
]

# Use additional Sphinx extensions for HTML/Reveal.js builder
if tags.has('html') or tags.has('revealjs'):  # pylint: disable=undefined-variable
#   needs_extensions['sphinxcontrib.imagesvg'] = '0.1.0'  # versioning not (yet) supported
    extensions.append('sphinxcontrib.imagesvg')
    needs_extensions['sphinxcontrib.asciinema'] = '0.3.5'
    extensions.append('sphinxcontrib.asciinema')

# Use additional Sphinx extensions for LaTeX/PDF builder
if tags.has('latex') or tags.has('latexpdf'):  # pylint: disable=undefined-variable
#   needs_extensions['sphinxcontrib.inkscapeconverter'] = '1.2.1'
#   extensions.append('sphinxcontrib.inkscapeconverter')
    needs_extensions['sphinxcontrib.rsvgconverter']     = '1.2.1'
    extensions.append('sphinxcontrib.rsvgconverter')
#   needs_extensions['sphinxcontrib.cairosvgconverter'] = '1.2.1'
#   extensions.append('sphinxcontrib.cairosvgconverter')

# Use different template description in case of Reveal.js builder
if tags.has('revealjs'):    # pylint: disable=undefined-variable
    templates_path = [
        '{}'.format(path_revealjs_templates),
    ]
else:
    templates_path = [
        '{}'.format(path_html_templates),
        '{}'.format(path_latex_templates),
    ]

exclude_patterns = [
    '**/.gitkeepdir',
    '**/*.rst.svgbob',
    '**/*.drawio',
    'fonts*',
    'exercises/toyproject*',
]

# Exclude pattern when read-the-docs not envolved
if tags.has('without_rtd'):  # pylint: disable=undefined-variable
    exclude_patterns.append('rtd.rst')
    exclude_patterns.append('rtd/**')
    exclude_patterns.append('rtd')

# Exclude pattern when thanks not envolved
if tags.has('without_thanks'):  # pylint: disable=undefined-variable
    exclude_patterns.append('thanks.rst')
    exclude_patterns.append('thanks/**')
    exclude_patterns.append('thanks')

logcfg.info('exclude pattern is: "{}"'.format(exclude_patterns), color='red')

# Use different master toctree document in case of Reveal.js builder
master_doc = 'index'
if tags.has('revealjs'):    # pylint: disable=undefined-variable
    source_suffix = {
        # toctree entries will be filtered out by Reveal.js builder
        # all content have to be include but toctree entries already
        # needed for glossary terms and bibliography references
        '.rstr': 'restructuredtext',
    }
    # Suppress arbitrary warning messages.
    suppress_warnings = [
        # Reveal.js does not support document tructuring by toctree, only
        # include directives can handle multiple artifact files. So it is
        # an common problem, that exactly the same header string will occure
        # multiple time on the level of the master_doc file.
        "autosectionlabel.**/revealjs",
        "autosectionlabel.index",
    ]
else:
    source_suffix = {
        '.rst': 'restructuredtext',
    }

# Generate dynamic toctrees
with open('gentoctree.rsti.in', 'r+') as t:
    with open('gentoctree.rsti', 'w') as g:
        dynamic_toctree = t.read().format(
            rtd = 'rtd/index' if not tags.has('without_rtd') else '',
            thanks = 'thanks/index' if not tags.has('without_thanks') else '',
            indexlol = 'indexlol' if tags.has('with_indexlol') else '',
            indexlot = 'indexlot' if tags.has('with_indexlot') else '',
            indexlof = 'indexlof' if tags.has('with_indexlof') else '',
            indexloe = 'indexloe' if tags.has('with_indexloe') else '',
            indexlod = 'indexlod' if tags.has('with_indexlod') else '',
            indexloi = 'indexloi' if tags.has('with_indexloi') else '',
        )
        g.write(dynamic_toctree)

language = 'en'
default_role = 'any'
pygments_style = 'sphinx'
show_authors = True

if tags.has('revealjs'):
    numfig = False
else:
    numfig = True

numfig_secnum_depth = 1
numfig_format = {
    'code-block': 'Listing %s',
    'sections': 'Section %s',
    'figure': 'Figure %s',
    'table': 'Table %s',
}

math_numfig = True
math_number_all = True
math_eqref_format = 'Equation {number}'

user_agent = 'Mozilla/5.0 AppleWebKit/537.36 Chrome/87.0.4280.88 Safari/537.36'
linkcheck_retries = 5
linkcheck_timeout = 60
linkcheck_workers = 10
linkcheck_anchors = False
linkcheck_ignore = [
    'https://www.reportlab.com/dev/docs/',
    'https://github.com/tiacsys/zds23-bridlekite/',
    'http://localhost:\d+/',
]

rst_prolog = u'''
.. include:: /{docsrc}/docroles.rsti
.. include:: /{docsrc}/docmeta.rsti
.. |CREDITS| replace:: :download:`CREDITS </CREDITS>`
.. |LICENSE| replace:: :download:`LICENSE </LICENSE>`
.. |docsrc| replace:: {docsrc}
.. |docstat| replace:: {docstat}
.. |docnumb| replace:: {docnumb}
.. |genvers| replace:: {genvers}
.. |identify| replace:: {identify}
.. |title| replace:: {title}
.. |subtitle| replace:: {subtitle}
.. |headline| replace:: {headline}
.. |publisher| replace:: {publisher}
.. |copyright| replace:: {copyright}
.. |project| replace:: {project}
.. |author| replace:: {author}
.. |about| replace:: {about}
.. |contactaddr| replace:: {contactaddr}
.. |contactemail| replace:: {contactemail}
.. |contactweb| replace:: {contactweb}
.. |gxp_name| replace:: {gxp_name}
.. |gxp_name_e| replace:: :emphasis:`{gxp_name}`
.. |gxp_name_s| replace:: :strong:`{gxp_name}`
.. meta::
   :producer: {producer}
   :creator: {creator}
   :publisher: {publisher}
   :subject: {subject}
   :keywords: {keywords}
   :author: {author}
   :copyright: {copyright}
   :docstat: {docstat}
   :docnumb: {docnumb}
   :project: {project}
   :title: {title}
   :subtitle: {subtitle}
   :headline: {headline}
   :version: {version}
   :release: {release}
   :identify: {identify}
'''.format(
    docsrc = DOCSRC,
    docstat = docstat,
    docnumb = docnumb,
    genvers = genvers,
    version = version,
    identify = identify,
    release = release,
    title = title,
    subtitle = subtitle,
    headline = headline,
    copyright = copyright,
    project = project,
    author = author,
    about = about,
    contactaddr = contactaddr,
    contactemail = contactemail,
    contactweb = contactweb,
    producer = 'Sphinx ' + build_sphinx,
    creator = 'Sphinx ' + build_sphinx,
    publisher = publisher,
    subject = about,
    keywords = keywords,
    gxp_name = gxp_name,
)

rst_epilog = '''
.. include:: /{docsrc}/docterms.rsti
.. include:: /{docsrc}/docextlnk.rsti
.. include:: /{docsrc}/docunicode.rsti
.. include:: /{docsrc}/docreplaces.rsti
'''.format(
    docsrc = DOCSRC,
)

# -- Options for autosectionlabel extension ----------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autosectionlabel.html#configuration

autosectionlabel_prefix_document = True

# -- Options for extlinks extension ------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/extlinks.html#configuration

extlinks = {
    'wikide': ('https://de.wikipedia.org/wiki/%s', 'German Wikipedia: %s'),
    'wikien': ('https://en.wikipedia.org/wiki/%s', 'English Wikipedia: %s'),
    'elinux': ('https://elinux.org/%s', 'Embedded Linux Wiki: %s'),
    'tcs.bridle': (
        'https://bridle.tiac-systems.net/%s',
        'https://bridle.tiac-systems.net/%s'
    ),
    'tcs.gxp.dir': (
        gxp_base + gxp_slug + '/%s',
        gxp_name + ': %s'
    ),
    'tcs.gxp.file': (
        gxp_base + gxp_slug + '/' + basename + '%s',
        gxp_name + ': %s'
    ),
}

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    #
    # Standard reference to this docs, with local objects.inv
    #

    # python -m sphinx.ext.intersphinx 'build/html/objects.inv'
    # 'html': ('html', '{}/html/'.format(DOCBLD)),

    #
    # Standard reference to web docs, with web objects.inv
    #

    # python -m sphinx.ext.intersphinx 'https://docs.python.org/3/objects.inv'
    # 'python-doc': ('https://docs.python.org/3', None),

    # python -m sphinx.ext.intersphinx 'https://devguide.python.org/objects.inv'
    # 'python-devguide': ('https://devguide.python.org/', None),

    # python -m sphinx.ext.intersphinx 'https://www.sphinx-doc.org/en/master/objects.inv'
    # 'sphinx-doc': ('https://www.sphinx-doc.org/en/master', None),

    # python -m sphinx.ext.intersphinx 'https://rest-sphinx-memo.readthedocs.io/en/stable/objects.inv'
    # 'sphinx-memo': ('https://rest-sphinx-memo.readthedocs.io/en/stable/', None),

    # python -m sphinx.ext.intersphinx 'https://jbms.github.io/sphinx-immaterial/objects.inv'
    # 'sphinx-immaterial': ('https://jbms.github.io/sphinx-immaterial/', None),

    # python -m sphinx.ext.intersphinx 'https://sphinx-revealjs.readthedocs.io/en/stable/objects.inv'
    # 'sphinx-revealjs': ('https://sphinx-revealjs.readthedocs.io/en/stable/', None),

    # python -m sphinx.ext.intersphinx 'https://sphinxcontrib-spelling.readthedocs.io/en/stable/objects.inv'
    # 'sphinx-spelling': ('https://sphinxcontrib-spelling.readthedocs.io/en/stable/', None),

    # python -m sphinx.ext.intersphinx 'https://docs.zephyrproject.org/latest/objects.inv'
    # 'zephyr-doc': ('https://docs.zephyrproject.org/latest/', None),

    # python -m sphinx.ext.intersphinx 'https://bridle.tiac-systems.net/doc/latest/bridle/objects.inv'
    'tiac-bridle-doc': ('https://bridle.tiac-systems.net/doc/latest/bridle/', None),

    # python -m sphinx.ext.intersphinx 'https://bridle.tiac-systems.net/doc/latest/zephyr/objects.inv'
    'tiac-zephyr-doc': ('https://bridle.tiac-systems.net/doc/latest/zephyr/', None),

    #
    # Drawing the Docutils objects.inv from a RTD server,
    # but referring to the 0.16 web docs
    # Idea comes from https://sphobjinv.readthedocs.io/en/latest/
    #

    # python -m sphinx.ext.intersphinx 'https://docutils.readthedocs.io/en/sphinx-docs/objects.inv'
#   'docutils': ('https://docutils.sourceforge.io/docs/',
#                'https://docutils.readthedocs.io/en/sphinx-docs/objects.inv'),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Options for bibtex extension --------------------------------------------
# https://sphinxcontrib-bibtex.readthedocs.io/en/latest/usage.html#configuration

bibtex_bibfiles = [
    '{}/sphinx.bib'.format(path_bibtex),
    '{}/python.bib'.format(path_bibtex),
    '{}/cmake.bib'.format(path_bibtex),
    '{}/yocto.bib'.format(path_bibtex),
    '{}/zephyr.bib'.format(path_bibtex),
    '{}/arm.bib'.format(path_bibtex),
]

# -- Options for spelling extension ------------------------------------------
# https://sphinxcontrib-spelling.readthedocs.io/en/stable/customize.html

spelling_warning = True
spelling_show_suggestions = True

spelling_word_list_filename = [
    '{}/american-english-huge'.format(path_dictionaries),
    '{}/ngerman'.format(path_dictionaries),
    '{}/missing'.format(path_dictionaries),
    '{}/companies'.format(path_dictionaries),
    '{}/electronics'.format(path_dictionaries),
    '{}/proper-nouns'.format(path_dictionaries),
    'spelling'
]

spelling_exclude_patterns = [
    'doc*.rsti',
    'index*.rst',
    'bibliography.rst',
    'bibliography.rstr',
]

# -- Options for svg2pdfconverter extension ---------------------------------
# https://github.com/missinglinkelectronics/sphinxcontrib-svg2pdfconverter
#
# Convert SVG images to PDF with external tool, either with:
#
#    sphinxcontrib.inkscapeconverter -- Inkscape, or
#    sphinxcontrib.rsvgconverter     -- rsvg-convert from libRSVG or
#    sphinxcontrib.cairosvgconverter -- CairoSVG
#

# -- Options for asciinema extension ----------------------------------------
# https://github.com/divi255/sphinxcontrib.asciinema

sphinxcontrib_asciinema_defaults = {
    'theme': 'solarized-light',
    'font-size': '12px',
    'preload': True,
}

# -- Options for sass extension ---------------------------------------------
# https://github.com/attakei-lab/sphinxcontrib-sass#usage

sass_src_dir = '{}/revealjs/revealjs4/css/theme/source'.format(path_static)
sass_out_dir = '{}/revealjs/revealjs4/dist/theme'.format(path_static)

sass_include_paths = [
    path_revealjs_sass
]

sass_targets = {
    'tiac.scss': 'tiac.css',
    'tiac-decktape.scss': 'tiac-decktape.css',
}

# -- Options for LaTeX output ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

latex_title = u'{title}\\\\{{\\Large {headline}}}\\\\{{\\large {subtitle}}}'.format(
    title = title,
    subtitle = subtitle,
    headline = headline,
)

latex_author = u'{publisher}\\\\{author}'.format(
    publisher = publisher,
    author = author,
)

latex_releasename = u'Document Number: {docnumb}\\\\Revision:'.format(
    docnumb = docnumb,
)

latex_docclass = {
    'manual': 'book',
    'howto': 'article',  # two columns: 'proc', longer article: 'report'
}
latex_documents = [
    (master_doc, basename + '.tex', latex_title, latex_author, 'manual'),
    ('rtd', basename + '-readthedocs.tex', u'{}\\\\Read-The-Docs'.format(title), latex_author, 'howto'),
]

# latex_logo = '{}/bookshelf.pdf'.format(path_images)   # colored version of material/bookshelf.svg
latex_logo = '{}/library.pdf'.format(path_images)       # colored version of material/library.svg
latex_show_pagerefs = True

latex_engine = 'xelatex'

f = open('{}/extrapackages.tex'.format(path_latex_templates), 'r+')
latex_custom_extrapackages = f.read()

f = open('{}/passoptstopackages.tex.in'.format(path_latex_templates), 'r+')
latex_custom_passoptionstopackages = f.read().format (
    producer = 'Sphinx ' + build_sphinx,
    creator = 'Sphinx ' + build_sphinx,
    publisher = publisher,
    subject = about + ' Release: ' + release + ' (' + identify + ')',
    keywords = keywords,
)

f = open('{}/preamble.tex.in'.format(path_latex_templates), 'r+')
latex_custom_preamble = f.read().format (
    docnumb = docnumb,
    identify = identify,
    publisher = publisher,
    contactaddr = contactaddr,
    contactemail = contactemail,
    contactweb = contactweb,
)

f = open('{}/fontpkg.tex.in'.format(path_latex_templates), 'r+')
latex_custom_fontpkg = f.read().format (
    dejavu = '.' + os.sep,
    wenquanyi = '.' + os.sep,
)

latex_custom_fonts_urimap = {
    'DejaVuSansCondensed.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansCondensed-Bold.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansCondensed-Oblique.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansCondensed-BoldOblique.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansMono.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansMono-Bold.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansMono-Oblique.otf': '{}/'.format(addr_dejavu),
    'DejaVuSansMono-BoldOblique.otf': '{}/'.format(addr_dejavu),
    'WenQuanYiZenHei.otf': '{}/'.format(addr_wenquanyi),
}

f = open('{}/utf8extra.tex'.format(path_latex_templates), 'r+')
latex_custom_utf8extra = f.read()

latex_elements = {
    #
    # Keys that you may want to override include:
    #
    'extraclassoptions': 'table',

    # Paper size option of the document class ('letterpaper' or 'a4paper'),
    # default 'letterpaper'.
    'papersize': 'a4paper',

    # Point size option of the document class ('10pt', '11pt' or '12pt'),
    # default '10pt'.
    'pointsize': '10pt',

    # "babel" package inclusion, default r'\usepackage{babel}'.
    'babel': r'\usepackage[english]{babel}',

    # "geometry" package inclusion, default r'\usepackage{geometry}'.
    # note: 'total={w,h}' depends hard on 'a4paper', see above.
    'geometry': r'\usepackage[total={170mm,257mm},left=25mm,right=15mm,top=20mm,headsep=10mm]{geometry}',
#   'geometry': r'\usepackage[headsep=1.0cm,left=2.5cm,right=1.5cm]{geometry}',

    # Font package inclusion, default r'\usepackage{times}' (which uses Times
    # and Helvetica). You can set this to '' to use the Computer Modern fonts.
    # Defaults to '' when the language uses the Cyrillic script.
    # For xelatex it defaults to: '''\setmainfont{FreeSerif}[..]
    # \setsansfont{FreeSans}[..]\setmonofont{FreeMono}[..]'''
    'fontpkg': latex_custom_fontpkg,

    # Inclusion of the "fncychap" package (which makes fancy chapter titles),
    # default r'\usepackage[Bjarne]{fncychap}' for English documentation,
    # r'\usepackage[Sonny]{fncychap}' for internationalized docs (because the
    # "Bjarne" style uses numbers spelled out in English). Other "fncychap"
    # styles you can try include "Lenny", "Glenn", "Conny" and "Rejne". You can
    # also set this to '' to disable fncychap.
#   'fncychap': r'\usepackage[Sonny]{fncychap}',
#   'fncychap': r'\usepackage[Lenny]{fncychap}',
#   'fncychap': r'\usepackage[Glenn]{fncychap}',
#   'fncychap': r'\usepackage[Conny]{fncychap}',
#   'fncychap': r'\usepackage[Rejne]{fncychap}',
#   'fncychap': r'\usepackage[Bjarne]{fncychap}',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',

    # Additional package inclusion, default empty.
    'extrapackages': latex_custom_extrapackages,

    # "PassOptionsToPackage" call, default empty.
    'passoptionstopackages': latex_custom_passoptionstopackages,

    # Additional preamble content, default empty.
    'preamble': latex_custom_preamble,

    # Latex figure (float) alignment, default 'htbp' (here, top, bottom, page).
    # Whenever an image doesn't fit into the current page, it will be 'floated'
    # into the next page but may be preceded by any other text. If you don't
    # like this behavior, use 'H' which will disable floating and position
    # figures strictly in the order they appear in the source.
    'figure_align': 'H',

    # Latex number figure format, default empty.
#   'numfig_format': '',

    #
    # Keys that don’t need be overridden unless in special cases are:
    #

    # "inputenc" package inclusion, defaults to r'\usepackage[utf8]{inputenc}'
    # when using pdflatex. Otherwise unset.
#   'inputenc': r'\usepackage[utf8]{inputenc}',

    # Unicode character declaration, for xelatex defaults to:
    # \catcode`^^^^00a0\active\protected\def^^^^00a0{\leavevmode\nobreak\ }
    'utf8extra': latex_custom_utf8extra,

    # "cmap" package inclusion, default r'\usepackage{cmap}'.
#   'cmappkg': r'\usepackage{cmap}',

    # "fontenc" package inclusion, default r'\usepackage[T1]{fontenc}' and
    # r'\usepackage{fontspec}\defaultfontfeatures[\rmfamily,\sffamily,\ttfamily]{}'
    # in case of xelatex for non-mandarin languages.
#   'fontenc': r'\usepackage[T1]{fontenc}',

    # "amsmath" package inclusion, default r'\usepackage{amsmath,amssymb,amstext}'.
#   'amsmath': r'\usepackage{amsmath,amssymb,amstext}',

    # Value that prefixes 'release' element on title page, default 'Release'.
    'releasename': latex_releasename,

    # "makeindex" call, default r'\makeindex'. Override if you want to
    # generate a differently-styled index page.
#   'makeindex': r'\makeindex',

    # "maketitle" call, default r'\sphinxmaketitle'. Override if you want to
    # generate a differently-styled title page.
#   'maketitle': r'\sphinxmaketitle',

    # "tableofcontents" call, default r'\sphinxtableofcontents'. Override if
    # you want to generate a different table of contents or put content between
    # the title page and the TOC.
#   'tableofcontents': r'\sphinxtableofcontents',

    # "printindex" call, the last thing in the file, default r'\printindex'.
    # Override if you want to generate the index differently or append some
    # content after the index.
    'printindex': r'\footnotesize\raggedright\printindex',

    # Commands used to display transitions, default r'\n\n\bigskip\hrule{}\bigskip\n\n'.
    # Override if you want to display transitions differently.
#   'transition': r'\n\n\bigskip\hrule{}\bigskip\n\n',

    #
    # Keys that are set by other options and therefore should not be
    # overridden are: 'docclass' 'classoptions' 'extraclassoptions'
    #                 'contentsname' 'title' 'date' 'release'
    #                 'author' 'logo' 'makeindex' 'shorthandoff'
    #                 'tocdepth' 'pageautorefname'
    #

    # Get rid of evenly numbered empty pages (default book style)
#   'classoptions': ',openany,oneside',
    'classoptions': ',twoside',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#configuration
# https://jbms.github.io/sphinx-immaterial/customization.html#configuration-options

html_title = u'{subtitle} – {headline} – {title}'.format(
    headline = headline,
    subtitle = subtitle,
    title = title,
)

html_theme = 'sphinx_rtd_theme'
### NOT YET ### html_theme = 'sphinx_immaterial'

html_static_path = ['{}/html'.format(path_static), '{}'.format(path_videos)]
html_extra_path = ['{}/html'.format(path_extra)]
html_favicon = '{}/bookshelf.svg'.format(path_images)  # colored version of material/bookshelf.svg
html_logo = '{}/library.svg'.format(path_images)       # colored version of material/library.svg

html_last_updated_fmt = None
# html_last_updated_fmt = '%b %d, %Y'
# html_last_updated_fmt = '%a, %d %b %Y %H:%M:%S %Z'
html_domain_indices = False
html_use_index = True
html_split_index = True
html_show_sourcelink = True
html_sourcelink_suffix = '.txt'
html_show_sphinx = True
html_show_copyright = True

html_context = {
    'document_title': title,
    'document_subtitle': subtitle,
    'document_headline': headline,
    'document_number': docnumb,
    'document_revision': release,
    'document_vcs': identify,
}

# html_js_files = []
html_css_files = [
    '{}/DejaVu.css'.format(wfs_addr),
#   '{}/WenQuanYi.css'.format(wfs_addr),
    'css/force-dejavu.css',
#   'css/force-wenquanyi.css',
#   'css/fix-cite.css',
#   'css/fix-float.css',
    'css/strikethrough.css',
    'css/underline.css',
    'css/strong.css',
    'css/colors.css',
    'css/tweaks-sphinx_rtd_theme.css',
]

html_search_scorer = '{}/js/scorer.js'.format(path_html_templates)

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': True,
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

# -- Options for Reveal.js output --------------------------------------------
# https://sphinx-revealjs.readthedocs.io/en/stable/configurations/#configurations

# Use different brandings in case of Reveal.js builder
if tags.has('revealjs'):    # pylint: disable=undefined-variable
    html_logo = ''
    html_show_copyright = True
    html_context['document_branding'] = branding
    html_context['document_subtitle'] = category
    html_context['document_termsofuse'] = '''
        All rights reserved. Reproduction, modification
        or redistribution not permitted.
    '''

revealjs_static_path = [
    '{}/revealjs'.format(path_static),
    '{}/html'.format(path_static),
    '{}/revealjs'.format(path_extra),
    '{}/html'.format(path_extra),
    '{}'.format(path_videos),
    '{}'.format(path_images),
]

revealjs_google_fonts = ['M PLUS 1p',]
revealjs_generic_font = 'sans-serif'
revealjs_style_theme = 'white'  # fallback for altmode
revealjs_use_index = False

# revealjs_script_files = []
revealjs_css_files = [
    'css/colors.css',
    'css/strong.css',
    'css/underline.css',
    'css/strikethrough.css',
    'css/tweaks-revealjs.css',
#   'plugin/asciinema/asciinema-player.css',
    'asciinema-player_2.6.1.css',  # QnD hack for sphinxcontrib.asciinema
    'asciinema-custom.css',        # QnD hack for sphinxcontrib.asciinema
    'revealjs4/plugin/rajgoel/chalkboard/style.css',
    'revealjs4/plugin/rajgoel/customcontrols/style.css',
    'revealjs4/dist/theme/tiac.css\" id=\"theme',  # QnD hack for themeoverride
    'revealjs4/plugin/highlight/solarized-light.css\" id=\"highlight-theme',  # QnD hack for themeoverride
]

#
# Raw JavaScript code for configuration of Reveal.js. If this value is set,
# render script tag after source script tags.
#
# https://revealjs.com/config/
# https://github.com/McShelby/reveal-themeoverride#configuration
# https://github.com/McShelby/reveal-altmode#configuration
# https://github.com/McShelby/reveal-pdfexport#configuration
# https://github.com/McShelby/reveal-helpbutton#configuration
# https://www.npmjs.com/package/reveal.js-menu#configuration
# https://github.com/rajgoel/reveal.js-plugins/issues/11#issuecomment-1029213918
# https://www.w3schools.com/css/css3_variables_javascript.asp
#
revealjs_script_conf = '''
    {{
        dependencies: [
            {{
                src: '_static/revealjs4/plugin/notes-pointer/notes-pointer.js',
                async: true,
            }},
        //  {{
        //      src: '_static/plugin/asciinema/asciinema-player.min.js',
        //      async: false,
        //  }},
            {{
                src: '_static/revealjs4/plugin/rajgoel/animate/svg.min.js',
                async: false,
            }},
            {{
            //  src: 'https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.2.1/chart.min.js',
                src: 'https://cdn.jsdelivr.net/npm/chart.js@3.2.1/dist/chart.min.js',
                async: false,
            }},
        ],

        hash: true,
        history: true,
        progress: true,
        overview: true,
        pause: true,
        help: true,

        rtl: false,
        loop: false,
        controls: true,
        controlsTutorial: true,
        controlsBackArrows: 'faded',
        mouseWheel: true,

        hideInactiveCursor: true,
        hideCursorTime: 500,

        slideNumber: 'c/t',
        showSlideNumber: 'print',

        fragments: true,
        fragmentInURL: true,

        rollingLinks: true,
        previewLinks: true,
        preloadIframes: true,
        viewDistance: 3,
        mobileViewDistance: 2,

        width: 1440,
        // height: 1080,
        minScale: 0.1,
        maxScale: 1.0,
        // margin: 0.15,

        center: true,
        theme: 'tiac',
        highlightTheme: 'solarized-light',

        transitionSpeed: 'fast', // default/fast/slow
        transition: 'fade', // none/fade/slide/convex/concave/zoom
        background_transition: 'convex',

        helpButtonDisplay: 'first',

        altModeShortcut: 'A',
        altModeConfig: [
            {{
                theme: 'tiac',
                fragments: true,
            }},
            {{
                width: 930, // A4:930(850)/A3:1395
                height: 685, // A4:685(640)/A3:1015
                minScale: 1.0,
                maxScale: 1.0,
                theme: 'tiac-decktape',
                fragments: false,
                showSlideNumber: 'all',
                helpButtonDisplay: 'none',
                menu: {{ openButton: false, }},
            }},
            {{
                theme: 'white',
                fragments: false,
                showSlideNumber: 'all',
                helpButtonDisplay: 'none',
                menu: {{ openButton: false, }},
            }},
            {{
                theme: 'black',
                fragments: false,
                showSlideNumber: 'all',
                helpButtonDisplay: 'none',
                menu: {{ openButton: false, }},
            }},
        ],

        pdfExportShortcut: 'P',
        pdfSeparateFragments: false,

        menu: {{
            openOnInit: false,
            openButton: true,
            keyboard: true,
            markers: true,
            numbers: true,
            // themes: true,
            // themesPath: '{themespath}/',
            themes: [
                {{
                    name: '{publisher}',
                    theme: '{themespath}/tiac.css',
                }},
                {{
                    name: 'Black',
                    theme: '{themespath}/black.css',
                }},
                {{
                    name: 'White',
                    theme: '{themespath}/white.css',
                }},
                {{
                    name: 'League',
                    theme: '{themespath}/league.css',
                }},
                {{
                    name: 'Sky',
                    theme: '{themespath}/sky.css',
                }},
                {{
                    name: 'Beige',
                    theme: '{themespath}/beige.css',
                }},
                {{
                    name: 'Simple',
                    theme: '{themespath}/simple.css',
                }},
                {{
                    name: 'Serif',
                    theme: '{themespath}/serif.css',
                }},
                {{
                    name: 'Blood',
                    theme: '{themespath}/blood.css',
                }},
                {{
                    name: 'Night',
                    theme: '{themespath}/night.css',
                }},
                {{
                    name: 'Moon',
                    theme: '{themespath}/moon.css',
                }},
                {{
                    name: 'Solarized',
                    theme: '{themespath}/solarized.css',
                }},
            ],
            transitions: true,
            side: 'left',
            width: 'third',
            titleSelector: 'h1, h2',
            hideMissingTitles: true, // reduce exactly to titleSelector
            custom: [
                {{
                    title: 'Bookmarks',
                    icon: '<i class="fas fa-bookmark">',
                    src: '{bookmarks}',
                }},
            ],
        }},

        notes_pointer: {{
            pointer: {{
                size: 24,
                color: 'rgba(255, 0, 0, 0.66)',
                key: 'R',
            }},
            notes: {{
                key: 'S',
            }},
        }},

        customcontrols: {{
            controls: [
                {{
                    id: 'toggle-overview',
                    title: 'Toggle overview (O)',
                    icon: '<i class="fa fa-th"></i>',
                    action: 'Reveal.toggleOverview();',
                }},
                {{
                    icon: '<i class="fa fa-pen-square"></i>',
                    title: 'Toggle chalkboard (B)',
                    action: 'RevealChalkboard.toggleChalkboard();',
                }},
                {{
                    icon: '<i class="fa fa-pen"></i>',
                    title: 'Toggle notes canvas (C)',
                    action: 'RevealChalkboard.toggleNotesCanvas();',
                }},
            ],
        }},

        anything: [
        //  {{
        //      className: 'asciicast',
        //      defaults: {{
        //          theme: 'solarized-light',
        //          fontSize: '20px',
        //          preload: true,
        //          fit: false,
        //      }},
        //      initialize: (function(container, options) {{
        //          // console.log(options.URL, container, options);
        //          AsciinemaPlayer.create(options.URL, container, options);
        //      }}),
        //  }},
        ],

        animate: {{
            autoplay: true,
        }},

        chart: {{
            defaults: {{
                color: 'black', // color of labels
                font: {{ // for labels
                    family: getComputedStyle(document.querySelector(':root')).getPropertyValue('--r-main-font'),
                    size: getComputedStyle(document.querySelector(':root')).getPropertyValue('--r-main-font-size'),
                }},
                scale: {{
                    beginAtZero: true,
                    ticks: {{
                        display: true,
                        stepSize: 5,
                        font: {{ // for axis
                            family: getComputedStyle(document.querySelector(':root')).getPropertyValue('--r-heading-font'),
                            size: getComputedStyle(document.querySelector(':root')).getPropertyValue('--r-main-font-size'),
                        }},
                    }},
                    grid: {{
                        color: 'darkgray', // color of grid lines
                    }},
                }},
            }},
            line: {{
                borderColor: [
                    'rgba(20,220,220,.8)',
                    'rgba(220,120,120,.8)',
                    'rgba(20,120,220,.8)',
                ],
                borderDash: [ [5,10], [0,0] ],
                borderWidth: 5,
            }},
            bar: {{
                backgroundColor: [
                    'rgba(20,220,220,.8)',
                    'rgba(220,120,120,.8)',
                    'rgba(20,120,220,.8)',
                ],
            }},
            pie: {{
                backgroundColor: [ [
                    'rgba(0,0,0,.8)',
                    'rgba(220,20,20,.8)',
                    'rgba(20,220,20,.8)',
                    'rgba(220,220,20,.8)',
                    'rgba(20,20,220,.8)',
                ] ],
            }},
            radar: {{
                borderColor: [
                    'rgba(20,220,220,.8)',
                    'rgba(220,120,120,.8)',
                    'rgba(20,120,220,.8)',
                ],
            }},
        }},
    }}
'''.format(
    publisher = publisher,
    themespath = '_static/revealjs4/dist/theme',
    bookmarks = '_static/bookmarks.html',
)

#
# List of pulugin configurations. If this value is set, render script tag after
# source script tags. There are bundled Reveal.js plugins at 'revealjs4/plugin'.
#
# https://revealjs.com/plugins/#built-in-plugins
# https://highlightjs.org/
#
revealjs_script_plugins = [
    {
        'name': 'RevealHighlight',
        'src': 'revealjs4/plugin/highlight/highlight.js',
    },
    {
        'name': 'RevealMath',
        'src': 'revealjs4/plugin/math/math.js',
    },
#   {
#       'name': 'RevealNotes',
#       'src': 'revealjs4/plugin/notes/notes.js',
#   },
    {
        'name': 'RevealSearch',
        'src': 'revealjs4/plugin/search/search.js',
    },
    {
        'name': 'RevealZoom',
        'src': 'revealjs4/plugin/zoom/zoom.js',
    },
    # https://github.com/McShelby/reveal-themeoverride
    {
        'name': 'ThemeOverride',
        'src': 'revealjs4/plugin/themeoverride/themeoverride.js',
    },
    # https://github.com/McShelby/reveal-altmode
    {
        'name': 'AltMode',
        'src': 'revealjs4/plugin/altmode/altmode.js',
    },
    # https://github.com/McShelby/reveal-pdfexport
    {
        'name': 'PdfExport',
        'src': 'revealjs4/plugin/pdfexport/pdfexport.js',
    },
    # https://github.com/McShelby/reveal-helpbutton
    {
        'name': 'HelpButton',
        'src': 'revealjs4/plugin/helpbutton/helpbutton.js',
    },
    # https://www.npmjs.com/package/reveal.js-menu
    {
        'name': 'RevealMenu',
        'src': 'revealjs4/plugin/menu/menu.js',
    },
    # https://www.npmjs.com/package/reveal.js-plugins
    # RevealChalkboard: allowing to add chalkboard
    # effect based on Chalkboard by Mohamed Moustafa
    # (https://github.com/mmoustafa/Chalkboard).
    {
        'name': 'RevealChalkboard',
        'src': 'revealjs4/plugin/rajgoel/chalkboard/plugin.js',
    },
    # https://www.npmjs.com/package/reveal.js-plugins
    # RevealCustomControls: allowing to add responsive
    # custom controls which allow arbitrary positioning,
    # layout, and behaviour of the controls.
    {
        'name': 'RevealCustomControls',
        'src': 'revealjs4/plugin/rajgoel/customcontrols/plugin.js',
    },
    # https://www.npmjs.com/package/reveal.js-plugins
    # RevealAnything: allowing to add anything inside
    # an HTML object using a JSON string and/or a
    # javascript function.
    {
        'name': 'RevealAnything',
        'src': 'revealjs4/plugin/rajgoel/anything/plugin.js',
    },
    # https://www.npmjs.com/package/reveal.js-plugins
    # RevealAnimate: allowing to add animations using
    # SVG.js (https://svgjs.dev/).
    {
        'name': 'RevealAnimate',
        'src': 'revealjs4/plugin/rajgoel/animate/plugin.js',
    },
    # https://www.npmjs.com/package/reveal.js-plugins
    # RevealChart: allowing to add animated charts using
    # Chart.js (https://www.chartjs.org/).
    {
        'name': 'RevealChart',
        'src': 'revealjs4/plugin/rajgoel/chart/plugin.js',
    },
]

f = open('{}/decktape-build.in'.format(path_revealjs_templates), 'r+')
revealjs_decktape_build = f.read().format (
    python_executable = sys.executable,
    publisher = publisher,
    author = author,
    title = title,
    subtitle = 'Slides',
    headline = headline,
    release = release,
    identify = identify,
    pause = decktape_pause,
    size = decktape_size,
    slides = decktape_slides,
)

def create_decktape_builder(content, outfile):
    try:
        with open(outfile, 'w') as o:
            o.write(content)

        o.close()
        mode = os.stat(outfile).st_mode
        mode |= (mode & 0o444) >> 2
        os.chmod(outfile, mode)

        return True

    except Exception as exc:
        logcfg.warning('Could not create decktape builder: %s [%s]' % (outfile, exc))
        return False

def setup_revealjs_outdir(app):
    script_file = app.outdir + '/decktape-build'

    logcfg.info('creating decktape builder in %s...', script_file, color='yellow')
    if not create_decktape_builder(revealjs_decktape_build, script_file):
        return

    logcfg.info('have decktape builder in %s...', script_file, color='green')

def download_remote_file(uri, outfile):
    try:
        r = sphinx.util.requests.get(uri)

        if r.status_code >= 400:
            logcfg.warning('Could not fetch remote file: %s [%d]' % (uri, r.status_code))
            return False

        else:
            if r.status_code == 200:
                with open(outfile, 'wb') as f:
                    f.write(r.content)
            return True

    except Exception as exc:
        logcfg.warning('Could not fetch remote file: %s [%s]' % (uri, exc))
        return False

def setup_latex_outdir(app):
    for font, uri_base in latex_custom_fonts_urimap.items():

        font_url = uri_base + font
        font_file = app.outdir + '/' + font

        logcfg.info('loading custom font from %s...', font_url, color='yellow')
        if not download_remote_file(font_url, font_file):
            continue

        logcfg.info('have custom font in %s...', font_file, color='green')

def setup_outdir(app):
    if app.builder.name == 'revealjs':
        setup_revealjs_outdir(app)

    if app.builder.name == 'latex':
        setup_latex_outdir(app)

def setup(app):
    app.connect('builder-inited', setup_outdir)


# vim: tw=130 ts=4 sw=4 sts=4 sta et ai nu
