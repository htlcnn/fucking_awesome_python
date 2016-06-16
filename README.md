# Fucking Awesome Python

A curated list with Github stars and forks stats based on awesome [awesome-python](https://github.com/vinta/awesome-python), inspired by [fucking-awesome-go](https://github.com/hvnsweeting/fucking-awesome-go) and [fucking-awesome-python](https://github.com/trananhkma/fucking-awesome-python)

# Awesome Python [![:earth_americas:Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

A curated list of awesome Python frameworks, libraries, software and resources.

Inspired by [:octocat:awesome-php](https://github.com/ziadoz/awesome-php) - :star: 12110 :fork_and_knife: 2416.

- [Awesome Python](#awesome-python)
    - [Environment Management](#environment-management)
    - [Package Management](#package-management)
    - [Package Repositories](#package-repositories)
    - [Distribution](#distribution)
    - [Build Tools](#build-tools)
    - [Interactive Interpreter](#interactive-interpreter)
    - [Files](#files)
    - [Date and Time](#date-and-time)
    - [Text Processing](#text-processing)
    - [Specific Formats Processing](#specific-formats-processing)
    - [Natural Language Processing](#natural-language-processing)
    - [Documentation](#documentation)
    - [Configuration](#configuration)
    - [Command-line Tools](#command-line-tools)
    - [Downloader](#downloader)
    - [Imagery](#imagery)
    - [OCR](#ocr)
    - [Audio](#audio)
    - [Video](#video)
    - [Geolocation](#geolocation)
    - [HTTP](#http)
    - [Database](#database)
    - [Database Drivers](#database-drivers)
    - [ORM](#orm)
    - [Web Frameworks](#web-frameworks)
    - [Serverless Frameworks](#serverless-frameworks)
    - [Permissions](#permissions)
    - [CMS](#cms)
    - [E-commerce](#e-commerce)
    - [RESTful API](#restful-api)
    - [Serialization](#serialization)
    - [Authentication](#authentication)
    - [Template Engine](#template-engine)
    - [Queue](#queue)
    - [Search](#search)
    - [News Feed](#news-feed)
    - [Asset Management](#asset-management)
    - [Caching](#caching)
    - [Email](#email)
    - [Internationalization](#internationalization)
    - [URL Manipulation](#url-manipulation)
    - [HTML Manipulation](#html-manipulation)
    - [Web Crawling](#web-crawling)
    - [Web Content Extracting](#web-content-extracting)
    - [Forms](#forms)
    - [Data Validation](#data-validation)
    - [Anti-spam](#anti-spam)
    - [Tagging](#tagging)
    - [Admin Panels](#admin-panels)
    - [Static Site Generator](#static-site-generator)
    - [Processes](#processes)
    - [Concurrency and Parallelism](#concurrency-and-parallelism)
    - [Networking](#networking)
    - [WebSocket](#websocket)
    - [WSGI Servers](#wsgi-servers)
    - [RPC Servers](#rpc-servers)
    - [Cryptography](#cryptography)
    - [GUI](#gui)
    - [Game Development](#game-development)
    - [Logging](#logging)
    - [Testing](#testing)
    - [Code Analysis and Linter](#code-analysis-and-linter)
    - [Debugging Tools](#debugging-tools)
    - [Science and Data Analysis](#science-and-data-analysis)
    - [Data Visualization](#data-visualization)
    - [Computer Vision](#computer-vision)
    - [Machine Learning](#machine-learning)
    - [Functional Programming](#functional-programming)
    - [MapReduce](#mapreduce)
    - [Third-party APIs](#third-party-apis)
    - [DevOps Tools](#devops-tools)
    - [ChatOps Tools](#chatops-tools)
    - [Job Scheduler](#job-scheduler)
    - [Foreign Function Interface](#foreign-function-interface)
    - [High Performance](#high-performance)
    - [Network Virtualization and SDN](#network-virtualization-and-sdn)
    - [Hardware](#hardware)
    - [Compatibility](#compatibility)
    - [Miscellaneous](#miscellaneous)
    - [Algorithms and Design Patterns](#algorithms-and-design-patterns)
    - [Editor Plugins](#editor-plugins)
    - [IDEs](#ides)
- [Services](#services)
    - [Continuous Integration](#continuous-integration)
    - [Code Quality](#code-quality)
- [Resources](#resources)
    - [Websites](#websites)
    - [Weekly](#weekly)
    - [Twitter](#twitter)
- [Other Awesome Lists](#other-awesome-lists)
- [Contributing](#contributing)

- - -

## Environment Management

*Libraries for Python version and environment management.*

* [:octocat:p](https://github.com/qw3rtman/p) - :star: 557 :fork_and_knife: 23 - Dead simple interactive Python version management.
* [:octocat:pyenv](https://github.com/yyuu/pyenv) - :star: 4712 :fork_and_knife: 371 - Simple Python version management.
* [:earth_americas:venv](https://docs.python.org/3/library/venv.html) - (Python standard library in Python 3.3+) Creating lightweight virtual environments.
* [:earth_americas:virtualenv](https://pypi.python.org/pypi/virtualenv) - A tool to create isolated Python environments.
* [:earth_americas:virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) - A set of extensions to virtualenv.

## Package Management

*Libraries for package and dependency management.*

* [:earth_americas:pip](https://pip.pypa.io/en/stable/) - The Python package and dependency manager.
    * [Python Package Index](https://pypi.python.org/pypi)
* [:octocat:pip-tools](https://github.com/nvie/pip-tools) - :star: 1623 :fork_and_knife: 148 - A set of tools to keep your pinned Python dependencies fresh.
* [:octocat:conda](https://github.com/conda/conda/) - :star: 761 :fork_and_knife: 261 - Cross-platform, Python-agnostic binary package manager.
* [:earth_americas:Curdling](http://clarete.li/curdling/) - Curdling is a command line tool for managing Python packages.
* [:earth_americas:wheel](http://pythonwheels.com/) - The new standard of Python distribution and are intended to replace eggs.

## Package Repositories

*Local PyPI repository server and proxies.*

* [:octocat:warehouse](https://github.com/pypa/warehouse) - :star: 602 :fork_and_knife: 125 - Next generation Python Package Repository (PyPI).
    * [Warehouse](https://warehouse.python.org/)
* [:earth_americas:bandersnatch](https://bitbucket.org/pypa/bandersnatch) - PyPI mirroring tool provided by Python Packaging Authority (PyPA).
* [:earth_americas:devpi](http://doc.devpi.net/latest/) - PyPI server and packaging/testing/release tool.
* [:octocat:localshop](https://github.com/mvantellingen/localshop) - :star: 274 :fork_and_knife: 98 - Local PyPI server (custom packages and auto-mirroring of pypi).

## Distribution

*Libraries to create packaged executables for release distribution.*

* [:octocat:PyInstaller](https://github.com/pyinstaller/pyinstaller) - :star: 1839 :fork_and_knife: 444 - Converts Python programs into stand-alone executables (cross-platform).
* [:octocat:dh-virtualenv](https://github.com/spotify/dh-virtualenv) - :star: 827 :fork_and_knife: 86 - Build and distribute a virtualenv as a Debian package.
* [:earth_americas:Nuitka](http://nuitka.net/) - Compile scripts, modules, packages to an executable or extension module.
* [:earth_americas:py2app](http://pythonhosted.org/py2app/) - Freezes Python scripts (Mac OS X).
* [:earth_americas:py2exe](http://www.py2exe.org/) - Freezes Python scripts (Windows).
* [:earth_americas:pynsist](http://pynsist.readthedocs.io/) - A tool to build Windows installers, installers bundle Python itself.

## Build Tools

*Compile software from source code.*

* [:earth_americas:buildout](http://www.buildout.org/en/latest/) - A build system for creating, assembling and deploying applications from multiple parts.
* [:earth_americas:BitBake](http://www.yoctoproject.org/docs/1.6/bitbake-user-manual/bitbake-user-manual.html) - A make-like build tool for embedded Linux.
* [:octocat:PlatformIO](https://github.com/platformio/platformio) - :star: 1086 :fork_and_knife: 159 - A console tool to build code with different development platforms.
* [:octocat:PyBuilder](https://github.com/pybuilder/pybuilder) - :star: 645 :fork_and_knife: 136 - A continuous build tool written in pure Python.
* [:earth_americas:SCons](http://www.scons.org/) - A software construction tool.

## Interactive Interpreter

*Interactive Python interpreters (REPL).*

* [:earth_americas:Jupyter Notebook (IPython)](https://jupyter.org) -  A rich toolkit to help you make the most out of using Python interactively.
* [:octocat:bpython](https://github.com/bpython/bpython) - :star: 541 :fork_and_knife: 72 – A fancy interface to the Python interpreter.
* [ptpython](https://github.com/jonathanslenders/ptpython) - Advanced Python REPL built on top of the [:octocat:python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) - :star: 2604 :fork_and_knife: 131.

## Files

*Libraries for file manipulation and MIME type detection.*

* [:earth_americas:imghdr](https://docs.python.org/2/library/imghdr.html) - (Python standard library) Determine the type of an image.
* [:earth_americas:mimetypes](https://docs.python.org/2/library/mimetypes.html) - (Python standard library) Map filenames to MIME types.
* [path.py](https://github.com/jaraco/path.py) - A module wrapper for [:earth_americas:os.path](https://docs.python.org/2/library/os.path.html).
* [:earth_americas:pathlib](https://pathlib.readthedocs.org/en/pep428/) - (Python standard library in Python 3.4+) An cross-platform, object-oriented path library.
* [:octocat:python-magic](https://github.com/ahupp/python-magic) - :star: 648 :fork_and_knife: 102 - A Python interface to the libmagic file type identification library.
* [:octocat:Unipath](https://github.com/mikeorr/Unipath) - :star: 368 :fork_and_knife: 30 - An object-oriented approach to file/directory operations.
* [:octocat:watchdog](https://github.com/gorakhargosh/watchdog) - :star: 2067 :fork_and_knife: 273 - API and shell utilities to monitor file system events.

## Date and Time

*Libraries for working with dates and times.*

* [:octocat:arrow](https://github.com/crsmithdev/arrow) - :star: 3082 :fork_and_knife: 260 - Better dates & times for Python.
* [:octocat:Chronyk](https://github.com/KoffeinFlummi/Chronyk) - :star: 218 :fork_and_knife: 8 - A Python 3 library for parsing human-written times and dates.
* [dateutil](https://github.com/dateutil/dateutil) - Extensions to the standard Python [:earth_americas:datetime](https://docs.python.org/2/library/datetime.html) module.
* [:octocat:delorean](https://github.com/myusuf3/delorean/) - :star: 1184 :fork_and_knife: 61 - A library for clearing up the inconvenient truths that arise dealing with datetimes.
* [moment](https://github.com/zachwill/moment) - A Python library for dealing with dates/times. Inspired by [:earth_americas:Moment.js](http://momentjs.com/).
* [:octocat:PyTime](https://github.com/shinux/PyTime) - :star: 96 :fork_and_knife: 12 - A easy-use Python module which aims to operate date/time/datetime by string.
* [pytz](https://launchpad.net/pytz) - World timezone definitions, modern and historical. Brings the [:earth_americas:tz database](https://en.wikipedia.org/wiki/Tz_database) into Python.
* [:octocat:when.py](https://github.com/dirn/When.py) - :star: 148 :fork_and_knife: 13 - Providing user-friendly functions to help perform common date and time actions.

## Text Processing

*Libraries for parsing and manipulating plain texts.*

* General
    * [:octocat:chardet](https://github.com/chardet/chardet) - :star: 533 :fork_and_knife: 79 - Python 2/3 compatible character encoding detector.
    * [:earth_americas:difflib](https://docs.python.org/2/library/difflib.html) - (Python standard library) Helpers for computing deltas.
    * [:octocat:ftfy](https://github.com/LuminosoInsight/python-ftfy) - :star: 1309 :fork_and_knife: 48 - Makes Unicode text less broken and more consistent automagically.
    * [:octocat:fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy) - :star: 2472 :fork_and_knife: 245 - Fuzzy String Matching.
    * [:octocat:Levenshtein](https://github.com/ztane/python-Levenshtein/) - :star: 214 :fork_and_knife: 42 - Fast computation of Levenshtein distance and string similarity.
    * [:octocat:pangu.py](https://github.com/vinta/pangu.py) - :star: 40 :fork_and_knife: 8 - Spacing texts for CJK and alphanumerics.
    * [:octocat:pyfiglet](https://github.com/pwaller/pyfiglet) - :star: 150 :fork_and_knife: 16 - An implementation of figlet written in Python.
    * [:octocat:shortuuid](https://github.com/stochastic-technologies/shortuuid) - :star: 584 :fork_and_knife: 46 - A generator library for concise, unambiguous and URL-safe UUIDs.
    * [:earth_americas:unidecode](https://pypi.python.org/pypi/Unidecode) - ASCII transliterations of Unicode text.
    * [:octocat:uniout](https://github.com/moskytw/uniout) - :star: 95 :fork_and_knife: 10 - Print readable chars instead of the escaped string.
    * [:octocat:xpinyin](https://github.com/lxneng/xpinyin) - :star: 333 :fork_and_knife: 92 - A library to translate Chinese hanzi (漢字) to pinyin (拼音).
* Slugify
    * [:octocat:awesome-slugify](https://github.com/dimka665/awesome-slugify) - :star: 281 :fork_and_knife: 16 - A Python slugify library that can preserve unicode.
    * [:octocat:python-slugify](https://github.com/un33k/python-slugify) - :star: 259 :fork_and_knife: 31 - A Python slugify library that translates unicode to ASCII.
    * [:octocat:unicode-slugify](https://github.com/mozilla/unicode-slugify) - :star: 203 :fork_and_knife: 37 - A slugifier that generates unicode slugs with Django as a dependency.
* Parser
    * [:octocat:phonenumbers](https://github.com/daviddrysdale/python-phonenumbers) - :star: 1232 :fork_and_knife: 164 - Parsing, formatting, storing and validating international phone numbers.
    * [:earth_americas:PLY](http://www.dabeaz.com/ply/) - Implementation of lex and yacc parsing tools for Python
    * [:earth_americas:Pygments](http://pygments.org/) - A generic syntax highlighter.
    * [:earth_americas:pyparsing](http://pyparsing.wikispaces.com/) - A general purpose framework for generating parsers.
    * [:octocat:python-nameparser](https://github.com/derek73/python-nameparser) - :star: 150 :fork_and_knife: 26 - Parsing human names into their individual components.
    * [:octocat:python-user-agents](https://github.com/selwin/python-user-agents) - :star: 357 :fork_and_knife: 76 - Browser user agent parser.
    * [:octocat:sqlparse](https://github.com/andialbrecht/sqlparse) - :star: 651 :fork_and_knife: 161 - A non-validating SQL parser.

## Specific Formats Processing

*Libraries for parsing and manipulating specific text formats.*

* General
    * [:octocat:tablib](https://github.com/kennethreitz/tablib) - :star: 1965 :fork_and_knife: 276 - A module for Tabular Datasets in XLS, CSV, JSON, YAML.
* Office
    * [:octocat:Marmir](https://github.com/brianray/mm) - :star: 120 :fork_and_knife: 16 - Takes Python data structures and turns them into spreadsheets.
    * [:earth_americas:openpyxl](https://openpyxl.readthedocs.io/) - A library for reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files.
    * [:octocat:pyexcel](https://github.com/pyexcel/pyexcel) - :star: 82 :fork_and_knife: 24 - Providing one API for reading, manipulating and writing csv, ods, xls, xlsx and xlsm files.
    * [:octocat:python-docx](https://github.com/python-openxml/python-docx) - :star: 539 :fork_and_knife: 206 - Reads, queries and modifies Microsoft Word 2007/2008 docx files.
    * [:earth_americas:relatorio](http://relatorio.tryton.org/) - Templating OpenDocument files.
    * [:octocat:unoconv](https://github.com/dagwieers/unoconv) - :star: 726 :fork_and_knife: 215 - Convert between any document format supported by LibreOffice/OpenOffice.
    * [:earth_americas:XlsxWriter](https://xlsxwriter.readthedocs.io) - A Python module for creating Excel .xlsx files.
    * [:earth_americas:xlwings](http://xlwings.org/) - A BSD-licensed library that makes it easy to call Python from Excel and vice versa.
    * [xlwt](https://github.com/python-excel/xlwt) / [:octocat:xlrd](https://github.com/python-excel/xlrd) - :star: 764 :fork_and_knife: 180 - Writing and reading data and formatting information from Excel files.
* PDF
    * [:octocat:PDFMiner](https://github.com/euske/pdfminer) - :star: 1555 :fork_and_knife: 410 - A tool for extracting information from PDF documents.
    * [:octocat:PyPDF2](https://github.com/mstamy2/PyPDF2) - :star: 990 :fork_and_knife: 299 - A library capable of splitting, merging and transforming PDF pages.
    * [:earth_americas:ReportLab](http://www.reportlab.com/opensource/) - Allowing Rapid creation of rich PDF documents.
* Markdown
    * [:octocat:Mistune](https://github.com/lepture/mistune) - :star: 673 :fork_and_knife: 58 - Fastest and full featured pure Python parsers of Markdown.
    * [:octocat:Python-Markdown](https://github.com/waylan/Python-Markdown) - :star: 887 :fork_and_knife: 249 - A Python implementation of John Gruber’s Markdown.
* YAML
    * [:earth_americas:PyYAML](http://pyyaml.org/) - YAML implementations for Python.
* CSV
    * [:octocat:csvkit](https://github.com/wireservice/csvkit) - :star: 2177 :fork_and_knife: 323 - Utilities for converting to and working with CSV.
* Archive
    * [:octocat:unp](https://github.com/mitsuhiko/unp) - :star: 219 :fork_and_knife: 9 - A command line tool that can unpack archives easily.

## Natural Language Processing

*Libraries for working with human languages.*

* [:earth_americas:NLTK](http://www.nltk.org/) - A leading platform for building Python programs to work with human language data.
* [:earth_americas:Pattern](http://www.clips.ua.ac.be/pattern) - A web mining module for the Python.
* [:octocat:Jieba](https://github.com/fxsjy/jieba) - :star: 5393 :fork_and_knife: 1714 - Chinese text segmentation.
* [:octocat:SnowNLP](https://github.com/isnowfy/snownlp) - :star: 1360 :fork_and_knife: 397 - A library for processing Chinese text.
* [:earth_americas:spaCy](https://spacy.io/) - A library for industrial-strength natural language processing in Python and Cython.
* [:octocat:TextBlob](https://github.com/sloria/TextBlob) - :star: 3072 :fork_and_knife: 365 - Providing a consistent API for diving into common NLP tasks.
* [:octocat:TextGrocery](https://github.com/2shou/TextGrocery) - :star: 263 :fork_and_knife: 82 - A simple, efficient short-text classification tool based on LibLinear and Jieba.
* [:octocat:langid.py](https://github.com/saffsd/langid.py) - :star: 585 :fork_and_knife: 110 - Stand-alone language identification system.

## Documentation

*Libraries for generating project documentation.*

* [:earth_americas:Sphinx](http://www.sphinx-doc.org/en/latest/) - Python Documentation generator.
    * [awesome-sphinxdoc](https://github.com/yoloseem/awesome-sphinxdoc)
* [:earth_americas:MkDocs](http://www.mkdocs.org/) - Markdown friendly documentation generator.
* [:octocat:pdoc](https://github.com/BurntSushi/pdoc) - :star: 219 :fork_and_knife: 39 - Epydoc replacement to auto generate API documentation for Python libraries.
* [:octocat:Pycco](https://github.com/pycco-docs/pycco) - :star: 495 :fork_and_knife: 109 - The literate-programming-style documentation generator.

## Configuration

*Libraries for storing and parsing configuration options.*

* [config](https://www.red-dove.com/config-doc/) - Hierarchical config from the author of [:earth_americas:logging](https://docs.python.org/2/library/logging.html).
* [:earth_americas:ConfigObj](http://www.voidspace.org.uk/python/configobj.html) - INI file parser with validation.
* [:earth_americas:ConfigParser](https://docs.python.org/2/library/configparser.html) - (Python standard library) INI file parser.
* [:earth_americas:profig](http://profig.readthedocs.org/en/default/) - Config from multiple formats with value conversion.
* [:octocat:python-decouple](https://github.com/henriquebastos/python-decouple) - :star: 251 :fork_and_knife: 21 - Strict separation of settings from code.

## Command-line Tools

*Libraries for building command-line application.*

* Command-line Application Development
    * [:octocat:asciimatics](https://github.com/peterbrittain/asciimatics) - :star: 286 :fork_and_knife: 9 - Cross-platform, full-screen terminal package (i.e.  mouse/keyboard input and coloured, positioned text output) complete with high-level API for complex animations and special effects.
    * [:earth_americas:cement](http://builtoncement.com/) - CLI Application Framework for Python.
    * [:earth_americas:click](http://click.pocoo.org/dev/) - A package for creating beautiful command line interfaces in a composable way.
    * [:earth_americas:cliff](http://docs.openstack.org/developer/cliff/) - A framework for creating command-line programs with multi-level commands.
    * [:octocat:clint](https://github.com/kennethreitz/clint) - :star: 2016 :fork_and_knife: 182 - Python Command-line Application Tools.
    * [:earth_americas:colorama](https://pypi.python.org/pypi/colorama) - Cross-platform colored terminal text.
    * [:earth_americas:docopt](http://docopt.org/) - Pythonic command line arguments parser.
    * [:octocat:Gooey](https://github.com/chriskiehl/Gooey) - :star: 4084 :fork_and_knife: 201 - Turn command line programs into a full GUI application with one line
    * [:octocat:python-prompt-toolkit](https://github.com/jonathanslenders/python-prompt-toolkit) - :star: 2604 :fork_and_knife: 131 - A Library for building powerful interactive command lines.
* Productivity Tools
    * [:octocat:aws-cli](https://github.com/aws/aws-cli) - :star: 3928 :fork_and_knife: 609 - A universal command-line interface for Amazon Web Services.
    * [:octocat:bashplotlib](https://github.com/glamp/bashplotlib) - :star: 553 :fork_and_knife: 45 - Making basic plots in the terminal.
    * [:octocat:caniusepython3](https://github.com/brettcannon/caniusepython3) - :star: 241 :fork_and_knife: 24 - Determine what projects are blocking you from porting to Python 3.
    * [:octocat:cookiecutter](https://github.com/audreyr/cookiecutter) - :star: 3455 :fork_and_knife: 420 - A command-line utility that creates projects from cookiecutters (project templates).
    * [:octocat:doitlive](https://github.com/sloria/doitlive) - :star: 711 :fork_and_knife: 22 - A tool for live presentations in the terminal.
    * [:octocat:howdoi](https://github.com/gleitz/howdoi) - :star: 4432 :fork_and_knife: 394 - Instant coding answers via the command line.
    * [:octocat:httpie](https://github.com/jkbrzt/httpie) - :star: 23953 :fork_and_knife: 1479 - A command line HTTP client, a user-friendly cURL replacement.
    * [:octocat:PathPicker](https://github.com/facebook/PathPicker) - :star: 2900 :fork_and_knife: 164 - Select files out of bash output.
    * [:octocat:percol](https://github.com/mooz/percol) - :star: 2067 :fork_and_knife: 95 - Adds flavor of interactive selection to the traditional pipe concept on UNIX.
    * [:octocat:SAWS](https://github.com/donnemartin/saws) - :star: 2887 :fork_and_knife: 103 - A Supercharged AWS CLI.
    * [:octocat:thefuck](https://github.com/nvbn/thefuck) - :star: 20545 :fork_and_knife: 960 - Correcting your previous console command.
    * [:octocat:try](https://github.com/timofurrer/try) - :star: 289 :fork_and_knife: 11 - A dead simple CLI to try out python packages - It's never been easier.
    * [:octocat:mycli](https://github.com/dbcli/mycli) - :star: 2752 :fork_and_knife: 144 - A Terminal Client for MySQL with AutoCompletion and Syntax Highlighting.
    * [:octocat:pgcli](https://github.com/dbcli/pgcli) - :star: 4610 :fork_and_knife: 182 - Postgres CLI with autocompletion and syntax highlighting.

## Downloader

*Libraries for downloading.*

* [:octocat:s3cmd](https://github.com/s3tools/s3cmd) - :star: 1884 :fork_and_knife: 594 - A command line tool for managing Amazon S3 and CloudFront.
* [:octocat:s4cmd](https://github.com/bloomreach/s4cmd) - :star: 418 :fork_and_knife: 82 - Super S3 command line tool, good for higher performance.
* [:earth_americas:you-get](https://www.soimort.org/you-get/) - A YouTube/Youku/Niconico video downloader written in Python 3.
* [:earth_americas:youtube-dl](http://rg3.github.io/youtube-dl/) - A small command-line program to download videos from YouTube.

## Imagery

*Libraries for manipulating images.*

* [pillow](https://github.com/python-pillow/Pillow) - Pillow is the friendly [:earth_americas:PIL](http://www.pythonware.com/products/pil/) fork.
* [:octocat:hmap](https://github.com/rossgoodwin/hmap) - :star: 112 :fork_and_knife: 6 - Image histogram remapping.
* [:earth_americas:imgSeek](https://sourceforge.net/projects/imgseek/) - A project for searching a collection of images using visual similarity.
* [:octocat:nude.py](https://github.com/hhatto/nude.py) - :star: 370 :fork_and_knife: 51 - Nudity detection.
* [:earth_americas:pyBarcode](https://pythonhosted.org/pyBarcode/) - Create barcodes in Python without needing PIL.
* [:octocat:pygram](https://github.com/ajkumar25/pygram) - :star: 41 :fork_and_knife: 6 - Instagram-like image filters.
* [:octocat:python-qrcode](https://github.com/lincolnloop/python-qrcode) - :star: 883 :fork_and_knife: 200 - A pure Python QR Code generator.
* [:octocat:Quads](https://github.com/fogleman/Quads) - :star: 569 :fork_and_knife: 49 - Computer art based on quadtrees.
* [:earth_americas:scikit-image](http://scikit-image.org/) - A Python library for (scientific) image processing.
* [:octocat:thumbor](https://github.com/thumbor/thumbor) - :star: 3946 :fork_and_knife: 398 - A smart imaging service. It enables on-demand crop, re-sizing and flipping of images.
* [wand](https://github.com/dahlia/wand) - Python bindings for [:earth_americas:MagickWand](http://www.imagemagick.org/script/magick-wand.php), C API for ImageMagick.

## OCR

*Libraries for Optical Character Recognition.*

* [:octocat:pyocr](https://github.com/jflesch/pyocr) - :star: 304 :fork_and_knife: 57 - A wrapper for Tesseract and Cuneiform.
* [pytesseract](https://github.com/madmaze/pytesseract) - Another wrapper for [Google Tesseract OCR](https://github.com/tesseract-ocr).

## Audio

*Libraries for manipulating audio.*

* [:octocat:audiolazy](https://github.com/danilobellini/audiolazy) - :star: 225 :fork_and_knife: 25 - Expressive Digital Signal Processing (DSP) package for Python.
* [:octocat:audioread](https://github.com/beetbox/audioread) - :star: 98 :fork_and_knife: 36 - Cross-library (GStreamer + Core Audio + MAD + FFmpeg) audio decoding.
* [beets](http://beets.io/) - A music library manager and [:earth_americas:MusicBrainz](https://musicbrainz.org/) tagger.
* [:octocat:dejavu](https://github.com/worldveil/dejavu) - :star: 2113 :fork_and_knife: 392 - Audio fingerprinting and recognition.
* [django-elastic-transcoder](https://github.com/StreetVoice/django-elastic-transcoder) - Django + [:earth_americas:Amazon Elastic Transcoder](http://aws.amazon.com/elastictranscoder/).
* [:earth_americas:eyeD3](http://eyed3.nicfit.net/) - A tool for working with audio files, specifically MP3 files containing ID3 metadata.
* [:earth_americas:id3reader](http://nedbatchelder.com/code/modules/id3reader.py) - A Python module for reading MP3 meta data.
* [:octocat:m3u8](https://github.com/globocom/m3u8) - :star: 172 :fork_and_knife: 73 - A module for parsing m3u8 file.
* [:earth_americas:mutagen](https://bitbucket.org/lazka/mutagen) - A Python module to handle audio metadata.
* [:octocat:pydub](https://github.com/jiaaro/pydub) - :star: 1416 :fork_and_knife: 147 - Manipulate audio with a simple and easy high level interface.
* [pyechonest](https://github.com/echonest/pyechonest) - Python client for the [:earth_americas:Echo Nest](http://developer.echonest.com/) API.
* [:earth_americas:talkbox](http://scikits.appspot.com/talkbox) - A Python library for speech/signal processing.
* [:octocat:TimeSide](https://github.com/Parisson/TimeSide) - :star: 163 :fork_and_knife: 23 - Open web audio processing framework.
* [:octocat:tinytag](https://github.com/devsnd/tinytag) - :star: 187 :fork_and_knife: 24 - A library for reading music meta data of MP3, OGG, FLAC and Wave files.
* [:earth_americas:mingus](http://bspaans.github.io/python-mingus/) - An advanced music theory and notation package with MIDI file and playback support.

## Video

*Libraries for manipulating video and GIFs.*

* [:earth_americas:moviepy](http://zulko.github.io/moviepy/) - A module for script-based movie editing with many formats, including animated GIFs.
* [:octocat:scikit-video](https://github.com/aizvorski/scikit-video) - :star: 38 :fork_and_knife: 4 - Video processing routines for SciPy.

## Geolocation

*Libraries for geocoding addresses and working with latitudes and longitudes.*

* [:earth_americas:GeoDjango](https://docs.djangoproject.com/en/dev/ref/contrib/gis/) - A world-class geographic web framework.
* [:octocat:GeoIP](https://github.com/maxmind/geoip-api-python) - :star: 131 :fork_and_knife: 33 - Python API for MaxMind GeoIP Legacy Database.
* [:octocat:geojson](https://github.com/frewsxcv/python-geojson) - :star: 207 :fork_and_knife: 28 - Python bindings and utilities for GeoJSON.
* [:octocat:geopy](https://github.com/geopy/geopy) - :star: 1099 :fork_and_knife: 274 - Python Geocoding Toolbox.
* [:octocat:pygeoip](https://github.com/appliedsec/pygeoip) - :star: 417 :fork_and_knife: 86 - Pure Python GeoIP API.
* [:octocat:django-countries](https://github.com/SmileyChris/django-countries) - :star: 261 :fork_and_knife: 83 - A Django app that provides country choices for use with forms, flag icons static files, and a country field for models.

## HTTP

*Libraries for working with HTTP.*

* [:earth_americas:requests](http://docs.python-requests.org/en/latest/) - HTTP Requests for Humans™.
* [:octocat:grequests](https://github.com/kennethreitz/grequests) - :star: 1451 :fork_and_knife: 176 - requests + gevent for asynchronous HTTP requests.
* [:octocat:httplib2](https://github.com/jcgregorio/httplib2) - :star: 363 :fork_and_knife: 191 - Comprehensive HTTP client library.
* [:octocat:treq](https://github.com/twisted/treq) - :star: 275 :fork_and_knife: 72 - Python requests like API built on top of Twisted's HTTP client.
* [:octocat:urllib3](https://github.com/shazow/urllib3) - :star: 1057 :fork_and_knife: 353 - A HTTP library with thread-safe connection pooling, file post support, sanity friendly.

## Database

*Databases implemented in Python.*

* [:earth_americas:pickleDB](https://pythonhosted.org/pickleDB/) - A simple and lightweight key-value store for Python.
* [:earth_americas:PipelineDB](https://www.pipelinedb.com/) - The Streaming SQL Database.
* [:octocat:TinyDB](https://github.com/msiemens/tinydb) - :star: 1008 :fork_and_knife: 64 - A tiny, document-oriented database.
* [:earth_americas:ZODB](http://www.zodb.org/en/latest/) - A native object database for Python. A key-value and object graph database.

## Database Drivers

*Libraries for connecting and operating databases.*

* MySQL - [awesome-mysql](http://shlomi-noach.github.io/awesome-mysql/)
    * [:earth_americas:mysql-python](https://sourceforge.net/projects/mysql-python/) - The MySQL database connector for Python.
    * [:octocat:mysqlclient](https://github.com/PyMySQL/mysqlclient-python) - :star: 341 :fork_and_knife: 48 - mysql-python fork supporting Python 3.
    * [:earth_americas:oursql](https://pythonhosted.org/oursql/) - A better MySQL connector with support for native prepared statements and BLOBs.
    * [:octocat:PyMySQL](https://github.com/PyMySQL/PyMySQL) - :star: 1761 :fork_and_knife: 404 - Pure Python MySQL driver compatible to mysql-python.
* PostgreSQL
    * [:earth_americas:psycopg2](http://initd.org/psycopg/) - The most popular PostgreSQL adapter for Python.
    * [:octocat:queries](https://github.com/gmr/queries) - :star: 143 :fork_and_knife: 13 - A wrapper of the psycopg2 library for interacting with PostgreSQL.
    * [:octocat:txpostgres](https://github.com/wulczer/txpostgres) - :star: 81 :fork_and_knife: 21 - Twisted based asynchronous driver for PostgreSQL.
* Other Relational Databases
    * [:earth_americas:apsw](http://rogerbinns.github.io/apsw/) - Another Python SQLite wrapper.
    * [:octocat:dataset](https://github.com/pudo/dataset) - :star: 2242 :fork_and_knife: 128 - Store Python dicts in a database - works with SQLite, MySQL, and PostgreSQL.
    * [:earth_americas:pymssql](http://www.pymssql.org/en/latest/) - A simple database interface to Microsoft SQL Server.
* NoSQL Databases
    * [:octocat:cassandra-python-driver](https://github.com/datastax/python-driver) - :star: 511 :fork_and_knife: 244 - Python driver for Cassandra.
    * [:octocat:HappyBase](https://github.com/wbolster/happybase) - :star: 249 :fork_and_knife: 73 - A developer-friendly library for Apache HBase.
    * [:octocat:Plyvel](https://github.com/wbolster/plyvel) - :star: 120 :fork_and_knife: 21 - A fast and feature-rich Python interface to LevelDB.
    * [:earth_americas:py2neo](http://py2neo.org/2.0/) - Python wrapper client for Neo4j's restful interface.
    * [:octocat:pycassa](https://github.com/pycassa/pycassa) - :star: 493 :fork_and_knife: 141 - Python Thrift driver for Cassandra.
    * [:earth_americas:PyMongo](https://docs.mongodb.org/ecosystem/drivers/python/) - The official Python client for MongoDB.
    * [:octocat:redis-py](https://github.com/andymccurdy/redis-py) - :star: 4173 :fork_and_knife: 1051 - The Redis Python Client.
    * [:octocat:telephus](https://github.com/driftx/Telephus) - :star: 93 :fork_and_knife: 34 - Twisted based client for Cassandra.
    * [:octocat:txRedis](https://github.com/deldotdr/txRedis) - :star: 115 :fork_and_knife: 32 - Twisted based client for Redis.

## ORM

*Libraries that implement Object-Relational Mapping or data mapping techniques.*

* Relational Databases
    * [:earth_americas:Django Models](https://docs.djangoproject.com/en/dev/topics/db/models/) - A part of Django.
    * [:earth_americas:SQLAlchemy](http://www.sqlalchemy.org/) - The Python SQL Toolkit and Object Relational Mapper.
        * [awesome-sqlalchemy](https://github.com/dahlia/awesome-sqlalchemy)
    * [:octocat:Peewee](https://github.com/coleifer/peewee) - :star: 2880 :fork_and_knife: 517 - A small, expressive ORM.
    * [:earth_americas:PonyORM](https://ponyorm.com/) - ORM that provides a generator-oriented interface to SQL.
    * [:earth_americas:python-sql](https://pypi.python.org/pypi/python-sql) - Write SQL queries pythonically.
* NoSQL Databases
    * [:octocat:django-mongodb-engine](https://github.com/django-nonrel/mongodb-engine) - :star: 642 :fork_and_knife: 188 - Django MongoDB Backend.
    * [PynamoDB](https://github.com/jlafon/PynamoDB) - A Pythonic interface for [:earth_americas:Amazon DynamoDB](https://aws.amazon.com/dynamodb/).
    * [:octocat:flywheel](https://github.com/mathcamp/flywheel) - :star: 59 :fork_and_knife: 8 - Object mapper for Amazon DynamoDB.
    * [:earth_americas:MongoEngine](http://mongoengine.org/) - A Python Object-Document-Mapper for working with MongoDB.
    * [:octocat:hot-redis](https://github.com/stephenmcd/hot-redis) - :star: 187 :fork_and_knife: 13 - Rich Python data types for Redis.
    * [:octocat:redisco](https://github.com/kiddouk/redisco) - :star: 303 :fork_and_knife: 59 - A Python Library for Simple Models and Containers Persisted in Redis.
* Others
    * [:octocat:butterdb](https://github.com/Widdershin/butterdb) - :star: 308 :fork_and_knife: 14 - A Python ORM for Google Drive Spreadsheets.

## Web Frameworks

*Full stack web frameworks.*

* [:earth_americas:Django](https://www.djangoproject.com/) - The most popular web framework in Python.
    * [awesome-django](https://github.com/rosarior/awesome-django)
* [:earth_americas:Flask](http://flask.pocoo.org/) - A microframework for Python.
    * [awesome-flask](https://github.com/humiaozuzu/awesome-flask)
* [:earth_americas:Pyramid](http://www.pylonsproject.org/) - A small, fast, down-to-earth, open source Python web framework.
    * [awesome-pyramid](https://github.com/uralbash/awesome-pyramid)
* [:earth_americas:Bottle](http://bottlepy.org/docs/dev/index.html) - A fast, simple and lightweight WSGI micro web-framework.
* [:earth_americas:CherryPy](http://www.cherrypy.org/) - A minimalist Python web framework, HTTP/1.1-compliant and WSGI thread-pooled.
* [:earth_americas:TurboGears](http://www.turbogears.org/) - A microframework that can scale up to a full stack solution.
* [:earth_americas:web.py](http://webpy.org/) - A web framework for Python that is as simple as it is powerful.
* [:earth_americas:web2py](http://www.web2py.com) - A full stack web framework and platform focused in the ease of use.
* [:earth_americas:Tornado](http://www.tornadoweb.org/en/latest/) - A Web framework and asynchronous networking library.

## Serverless Frameworks

*Frameworks for developing serverless Python code.*

* [apex](https://github.com/apex/apex) - Build, deploy, and manage [:earth_americas:AWS Lambda](https://aws.amazon.com/lambda/) functions with ease.
* [:octocat:Zappa](https://github.com/Miserlou/Zappa) - :star: 936 :fork_and_knife: 66 - A tool for deploying WSGI applications on AWS Lambda and API Gateway.
* [:octocat:python-lambda](https://github.com/nficano/python-lambda) - :star: 178 :fork_and_knife: 17 - A toolkit for developing and deploying Python code in AWS Lambda.

## Permissions

*Libraries that allow or deny users access to data or functionality.*

* [:octocat:Carteblanche](https://github.com/neuman/python-carteblanche/) - :star: 26 :fork_and_knife: 3 - Module to align code with thoughts of users and designers. Also magically handles navigation and permissions.
* [:octocat:django-guardian](https://github.com/django-guardian/django-guardian) - :star: 1139 :fork_and_knife: 315 - Implementation of per object permissions for Django 1.2+
* [:octocat:django-rules](https://github.com/dfunckt/django-rules) - :star: 305 :fork_and_knife: 19 - A tiny but powerful app providing object-level permissions to Django, without requiring a database.

## CMS

*Content Management Systems.*

* [:earth_americas:django-cms](http://www.django-cms.org/en/) - An Open source enterprise CMS based on the Django.
* [:earth_americas:djedi-cms](http://djedi-cms.org/) - A lightweight but yet powerful Django CMS with plugins, inline editing and performance in mind.
* [:earth_americas:FeinCMS](http://www.feincms.org/) - One of the most advanced Content Management Systems built on Django.
* [:earth_americas:Kotti](http://kotti.pylonsproject.org/) - A high-level, Pythonic web application framework built on Pyramid.
* [:earth_americas:Mezzanine](http://mezzanine.jupo.org/) - A powerful, consistent, and flexible content management platform.
* [:earth_americas:Opps](http://opps.github.io/opps/) - A Django-based CMS for magazines, newspapers websites and portals with high-traffic.
* [:earth_americas:Plone](https://plone.org/) - A CMS built on top of the open source application server Zope.
* [:earth_americas:Quokka](http://quokkaproject.org/) - Flexible, extensible, small CMS powered by Flask and MongoDB.
* [:earth_americas:Wagtail](https://wagtail.io/) - A Django content management system.
* [:earth_americas:Widgy](https://wid.gy/) - Last CMS framework, based on Django.

## E-commerce

*Frameworks and libraries for e-commerce and payments.*

* [:earth_americas:django-oscar](http://oscarcommerce.com/) - An open-source e-commerce framework for Django.
* [:octocat:django-shop](https://github.com/awesto/django-shop) - :star: 1069 :fork_and_knife: 449 - A Django based shop system.
* [:octocat:Cartridge](https://github.com/stephenmcd/cartridge) - :star: 465 :fork_and_knife: 226 - A shopping cart app built using the Mezzanine.
* [:earth_americas:shoop](https://www.shoop.io/en/) - An open source E-Commerce platform based on Django.
* [:octocat:alipay](https://github.com/lxneng/alipay) - :star: 139 :fork_and_knife: 44 - Unofficial Alipay API for Python.
* [:octocat:merchant](https://github.com/agiliq/merchant) - :star: 830 :fork_and_knife: 145 - A Django app to accept payments from various payment processors.
* [:octocat:money](https://github.com/carlospalol/money) - :star: 64 :fork_and_knife: 8 - Money class with optional CLDR-backed locale-aware formatting and an extensible currency exchange solution.
* [:octocat:python-currencies](https://github.com/Alir3z4/python-currencies) - :star: 20 :fork_and_knife: 0 - Display money format and its filthy currencies.

## RESTful API

*Libraries for developing RESTful APIs.*

* Django
    * [:earth_americas:django-rest-framework](http://www.django-rest-framework.org/) - A powerful and flexible toolkit to build web APIs.
    * [:earth_americas:django-tastypie](http://tastypieapi.org/) - Creating delicious APIs for Django apps.
    * [:octocat:django-formapi](https://github.com/5monkeys/django-formapi) - :star: 22 :fork_and_knife: 11 - Create JSON APIs with Django's form validation.
* Flask
    * [:earth_americas:flask-api](http://www.flaskapi.org/) - Browsable Web APIs for Flask.
    * [:octocat:flask-restful](https://github.com/flask-restful/flask-restful) - :star: 2030 :fork_and_knife: 423 - Quickly building REST APIs for Flask.
    * [:octocat:flask-restless](https://github.com/jfinkels/flask-restless) - :star: 647 :fork_and_knife: 217 - Generating RESTful APIs for database models defined with SQLAlchemy.
    * [:octocat:flask-api-utils](https://github.com/marselester/flask-api-utils) - :star: 28 :fork_and_knife: 2 - Taking care of API representation and authentication for Flask.
    * [:octocat:eve](https://github.com/nicolaiarocci/eve) - :star: 3307 :fork_and_knife: 443 - REST API framework powered by Flask, MongoDB and good intentions.
* Pyramid
    * [:octocat:cornice](https://github.com/mozilla-services/cornice) - :star: 276 :fork_and_knife: 128 - A RESTful framework for Pyramid.
* Framework agnostic
    * [:earth_americas:falcon](http://falconframework.org/) - A high-performance framework for building cloud APIs and web app backends.
    * [:octocat:hug](https://github.com/timothycrosley/hug) - :star: 3169 :fork_and_knife: 128 - A Python3 framework for cleanly exposing APIs over HTTP and the Command Line with automatic documentation and validation.
    * [:octocat:sandman](https://github.com/jeffknupp/sandman) - :star: 2224 :fork_and_knife: 181 - Automated REST APIs for existing database-driven systems.
    * [:octocat:restless](https://github.com/toastdriven/restless) - :star: 542 :fork_and_knife: 63 - Framework agnostic REST framework based on lessons learned from Tastypie.
    * [:octocat:ripozo](https://github.com/vertical-knowledge/ripozo) - :star: 155 :fork_and_knife: 19 - Quickly creating REST/HATEOAS/Hypermedia APIs.

## Serialization

*Libraries for serializing complex data types*

* [:octocat:marshmallow](https://github.com/marshmallow-code/marshmallow) - :star: 1150 :fork_and_knife: 139 - marshmallow is an ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes.

## Authentication

*Libraries for implementing authentications schemes.*

* OAuth
    * [:earth_americas:Authomatic](http://peterhudec.github.io/authomatic/) - Simple but powerful framework agnostic authentication/authorization client.
    * [:octocat:django-allauth](https://github.com/pennersr/django-allauth) - :star: 2398 :fork_and_knife: 877 - Authentication app for Django that "just works."
    * [:octocat:django-oauth-toolkit](https://github.com/evonove/django-oauth-toolkit) - :star: 760 :fork_and_knife: 230 - OAuth2 goodies for the Djangonauts.
    * [:octocat:django-oauth2-provider](https://github.com/caffeinehit/django-oauth2-provider) - :star: 294 :fork_and_knife: 234 - Providing OAuth2 access to Django app.
    * [:octocat:Flask-OAuthlib](https://github.com/lepture/flask-oauthlib) - :star: 714 :fork_and_knife: 199 - OAuth 1.0/a, 2.0 implementation of client and provider for Flask.
    * [:octocat:OAuthLib](https://github.com/idan/oauthlib) - :star: 1141 :fork_and_knife: 255 - A generic and thorough implementation of the OAuth request-signing logic.
    * [:octocat:python-oauth2](https://github.com/joestump/python-oauth2) - :star: 2420 :fork_and_knife: 947 - A fully tested, abstract interface to creating OAuth clients and servers.
    * [:octocat:python-social-auth](https://github.com/omab/python-social-auth) - :star: 2302 :fork_and_knife: 1000 - An easy-to-setup social authentication mechanism.
    * [:octocat:rauth](https://github.com/litl/rauth) - :star: 1425 :fork_and_knife: 148 - A Python library for OAuth 1.0/a, 2.0, and Ofly.
    * [:octocat:sanction](https://github.com/demianbrecht/sanction) - :star: 154 :fork_and_knife: 38 - A dead simple OAuth2 client implementation.
* Others
    * [:octocat:jose](https://github.com/demonware/jose) - :star: 47 :fork_and_knife: 16 - JavaScript Object Signing and Encryption draft implementation.
    * [:octocat:PyJWT](https://github.com/jpadilla/pyjwt) - :star: 819 :fork_and_knife: 128 - Implementation of the JSON Web Token draft 01.
    * [:octocat:python-jws](https://github.com/brianloveswords/python-jws) - :star: 40 :fork_and_knife: 16 - Implementation of JSON Web Signatures draft 02.
    * [:octocat:python-jwt](https://github.com/davedoesdev/python-jwt) - :star: 99 :fork_and_knife: 11 - Module for generating and verifying JSON Web Tokens.

## Template Engine

*Libraries and tools for templating and lexing.*

* [:octocat:Jinja2](https://github.com/pallets/jinja) - :star: 3358 :fork_and_knife: 688 - A modern and designer friendly templating language.
* [:earth_americas:Genshi](https://genshi.edgewall.org/) - Python templating toolkit for generation of web-aware output.
* [:earth_americas:Mako](http://www.makotemplates.org/) - Hyperfast and lightweight templating for the Python platform.

## Queue

*Libraries for working with event and task queues.*

* [:earth_americas:celery](http://www.celeryproject.org/) - An asynchronous task queue/job queue based on distributed message passing.
* [:octocat:huey](https://github.com/coleifer/huey) - :star: 915 :fork_and_knife: 94 - Little multi-threaded task queue.
* [:octocat:mrq](https://github.com/pricingassistant/mrq) - :star: 387 :fork_and_knife: 29 - Mr. Queue - A distributed worker task queue in Python using Redis & gevent.
* [:earth_americas:rq](http://python-rq.org/) - Simple job queues for Python.
* [:octocat:simpleq](https://github.com/rdegges/simpleq) - :star: 103 :fork_and_knife: 9 - A simple, infinitely scalable, Amazon SQS based queue.

## Search

*Libraries and software for indexing and performing search queries on data.*

* [:octocat:django-haystack](https://github.com/django-haystack/django-haystack) - :star: 1989 :fork_and_knife: 886 - Modular search for Django.
* [elasticsearch-py](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html) - The official low-level Python client for [:earth_americas:Elasticsearch](https://www.elastic.co/products/elasticsearch).
* [:octocat:elasticsearch-dsl-py](https://github.com/elastic/elasticsearch-dsl-py) - :star: 849 :fork_and_knife: 203 - The official high-level Python client for Elasticsearch.
* [:octocat:esengine](https://github.com/catholabs/esengine) - :star: 51 :fork_and_knife: 5 - ElasticSearch ODM (Object Document Mapper) for Python.
* [solrpy](https://github.com/edsu/solrpy) - A Python client for [:earth_americas:solr](http://lucene.apache.org/solr/).
* [:earth_americas:Whoosh](http://whoosh.readthedocs.io/) - A fast, pure Python search engine library.

## News Feed

*Libraries for building user's activities.*

* [:octocat:django-activity-stream](https://github.com/justquick/django-activity-stream) - :star: 1023 :fork_and_knife: 310 - Generating generic activity streams from the actions on your site.
* [:octocat:Stream-Framework](https://github.com/tschellenbach/Stream-Framework) - :star: 2156 :fork_and_knife: 267 - Building newsfeed and notification systems using Cassandra and Redis.

## Asset Management

*Tools for managing, compressing and minifying website assets.*

* [:octocat:django-compressor](https://github.com/django-compressor/django-compressor) - :star: 1684 :fork_and_knife: 486 - Compresses linked and inline JavaScript or CSS into a single cached file.
* [:octocat:django-pipeline](https://github.com/jazzband/django-pipeline) - :star: 1034 :fork_and_knife: 276 - An asset packaging library for Django.
* [:octocat:django-storages](https://github.com/jschneier/django-storages) - :star: 385 :fork_and_knife: 142 - A collection of custom storage back ends for Django.
* [:earth_americas:fanstatic](http://www.fanstatic.org/en/latest/) - Packages, optimizes, and serves static file dependencies as Python packages.
* [:earth_americas:fileconveyor](http://fileconveyor.org/) - A daemon to detect and sync files to CDNs, S3 and FTP.
* [:octocat:flask-assets](https://github.com/miracle2k/flask-assets) - :star: 267 :fork_and_knife: 72 - Helps you integrate webassets into your Flask app.
* [:octocat:jinja-assets-compressor](https://github.com/jaysonsantos/jinja-assets-compressor) - :star: 50 :fork_and_knife: 8 - A Jinja extension to compile and compress your assets.
* [:octocat:webassets](https://github.com/miracle2k/webassets) - :star: 735 :fork_and_knife: 216 - Bundles, optimizes, and manages unique cache-busting URLs for static resources.

## Caching

*Libraries for caching data.*

* [:octocat:Beaker](https://github.com/bbangert/beaker) - :star: 233 :fork_and_knife: 85 - A library for caching and sessions for use with web applications and stand-alone Python scripts and applications.
* [:octocat:django-cache-machine](https://github.com/django-cache-machine/django-cache-machine) - :star: 621 :fork_and_knife: 125 - Automatic caching and invalidation for Django models.
* [:octocat:django-cacheops](https://github.com/Suor/django-cacheops) - :star: 547 :fork_and_knife: 91 - A slick ORM cache with automatic granular event-driven invalidation.
* [:octocat:django-viewlet](https://github.com/5monkeys/django-viewlet) - :star: 54 :fork_and_knife: 12 - Render template parts with extended cache control.
* [:earth_americas:dogpile.cache](http://dogpilecache.readthedocs.io/) - dogpile.cache is next generation replacement for Beaker made by same authors.
* [:earth_americas:HermesCache](https://pypi.python.org/pypi/HermesCache) - Python caching library with tag-based invalidation and dogpile effect prevention.
* [:octocat:johnny-cache](https://github.com/jmoiron/johnny-cache) - :star: 257 :fork_and_knife: 87 - A caching framework for django applications.
* [pylibmc](https://github.com/lericson/pylibmc) - A Python wrapper around the [:earth_americas:libmemcached](http://libmemcached.org/libMemcached.html) interface.
* [:earth_americas:DiskCache](http://www.grantjenks.com/docs/diskcache/) - SQLite and file backed cache backend with faster lookups than memcached and redis.

## Email

*Libraries for sending and parsing email.*

* [:earth_americas:envelopes](http://tomekwojcik.github.io/envelopes/) - Mailing for human beings.
* [:octocat:flanker](https://github.com/mailgun/flanker) - :star: 928 :fork_and_knife: 86 - A email address and Mime parsing library.
* [:octocat:imbox](https://github.com/martinrusev/imbox) - :star: 624 :fork_and_knife: 83 - Python IMAP for Humans.
* [:octocat:inbox.py](https://github.com/kennethreitz/inbox.py) - :star: 1220 :fork_and_knife: 78 - Python SMTP Server for Humans.
* [:octocat:lamson](https://github.com/zedshaw/lamson) - :star: 548 :fork_and_knife: 151 - Pythonic SMTP Application Server.
* [:octocat:Marrow Mailer](https://github.com/marrow/mailer) - :star: 103 :fork_and_knife: 25 - High-performance extensible mail delivery framework.
* [:octocat:modoboa](https://github.com/tonioo/modoboa) - :star: 539 :fork_and_knife: 82 - A mail hosting and management platform including a modern and simplified Web UI.
* [:octocat:Nylas Sync Engine](https://github.com/nylas/sync-engine) - :star: 2973 :fork_and_knife: 266 - Providing a RESTful API on top of a powerful email sync platform.
* [:octocat:yagmail](https://github.com/kootenpv/yagmail) - :star: 526 :fork_and_knife: 25 - Yet another Gmail/SMTP client.

## Internationalization

*Libraries for working with i18n.*

* [:earth_americas:Babel](http://babel.pocoo.org/en/latest/) - An internationalization library for Python.
* [PyICU](https://github.com/ovalhub/pyicu) - A wrapper of International Components for Unicode C++ library ([:earth_americas:ICU](http://site.icu-project.org/)).

## URL Manipulation

*Libraries for parsing URLs.*

* [:octocat:furl](https://github.com/gruns/furl) - :star: 916 :fork_and_knife: 61 - A small Python library that makes manipulating URLs simple.
* [:octocat:purl](https://github.com/codeinthehole/purl) - :star: 163 :fork_and_knife: 21 - A simple, immutable URL class with a clean API for interrogation and manipulation.
* [:octocat:pyshorteners](https://github.com/ellisonleao/pyshorteners) - :star: 117 :fork_and_knife: 20 - A pure Python URL shortening lib.
* [:octocat:short_url](https://github.com/Alir3z4/python-short_url) - :star: 50 :fork_and_knife: 9 - Python implementation for generating Tiny URL and bit.ly-like URLs.
* [:octocat:webargs](https://github.com/sloria/webargs) - :star: 329 :fork_and_knife: 43 - A friendly library for parsing HTTP request arguments, with built-in support for popular web frameworks, including Flask, Django, Bottle, Tornado, and Pyramid.

## HTML Manipulation

*Libraries for working with HTML and XML.*

* [:earth_americas:BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Providing Pythonic idioms for iterating, searching, and modifying HTML or XML.
* [:octocat:bleach](https://github.com/mozilla/bleach) - :star: 1011 :fork_and_knife: 116 - A whitelist-based HTML sanitization and text linkification library.
* [:earth_americas:cssutils](https://pypi.python.org/pypi/cssutils/) - A CSS library for Python.
* [:octocat:html5lib](https://github.com/html5lib/html5lib-python) - :star: 485 :fork_and_knife: 105 - A standards-compliant library for parsing and serializing HTML documents and fragments.
* [:earth_americas:lxml](http://lxml.de/) - A very fast, easy-to-use and versatile library for handling HTML and XML.
* [:octocat:MarkupSafe](https://github.com/pallets/markupsafe) - :star: 123 :fork_and_knife: 48 - Implements a XML/HTML/XHTML Markup safe string for Python.
* [:octocat:pyquery](https://github.com/gawel/pyquery) - :star: 970 :fork_and_knife: 93 - A jQuery-like library for parsing HTML.
* [:octocat:untangle](https://github.com/stchris/untangle) - :star: 163 :fork_and_knife: 21 - Converts XML documents to Python objects for easy access.
* [:octocat:xhtml2pdf](https://github.com/xhtml2pdf/xhtml2pdf) - :star: 1147 :fork_and_knife: 414 - HTML/CSS to PDF converter.
* [:octocat:xmltodict](https://github.com/martinblech/xmltodict) - :star: 2025 :fork_and_knife: 198 - Working with XML feel like you are working with JSON.

## Web Crawling

*Libraries for scraping websites.*

* [:earth_americas:Scrapy](http://scrapy.org/) - A fast high-level screen scraping and web crawling framework.
* [:octocat:cola](https://github.com/chineking/cola) - :star: 944 :fork_and_knife: 452 - A distributed crawling framework.
* [:octocat:Demiurge](https://github.com/matiasb/demiurge) - :star: 36 :fork_and_knife: 5 - PyQuery-based scraping micro-framework.
* [:earth_americas:feedparser](http://pythonhosted.org/feedparser/) - Universal feed parser.
* [:earth_americas:Grab](http://grablib.org/) - Site scraping framework.
* [:octocat:MechanicalSoup](https://github.com/hickford/MechanicalSoup) - :star: 1362 :fork_and_knife: 70 - A Python library for automating interaction with websites.
* [:octocat:portia](https://github.com/scrapinghub/portia) - :star: 4246 :fork_and_knife: 622 - Visual scraping for Scrapy.
* [:octocat:pyspider](https://github.com/binux/pyspider) - :star: 6707 :fork_and_knife: 1741 - A powerful spider system.
* [:octocat:RoboBrowser](https://github.com/jmcarp/robobrowser) - :star: 2420 :fork_and_knife: 156 - A simple, Pythonic library for browsing the web without a standalone web browser.

## Web Content Extracting

*Libraries for extracting web contents.*

* [:octocat:Haul](https://github.com/vinta/Haul) - :star: 63 :fork_and_knife: 17 - An Extensible Image Crawler.
* [:octocat:html2text](https://github.com/Alir3z4/html2text) - :star: 248 :fork_and_knife: 54 - Convert HTML to Markdown-formatted text.
* [:octocat:lassie](https://github.com/michaelhelmick/lassie) - :star: 307 :fork_and_knife: 19 - Web Content Retrieval for Humans.
* [:octocat:micawber](https://github.com/coleifer/micawber) - :star: 303 :fork_and_knife: 44 - A small library for extracting rich content from URLs.
* [:octocat:newspaper](https://github.com/codelucas/newspaper) - :star: 3315 :fork_and_knife: 446 - News extraction, article extraction and content curation in Python.
* [:octocat:opengraph](https://github.com/erikriver/opengraph) - :star: 72 :fork_and_knife: 44 - A Python module to parse the Open Graph Protocol
* [:octocat:python-goose](https://github.com/grangier/python-goose) - :star: 1947 :fork_and_knife: 468 - HTML Content/Article Extractor.
* [:octocat:python-readability](https://github.com/buriy/python-readability) - :star: 948 :fork_and_knife: 187 - Fast Python port of arc90's readability tool.
* [:octocat:sanitize](https://github.com/Alir3z4/python-sanitize) - :star: 19 :fork_and_knife: 1 - Bringing sanity to world of messed-up data.
* [:octocat:sumy](https://github.com/miso-belica/sumy) - :star: 565 :fork_and_knife: 116 - A module for automatic summarization of text documents and HTML pages.
* [:octocat:textract](https://github.com/deanmalmgren/textract) - :star: 1703 :fork_and_knife: 149 - Extract text from any document, Word, PowerPoint, PDFs, etc.

## Forms

*Libraries for working with forms.*

* [:octocat:Deform](https://github.com/Pylons/deform) - :star: 173 :fork_and_knife: 109 - Python HTML form generation library influenced by the formish form generation library.
* [:octocat:django-bootstrap3](https://github.com/dyve/django-bootstrap3) - :star: 1403 :fork_and_knife: 448 - Bootstrap 3 integration with Django.
* [:octocat:django-crispy-forms](https://github.com/maraujop/django-crispy-forms) - :star: 2391 :fork_and_knife: 425 - A Django app which lets you create beautiful forms in a very elegant and DRY way.
* [:octocat:django-remote-forms](https://github.com/WiserTogether/django-remote-forms) - :star: 144 :fork_and_knife: 71 - A platform independent Django form serializer.
* [:octocat:WTForms](https://github.com/wtforms/wtforms) - :star: 520 :fork_and_knife: 181 - A flexible forms validation and rendering library.

## Data Validation

*Libraries for validating data. Used for forms in many cases.*

* [:octocat:Schematics](https://github.com/schematics/schematics) - :star: 1579 :fork_and_knife: 200 - Data Structure Validation.
* [:octocat:schema](https://github.com/keleshev/schema) - :star: 859 :fork_and_knife: 76 - A library for validating Python data structures.
* [jsonschema](https://github.com/Julian/jsonschema) - An implementation of [:earth_americas:JSON Schema](http://json-schema.org/) for Python.
* [:octocat:Cerberus](https://github.com/nicolaiarocci/cerberus/) - :star: 518 :fork_and_knife: 79 - A lightweight and extensible data validation library.
* [:earth_americas:colander](http://docs.pylonsproject.org/projects/colander/en/latest/) - Validating and deserializing data obtained via XML, JSON, an HTML form post.
* [:octocat:voluptuous](https://github.com/alecthomas/voluptuous) - :star: 605 :fork_and_knife: 92 - A Python data validation library.
* [:octocat:valideer](https://github.com/podio/valideer) - :star: 166 :fork_and_knife: 7 - Lightweight extensible data validation and adaptation library.

## Anti-spam

*Libraries for fighting spam.*

* [:octocat:django-simple-captcha](https://github.com/mbi/django-simple-captcha) - :star: 362 :fork_and_knife: 151 - A simple and highly customizable Django app to add captcha images to any Django form.
* [:octocat:django-simple-spam-blocker](https://github.com/moqada/django-simple-spam-blocker) - :star: 9 :fork_and_knife: 1 - Simple spam blocker for Django.

## Tagging

*Libraries for tagging items.*

* [:octocat:django-taggit](https://github.com/alex/django-taggit) - :star: 1470 :fork_and_knife: 403 - Simple tagging for Django.

## Admin Panels

*Libraries for administrative interfaces.*

* [:octocat:Ajenti](https://github.com/Eugeny/ajenti) - :star: 162 :fork_and_knife: 33 - The admin panel your servers deserve.
* [:earth_americas:django-suit](http://djangosuit.com/) - Alternative Django Admin-Interface (free only for Non-commercial use).
* [:octocat:django-xadmin](https://github.com/sshwsfc/xadmin) - :star: 1642 :fork_and_knife: 515 - Drop-in replacement of Django admin comes with lots of goodies.
* [:octocat:flask-admin](https://github.com/flask-admin/flask-admin) - :star: 1757 :fork_and_knife: 586 - Simple and extensible administrative interface framework for Flask.
* [:octocat:flower](https://github.com/mher/flower) - :star: 1743 :fork_and_knife: 337 - Real-time monitor and web admin for Celery.
* [:earth_americas:Grappelli](http://grappelliproject.com) – A jazzy skin for the Django Admin-Interface.
* [:octocat:Wooey](https://github.com/wooey/wooey) - :star: 643 :fork_and_knife: 54 - A Django app which creates automatic web UIs for Python scripts.

## Static Site Generator

*Static site generator is a software that takes some text + templates as input and produces HTML files on the output.*

* [:earth_americas:Pelican](http://blog.getpelican.com/) - Uses Markdown or ReST for content and Jinja 2 for themes. Supports DVCS, Disqus. AGPL.
* [:octocat:Cactus](https://github.com/koenbok/Cactus/) - :star: 2759 :fork_and_knife: 261 – Static site generator for designers.
* [:earth_americas:Hyde](http://hyde.github.io/) - Jinja2-based static web site generator.
* [:earth_americas:Nikola](https://www.getnikola.com/) - A static website and blog generator.
* [:earth_americas:Tinkerer](http://tinkerer.me/) - Tinkerer is a blogging engine/.static website generator powered by Sphinx.
* [:earth_americas:Lektor](https://www.getlektor.com/) - An easy to use static CMS and blog engine.

## Processes

*Libraries for starting and communicating with OS processes.*

* [envoy](https://github.com/kennethreitz/envoy) - Python [:earth_americas:subprocess](https://docs.python.org/2/library/subprocess.html) for Humans™.
* [:earth_americas:sarge](http://sarge.readthedocs.io/) - Yet another wrapper for subprocess.
* [:octocat:sh](https://github.com/amoffat/sh) - :star: 3373 :fork_and_knife: 282 - A full-fledged subprocess replacement for Python.

## Concurrency and Parallelism

*Libraries for concurrent and parallel execution.*

* [:earth_americas:multiprocessing](https://docs.python.org/2/library/multiprocessing.html) - (Python standard library) Process-based "threading" interface.
* [:earth_americas:threading](https://docs.python.org/2/library/threading.html) - (Python standard library) Higher-level threading interface.
* [:earth_americas:eventlet](http://eventlet.net/) - Asynchronous framework with WSGI support.
* [gevent](http://www.gevent.org/) - A coroutine-based Python networking library that uses [:octocat:greenlet](https://github.com/python-greenlet/greenlet) - :star: 638 :fork_and_knife: 118.
* [:octocat:Tomorrow](https://github.com/madisonmay/Tomorrow) - :star: 1135 :fork_and_knife: 67 - Magic decorator syntax for asynchronous code.

## Networking

*Libraries for networking programming.*

* [:earth_americas:asyncio](https://docs.python.org/3/library/asyncio.html) - (Python standard library) Asynchronous I/O, event loop, coroutines and tasks.
* [:earth_americas:Twisted](https://twistedmatrix.com/trac/) - An event-driven networking engine.
* [:octocat:pulsar](https://github.com/quantmind/pulsar) - :star: 1262 :fork_and_knife: 89 - Event-driven concurrent framework for Python.
* [:octocat:diesel](https://github.com/dieseldev/diesel) - :star: 534 :fork_and_knife: 52 - Greenlet-based event I/O Framework for Python.
* [:earth_americas:pyzmq](http://zeromq.github.io/pyzmq/) - A Python wrapper for the ZeroMQ message library.
* [:octocat:txZMQ](https://github.com/smira/txZMQ) - :star: 120 :fork_and_knife: 40 - Twisted based wrapper for the ZeroMQ message library.

## WebSocket

*Libraries for working with WebSocket.*

* [AutobahnPython](https://github.com/crossbario/autobahn-python) - WebSocket & WAMP for Python on Twisted and [:earth_americas:asyncio](https://docs.python.org/3/library/asyncio.html).
* [:octocat:Crossbar](https://github.com/crossbario/crossbar/) - :star: 947 :fork_and_knife: 127 - Open-source Unified Application Router (Websocket & WAMP for Python on Autobahn).
* [:octocat:django-socketio](https://github.com/stephenmcd/django-socketio) - :star: 895 :fork_and_knife: 180 - WebSockets for Django.
* [:octocat:WebSocket-for-Python](https://github.com/Lawouach/WebSocket-for-Python) - :star: 681 :fork_and_knife: 167 - WebSocket client and server library for Python 2 and 3 as well as PyPy.

## WSGI Servers

*WSGI-compatible web servers.*

* [:earth_americas:gunicorn](https://pypi.python.org/pypi/gunicorn) - Pre-forked, partly written in C.
* [:earth_americas:uwsgi](https://uwsgi-docs.readthedocs.io/) - A project aims at developing a full stack for building hosting services, written in C.
* [:earth_americas:bjoern](https://pypi.python.org/pypi/bjoern) - Asynchronous, very fast and written in C.
* [:earth_americas:fapws3](http://www.fapws.org/) - Asynchronous (network side only), written in C.
* [:earth_americas:meinheld](https://pypi.python.org/pypi/meinheld) - Asynchronous, partly written in C.
* [:octocat:netius](https://github.com/hivesolutions/netius) - :star: 40 :fork_and_knife: 2 - Asynchronous, very fast.
* [:earth_americas:paste](http://pythonpaste.org/) - Multi-threaded, stable, tried and tested.
* [:earth_americas:rocket](https://pypi.python.org/pypi/rocket) - Multi-threaded.
* [:earth_americas:waitress](https://waitress.readthedocs.io/) - Multi-threaded, poweres Pyramid.
* [:earth_americas:Werkzeug](http://werkzeug.pocoo.org/) - A WSGI utility library for Python that powers Flask and can easily be embedded into your own projects.

## RPC Servers

*RPC-compatible servers.*

* [:octocat:SimpleJSONRPCServer](https://github.com/joshmarshall/jsonrpclib/) - :star: 266 :fork_and_knife: 109 - This library is an implementation of the JSON-RPC specification.
* [:earth_americas:SimpleXMLRPCServer](https://docs.python.org/2/library/simplexmlrpcserver.html) - (Python standard library) Simple XML-RPC server implementation, single-threaded.
* [zeroRPC](https://github.com/0rpc/zerorpc-python) - zerorpc is a flexible RPC implementation based on [ZeroMQ](http://zeromq.org/) and [:earth_americas:MessagePack](http://msgpack.org/).

## Cryptography

* [:earth_americas:cryptography](https://cryptography.io/en/latest/) - A package designed to expose cryptographic primitives and recipes to Python developers.
* [hashids](https://github.com/davidaurelio/hashids-python) - Implementation of [:earth_americas:hashids](http://hashids.org) in Python.
* [:earth_americas:Paramiko](http://www.paramiko.org/) - A Python (2.6+, 3.3+) implementation of the SSHv2 protocol, providing both client and server functionality.
* [:earth_americas:Passlib](https://pythonhosted.org/passlib/) - Secure password storage/hashing library, very high level.
* [:earth_americas:PyCrypto](https://www.dlitz.net/software/pycrypto/) - The Python Cryptography Toolkit.
* [:octocat:PyNacl](https://github.com/pyca/pynacl) - :star: 282 :fork_and_knife: 58 - Python binding to the Networking and Cryptography (NaCl) library.

## GUI

*Libraries for working with graphical user interface applications.*

* [curses](https://docs.python.org/2/library/curses.html#module-curses) - Built-in wrapper for [:earth_americas:ncurses](http://www.gnu.org/software/ncurses/) used to create terminal GUI applications.
* [:octocat:enaml](https://github.com/nucleic/enaml) - :star: 456 :fork_and_knife: 60 - Creating beautiful user-interfaces with Declaratic Syntax like QML.
* [:earth_americas:kivy](https://kivy.org/) - A library for creating NUI applications, running on Windows, Linux, Mac OS X, Android and iOS.
* [:earth_americas:pyglet](https://bitbucket.org/pyglet/pyglet/wiki/Home) - A cross-platform windowing and multimedia library for Python.
* [PyQt](https://riverbankcomputing.com/software/pyqt/intro) - Python bindings for the [:earth_americas:Qt](http://www.qt.io/) cross-platform application and UI framework, with support for both Qt v4 and Qt v5 frameworks.
* [PySide](https://wiki.qt.io/PySide) - Python bindings for the [:earth_americas:Qt](http://www.qt.io/) cross-platform application and UI framework, supporting the Qt v4 framework.
* [:earth_americas:Tkinter](https://wiki.python.org/moin/TkInter) - Tkinter is Python's de-facto standard GUI package.
* [:octocat:Toga](https://github.com/pybee/toga) - :star: 781 :fork_and_knife: 59 - A Python native, OS native GUI toolkit.
* [:earth_americas:urwid](http://urwid.org/) - A library for creating terminal GUI applications with strong support for widgets, events, rich colors, etc.
* [:earth_americas:wxPython](http://wxpython.org/) - A blending of the wxWidgets C++ class library with the Python.
* [:earth_americas:PyGObject](https://wiki.gnome.org/Projects/PyGObject) - Python Bindings for GLib/GObject/GIO/GTK+ (GTK+3)
* [:octocat:Flexx](https://github.com/zoofIO/flexx) - :star: 949 :fork_and_knife: 90 - Flexx is a pure Python toolkit for creating GUI's, that uses web technology for its rendering.

## Game Development

*Awesome game development libraries.*

* [:earth_americas:Cocos2d](http://cocos2d.org/) - cocos2d is a framework for building 2D games, demos, and other graphical/interactive applications. It is based on pyglet.
* [:earth_americas:Panda3D](https://www.panda3d.org/) - 3D game engine developed by Disney and maintained by Carnegie Mellon's Entertainment Technology Center. Written in C++, completely wrapped in Python.
* [:earth_americas:Pygame](http://www.pygame.org/news.html) - Pygame is a set of Python modules designed for writing games.
* [:earth_americas:PyOgre](http://www.ogre3d.org/tikiwiki/PyOgre) - Python bindings for the Ogre 3D render engine, can be used for games, simulations, anything 3D.
* [:earth_americas:PyOpenGL](http://pyopengl.sourceforge.net/) - Python ctypes bindings for OpenGL and it's related APIs.
* [:earth_americas:PySDL2](http://pysdl2.readthedocs.io/) - A ctypes based wrapper for the SDL2 library.
* [:earth_americas:RenPy](https://www.renpy.org/) - A Visual Novel engine.

## Logging

*Libraries for generating and working with logs.*

* [:earth_americas:logging](https://docs.python.org/2/library/logging.html) - (Python standard library) Logging facility for Python.
* [:earth_americas:logbook](http://pythonhosted.org/Logbook/) - Logging replacement for Python.
* [:octocat:Eliot](https://github.com/ClusterHQ/eliot) - :star: 136 :fork_and_knife: 14 - Logging for complex & distributed systems.
* [:octocat:Raven](https://github.com/getsentry/raven-python) - :star: 960 :fork_and_knife: 596 - The Python client for Sentry.
* [:earth_americas:Sentry](https://pypi.python.org/pypi/sentry) - A realtime logging and aggregation server.

## Testing

*Libraries for testing codebases and generating test data.*

* Testing Frameworks
    * [:earth_americas:unittest](https://docs.python.org/2/library/unittest.html) - (Python standard library) Unit testing framework.
    * [:octocat:nose](https://github.com/nose-devs/nose) - :star: 957 :fork_and_knife: 293 - A nicer `unittest` for Python.
    * [:earth_americas:pytest](http://pytest.org/latest/) - A mature full-featured Python testing tool.
    * [:octocat:hypothesis](https://github.com/HypothesisWorks/hypothesis-python) - :star: 1307 :fork_and_knife: 125 - Hypothesis is an advanced Quickcheck style property based testing library.
    * [:earth_americas:mamba](http://nestorsalceda.github.io/mamba/) - The definitive testing tool for Python. Born under the banner of BDD.
    * [:octocat:Robot Framework](https://github.com/robotframework/robotframework) - :star: 964 :fork_and_knife: 365 - A generic test automation framework.
* Test Runners
    * [:earth_americas:tox](https://tox.readthedocs.io/) - Auto builds and tests distributions in multiple Python versions
    * [:octocat:green](https://github.com/CleanCut/green) - :star: 352 :fork_and_knife: 27 - A clean, colorful test runner.
* GUI / Web Testing
    * [Selenium](https://pypi.python.org/pypi/selenium) - Python bindings for [:earth_americas:Selenium](http://www.seleniumhq.org/) WebDriver.
    * [:octocat:locust](https://github.com/locustio/locust) - :star: 3667 :fork_and_knife: 527 - Scalable user load testing tool written in Python.
    * [:octocat:sixpack](https://github.com/seatgeek/sixpack) - :star: 1083 :fork_and_knife: 108 - A language-agnostic A/B Testing framework.
    * [:octocat:splinter](https://github.com/cobrateam/splinter) - :star: 1128 :fork_and_knife: 269 - Open source tool for testing web applications.
    * [:octocat:PyAutoGUI](https://github.com/asweigart/pyautogui) - :star: 497 :fork_and_knife: 73 - PyAutoGUI is a cross-platform GUI automation Python module for human beings.
* Mock
    * [:earth_americas:mock](https://docs.python.org/3/library/unittest.mock.html) - (Python standard library) A mocking and patching library.
    * [:earth_americas:doublex](https://pypi.python.org/pypi/doublex) - Powerful test doubles framework for Python.
    * [:octocat:freezegun](https://github.com/spulec/freezegun) - :star: 749 :fork_and_knife: 82 - Travel through time by mocking the datetime module.
    * [:octocat:httmock](https://github.com/patrys/httmock) - :star: 249 :fork_and_knife: 25 - A mocking library for requests for Python 2.6+ and 3.2+.
    * [:earth_americas:httpretty](http://falcao.it/HTTPretty/) - HTTP request mock tool for Python.
    * [:octocat:responses](https://github.com/getsentry/responses) - :star: 1240 :fork_and_knife: 112 - A utility library for mocking out the requests Python library.
    * [:octocat:VCR.py](https://github.com/kevin1024/vcrpy) - :star: 692 :fork_and_knife: 101 - Record and replay HTTP interactions on your tests.
* Object Factories
    * [:octocat:factory_boy](https://github.com/rbarrois/factory_boy) - :star: 919 :fork_and_knife: 124 - A test fixtures replacement for Python.
    * [:octocat:mixer](https://github.com/klen/mixer) - :star: 310 :fork_and_knife: 33 - Another fixtures replacement. Supported Django, Flask, SQLAlchemy, Peewee and etc.
    * [:octocat:model_mommy](https://github.com/vandersonmota/model_mommy) - :star: 576 :fork_and_knife: 132 - Creating random fixtures for testing in Django.
* Code Coverage
    * [:earth_americas:coverage](https://pypi.python.org/pypi/coverage) - Code coverage measurement.
* Fake Data
    * [:earth_americas:faker](http://www.joke2k.net/faker/) - A Python package that generates fake data.
    * [:octocat:fake2db](https://github.com/emirozer/fake2db) - :star: 1656 :fork_and_knife: 80 - Fake database generator.
    * [:earth_americas:radar](https://pypi.python.org/pypi/radar) - Generate random datetime / time.
* Error Handler
    * [:octocat:FuckIt.py](https://github.com/ajalt/fuckitpy) - :star: 2072 :fork_and_knife: 87 - FuckIt.py uses state-of-the-art technology to make sure your Python code runs whether it has any right to or not.


## Code Analysis and Linter

*Libraries and tools for analysing, parsing and manipulation codebases.*

* Code Analysis
    * [:octocat:code2flow](https://github.com/scottrogowski/code2flow) - :star: 248 :fork_and_knife: 31 - Turn your Python and JavaScript code into DOT flowcharts.
    * [:octocat:pycallgraph](https://github.com/gak/pycallgraph) - :star: 635 :fork_and_knife: 102 - A library that visualises the flow (call graph) of your Python application.
    * [:octocat:pysonar2](https://github.com/yinwang0/pysonar2) - :star: 2129 :fork_and_knife: 565 - A type inferencer and indexer for Python.
    * [:earth_americas:coala](http://coala-analyzer.org/) - Language independent and easily extendable code analysis application.
* Linter
    * [:earth_americas:Flake8](https://pypi.python.org/pypi/flake8) - The modular source code checker: pep8, pyflakes and co.
    * [:earth_americas:Pylint](https://www.pylint.org/) - A Fully customizable source code analyzer.
    * [:octocat:pylama](https://github.com/klen/pylama) - :star: 185 :fork_and_knife: 29 - Code audit tool for Python and JavaScript.

## Debugging Tools

*Libraries for debugging code.*

* Debugger
    * [ipdb](https://pypi.python.org/pypi/ipdb) - IPython-enabled [:earth_americas:pdb](https://docs.python.org/2/library/pdb.html).
    * [:earth_americas:pudb](https://pypi.python.org/pypi/pudb) – A full-screen, console-based Python debugger.
    * [:octocat:pyringe](https://github.com/google/pyringe) - :star: 1357 :fork_and_knife: 48 - Debugger capable of attaching to and injecting code into Python processes.
    * [:octocat:wdb](https://github.com/Kozea/wdb) - :star: 890 :fork_and_knife: 49 - An improbable web debugger through WebSockets.
    * [:earth_americas:winpdb](http://winpdb.org/) - A Python Debugger with GUI, capable of remote debugging based on `rpdb2`.
    * [:octocat:django-debug-toolbar](https://github.com/django-debug-toolbar/django-debug-toolbar) - :star: 3627 :fork_and_knife: 677 - Display various debug information for Django.
    * [:octocat:django-devserver](https://github.com/dcramer/django-devserver) - :star: 1144 :fork_and_knife: 145 - A drop-in replacement for Django's runserver.
    * [:octocat:flask-debugtoolbar](https://github.com/mgood/flask-debugtoolbar) - :star: 464 :fork_and_knife: 73 - A port of the django-debug-toolbar to flask.
* Profiler
    * [:octocat:line_profiler](https://github.com/rkern/line_profiler) - :star: 835 :fork_and_knife: 58 - Line-by-line profiling.
    * [:octocat:memory_profiler](https://github.com/fabianp/memory_profiler) - :star: 774 :fork_and_knife: 102 - Monitor Memory usage of Python code.
    * [:octocat:profiling](https://github.com/what-studio/profiling) - :star: 2402 :fork_and_knife: 84 - An interactive Python profiler.
* Others
    * [:octocat:pyelftools](https://github.com/eliben/pyelftools) - :star: 325 :fork_and_knife: 116 - Parsing and analyzing ELF files and DWARF debugging information.
    * [python-statsd](https://github.com/WoLpH/python-statsd) - Python Client for the [:octocat:statsd](https://github.com/etsy/statsd/) - :star: 9887 :fork_and_knife: 1357 server.

## Science and Data Analysis

*Libraries for scientific computing and data analyzing.*

* [:earth_americas:astropy](http://www.astropy.org/) - A community Python library for Astronomy.
* [:octocat:bcbio-nextgen](https://github.com/chapmanb/bcbio-nextgen) - :star: 310 :fork_and_knife: 165 - A toolkit providing best-practice pipelines for fully automated high throughput sequencing analysis.
* [:octocat:bccb](https://github.com/chapmanb/bcbb) - :star: 306 :fork_and_knife: 152 - Collection of useful code related to biological analysis.
* [:earth_americas:Biopython](http://biopython.org/wiki/Main_Page) - Biopython is a set of freely available tools for biological computation.
* [:octocat:blaze](https://github.com/blaze/blaze) - :star: 1492 :fork_and_knife: 220 - NumPy and Pandas interface to Big Data.
* [:earth_americas:cclib](http://cclib.github.io/) - A library for parsing and interpreting the results of computational chemistry packages.
* [:earth_americas:NetworkX](https://networkx.github.io/) - A high-productivity software for complex networks.
* [:earth_americas:Neupy](http://neupy.com/pages/home.html) - Running and testing different Artificial Neural Networks algorithms.
* [:earth_americas:NIPY](http://nipy.org) - A collection of neuroimaging toolkits.
* [:earth_americas:Numba](http://numba.pydata.org/) - Python JIT (just in time) complier to LLVM aimed at scientific Python by the developers of Cython and NumPy.
* [:earth_americas:NumPy](http://www.numpy.org/) - A fundamental package for scientific computing with Python.
* [:earth_americas:Open Babel](http://openbabel.org/wiki/Main_Page) - A chemical toolbox designed to speak the many languages of chemical data.
* [:octocat:Open Mining](https://github.com/mining/mining) - :star: 581 :fork_and_knife: 92 - Business Intelligence (BI) in Python (Pandas web interface)
* [:earth_americas:orange](http://orange.biolab.si/) - Data mining, data visualization, analysis and machine learning through visual programming or Python scripting.
* [:earth_americas:Pandas](http://pandas.pydata.org/) - A library providing high-performance, easy-to-use data structures and data analysis tools.
* [:earth_americas:PyDy](http://www.pydy.org/) - Short for Python Dynamics, used to assist with workflow in the modeling of dynamic motion based around NumPy, SciPy, IPython, and matplotlib.
* [:octocat:PyMC](https://github.com/pymc-devs/pymc3) - :star: 1516 :fork_and_knife: 336 - Markov Chain Monte Carlo sampling toolkit.
* [:earth_americas:RDKit](http://www.rdkit.org/) - Cheminformatics and Machine Learning Software.
* [:earth_americas:SciPy](http://www.scipy.org/) - A Python-based ecosystem of open-source software for mathematics, science, and engineering.
* [:octocat:statsmodels](https://github.com/statsmodels/statsmodels) - :star: 1484 :fork_and_knife: 737 - Statistical modeling and econometrics in Python.
* [:octocat:SymPy](https://github.com/sympy/sympy) - :star: 2918 :fork_and_knife: 1478 - A Python library for symbolic mathematics.
* [:octocat:zipline](https://github.com/quantopian/zipline) - :star: 3313 :fork_and_knife: 1026 - A Pythonic algorithmic trading library.

## Data Visualization

*Libraries for visualizing data. See: [:octocat:awesome-javascript](https://github.com/sorrycc/awesome-javascript#data-visualization) - :star: 6242 :fork_and_knife: 883.*

* [:earth_americas:matplotlib](http://matplotlib.org/) - A Python 2D plotting library.
* [:octocat:bokeh](https://github.com/bokeh/bokeh) - :star: 4291 :fork_and_knife: 915 - Interactive Web Plotting for Python.
* [:octocat:ggplot](https://github.com/yhat/ggplot) - :star: 2552 :fork_and_knife: 336 - Same API as ggplot2 for R.
* [:earth_americas:plotly](https://plot.ly/python/) - Collaborative web plotting for Python and matplotlib.
* [:earth_americas:pygal](http://www.pygal.org/en/latest/) - A Python SVG Charts Creator.
* [pygraphviz](https://pypi.python.org/pypi/pygraphviz) - Python interface to [:earth_americas:Graphviz](http://www.graphviz.org/).
* [:earth_americas:PyQtGraph](http://www.pyqtgraph.org/) - Interactive and realtime 2D/3D/Image plotting and science/engineering widgets.
* [:earth_americas:SnakeViz](http://jiffyclub.github.io/snakeviz/) - A browser based graphical viewer for the output of Python's cProfile module.
* [:octocat:vincent](https://github.com/wrobstory/vincent) - :star: 1882 :fork_and_knife: 198 - A Python to Vega translator.
* [:earth_americas:VisPy](http://vispy.org/) - High-performance scientific visualization based on OpenGL.

## Computer Vision

*Libraries for computer vision.*

* [:earth_americas:OpenCV](http://opencv.org/) - Open Source Computer Vision Library.
* [:earth_americas:SimpleCV](http://simplecv.org/) - An open source framework for building computer vision applications.

## Machine Learning

*Libraries for Machine Learning. See: [:octocat:awesome-machine-learning](https://github.com/josephmisiti/awesome-machine-learning#python) - :star: 13614 :fork_and_knife: 3024.*

* [:octocat:Crab](https://github.com/muricoca/crab) - :star: 694 :fork_and_knife: 260 - A ﬂexible, fast recommender engine.
* [:octocat:gensim](https://github.com/piskvorky/gensim) - :star: 2630 :fork_and_knife: 955 - Topic Modelling for Humans.
* [:octocat:hebel](https://github.com/hannes-brt/hebel) - :star: 1144 :fork_and_knife: 106 - GPU-Accelerated Deep Learning Library in Python.
* [:octocat:NuPIC](https://github.com/numenta/nupic) - :star: 4210 :fork_and_knife: 1183 - Numenta Platform for Intelligent Computing.
* [:octocat:pattern](https://github.com/clips/pattern) - :star: 4530 :fork_and_knife: 793 - Web mining module for Python.
* [:octocat:PyBrain](https://github.com/pybrain/pybrain) - :star: 1838 :fork_and_knife: 571 - Another Python Machine Learning Library.
* [Pylearn2](https://github.com/lisa-lab/pylearn2) - A Machine Learning library based on [:octocat:Theano](https://github.com/Theano/Theano) - :star: 3948 :fork_and_knife: 1428.
* [:octocat:python-recsys](https://github.com/ocelma/python-recsys) - :star: 585 :fork_and_knife: 256 - A Python library for implementing a Recommender System.
* [:earth_americas:scikit-learn](http://scikit-learn.org/) - A Python module for machine learning built on top of SciPy.
* [:octocat:pydeep](https://github.com/andersbll/deeppy) - :star: 891 :fork_and_knife: 152 - Deep learning in python
* [vowpal_porpoise](https://github.com/josephreisinger/vowpal_porpoise) - A lightweight Python wrapper for [:octocat:Vowpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit/) - :star: 3496 :fork_and_knife: 974.
* [skflow](https://github.com/tensorflow/skflow) - A simplified interface for [:octocat:TensorFlow](https://github.com/tensorflow/tensorflow) - :star: 26408 :fork_and_knife: 10327 (mimicking scikit-learn).

## MapReduce

*Frameworks and libraries for MapReduce.*

* [:octocat:dpark](https://github.com/douban/dpark) - :star: 1783 :fork_and_knife: 418 - Python clone of Spark, a MapReduce alike framework in Python.
* [:octocat:dumbo](https://github.com/klbostee/dumbo) - :star: 969 :fork_and_knife: 158 - Python module that allows one to easily write and run Hadoop programs.
* [:octocat:luigi](https://github.com/spotify/luigi) - :star: 4765 :fork_and_knife: 915 - A module that helps you build complex pipelines of batch jobs.
* [:octocat:mrjob](https://github.com/Yelp/mrjob) - :star: 1828 :fork_and_knife: 459 - Run MapReduce jobs on Hadoop or Amazon Web Services.
* [:earth_americas:PySpark](http://spark.apache.org/docs/latest/programming-guide.html) - The Spark Python API.
* [streamparse](https://github.com/Parsely/streamparse) - Run Python code against real-time streams of data. Integrates with [:earth_americas:Apache Storm](http://storm.apache.org/).

## Functional Programming

*Functional Programming with Python.*

* [:octocat:CyToolz](https://github.com/pytoolz/cytoolz/) - :star: 266 :fork_and_knife: 22 - Cython implementation of Toolz: High performance functional utilities.
* [:octocat:fn.py](https://github.com/kachayev/fn.py) - :star: 1949 :fork_and_knife: 123 - Functional programming in Python: implementation of missing features to enjoy FP.
* [:octocat:funcy](https://github.com/Suor/funcy) - :star: 1293 :fork_and_knife: 64 - A fancy and practical functional tools.
* [:octocat:Toolz](https://github.com/pytoolz/toolz) - :star: 1122 :fork_and_knife: 89 - A collection of functional utilities for iterators, functions, and dictionaries.

## Third-party APIs

*Libraries for accessing third party services APIs. See: [:octocat:List of Python API Wrappers and Libraries](https://github.com/realpython/list-of-python-api-wrappers) - :star: 524 :fork_and_knife: 69.*

* [:earth_americas:apache-libcloud](https://libcloud.apache.org/) - One Python library for all clouds.
* [:octocat:boto](https://github.com/boto/boto) - :star: 5500 :fork_and_knife: 2013 - Python interface to Amazon Web Services.
* [:octocat:django-wordpress](https://github.com/sunlightlabs/django-wordpress/) - :star: 212 :fork_and_knife: 49 - WordPress models and views for Django.
* [:octocat:facebook-sdk](https://github.com/mobolic/facebook-sdk) - :star: 1686 :fork_and_knife: 636 - Facebook Platform Python SDK.
* [:octocat:facepy](https://github.com/jgorset/facepy) - :star: 480 :fork_and_knife: 141 - Facepy makes it really easy to interact with Facebook's Graph API
* [:octocat:gmail](https://github.com/charlierguo/gmail) - :star: 1269 :fork_and_knife: 220 - A Pythonic interface for Gmail.
* [:octocat:google-api-python-client](https://github.com/google/google-api-python-client) - :star: 987 :fork_and_knife: 426 - Google APIs Client Library for Python.
* [:octocat:gspread](https://github.com/burnash/gspread) - :star: 1721 :fork_and_knife: 324 - Google Spreadsheets Python API.
* [:octocat:twython](https://github.com/ryanmcgrath/twython) - :star: 1180 :fork_and_knife: 307 - A Python wrapper for the Twitter API.

## DevOps Tools

*Software and libraries for DevOps.*

* [:octocat:Ansible](https://github.com/ansible/ansible) - :star: 17332 :fork_and_knife: 5234 - A radically simple IT automation platform.
* [:octocat:SaltStack](https://github.com/saltstack/salt) - :star: 6618 :fork_and_knife: 2951 - Infrastructure automation and management system.
* [:earth_americas:OpenStack](http://www.openstack.org/) - Open source software for building private and public clouds.
* [Docker Compose](https://docs.docker.com/compose/) - Fast, isolated development environments using [:earth_americas:Docker](https://www.docker.com/).
* [:earth_americas:Cloud-Init](http://cloudinit.readthedocs.io/) - A multi-distribution package that handles early initialization of a cloud instance.
* [:octocat:cuisine](https://github.com/sebastien/cuisine) - :star: 1177 :fork_and_knife: 148 - Chef-like functionality for Fabric.
* [:earth_americas:Fabric](http://www.fabfile.org/) - A simple, Pythonic tool for remote execution and deployment.
* [:octocat:Fabtools](https://github.com/ronnix/fabtools) - :star: 1010 :fork_and_knife: 203 - Tools for writing awesome Fabric files.
* [honcho](https://github.com/nickstenning/honcho) - A Python clone of [:octocat:Foreman](https://github.com/ddollar/foreman) - :star: 3876 :fork_and_knife: 474, for managing Procfile-based applications.
* [:octocat:pexpect](https://github.com/pexpect/pexpect) - :star: 600 :fork_and_knife: 161 - Controlling interactive programs in a pseudo-terminal like GNU expect.
* [:octocat:psutil](https://github.com/giampaolo/psutil) - :star: 1644 :fork_and_knife: 269 - A cross-platform process and system utilities module.
* [:octocat:supervisor](https://github.com/Supervisor/supervisor) - :star: 2552 :fork_and_knife: 527 - Supervisor process control system for UNIX.

## ChatOps Tools

*Libraries for chatbot development.*

* [:earth_americas:Errbot](http://errbot.io/) - The easiest and most popular chatbot to implement ChatOps.

## Job Scheduler

*Libraries for scheduling jobs.*

* [:earth_americas:APScheduler](http://apscheduler.readthedocs.io/) - A light but powerful in-process task scheduler that lets you schedule functions.
* [:octocat:django-schedule](https://github.com/thauber/django-schedule) - :star: 634 :fork_and_knife: 260 - A calendaring app for Django.
* [:earth_americas:doit](http://pydoit.org/) - A task runner and build tool.
* [:octocat:gunnery](https://github.com/gunnery/gunnery) - :star: 595 :fork_and_knife: 54 - Multipurpose task execution tool for distributed systems with web-based interface.
* [:earth_americas:Joblib](http://pythonhosted.org/joblib/index.html) - A set of tools to provide lightweight pipelining in Python.
* [:octocat:Plan](https://github.com/fengsp/plan) - :star: 893 :fork_and_knife: 63 - Writing crontab file in Python like a charm.
* [:octocat:schedule](https://github.com/dbader/schedule) - :star: 2225 :fork_and_knife: 222 - Python job scheduling for humans.
* [:octocat:Spiff](https://github.com/knipknap/SpiffWorkflow) - :star: 340 :fork_and_knife: 83 - A powerful workflow engine implemented in pure Python.
* [:earth_americas:TaskFlow](http://docs.openstack.org/developer/taskflow/) - A Python library that helps to make task execution easy, consistent and reliable.

## Foreign Function Interface

*Libraries for providing foreign function interface.*

* [:earth_americas:cffi](https://pypi.python.org/pypi/cffi) - Foreign Function Interface for Python calling C code.
* [:earth_americas:ctypes](https://docs.python.org/2/library/ctypes.html) - (Python standard library) Foreign Function Interface for Python calling C code.
* [:earth_americas:PyCUDA](https://mathema.tician.de/software/pycuda/) - A Python wrapper for Nvidia's CUDA API.
* [:earth_americas:SWIG](http://www.swig.org/Doc1.3/Python.html) - Simplified Wrapper and Interface Generator.

## High Performance

*Libraries for making Python faster.*

* [:earth_americas:Cython](http://cython.org/) - Optimizing Static Compiler for Python. Uses type mixins to compile Python into C or C++ modules resulting in large performance gains.
* [:octocat:PeachPy](https://github.com/Maratyszcza/PeachPy) - :star: 733 :fork_and_knife: 33 - x86-64 assembler embedded in Python. Can be used as inline assembler for Python or as a stand-alone assembler for Windows, Linux, OS X, Native Client and Go.
* [:earth_americas:PyPy](http://pypy.org/) - An implementation of Python in Python. The interpreter uses black magic to make Python very fast without having to add in additional type information.
* [:octocat:Pyston](https://github.com/dropbox/pyston) - :star: 3764 :fork_and_knife: 260 - A Python implementation built using LLVM and modern JIT techniques with the goal of achieving good performance.
* [:earth_americas:Stackless Python](https://bitbucket.org/stackless-dev/stackless/overview) - An enhanced version of the Python.

## Microsoft Windows

*Python programming on Microsoft Windows.*

* [:earth_americas:Python(x,y)](http://python-xy.github.io/) - Scientific-applications-oriented Python Distribution based on Qt and Spyder.
* [:earth_americas:pythonlibs](http://www.lfd.uci.edu/~gohlke/pythonlibs/) - Unofficial Windows binaries for Python extension packages.
* [:octocat:PythonNet](https://github.com/pythonnet/pythonnet) - :star: 195 :fork_and_knife: 72 - Python Integration with the .NET Common Language Runtime (CLR).
* [:earth_americas:PyWin32](https://sourceforge.net/projects/pywin32/) - Python Extensions for Windows.
* [:earth_americas:WinPython](https://winpython.github.io/) - Portable development environment for Windows 7/8.

## Network Virtualization and SDN

*Tools and libraries for Virtual Networking and SDN (Software Defined Networking).*

* [:earth_americas:Mininet](http://mininet.org/) - A popular network emulator and API written in Python.
* [:octocat:POX](https://github.com/noxrepo/pox) - :star: 311 :fork_and_knife: 302 - An open source development platform for Python-based Software Defined Networking (SDN) control applications, such as OpenFlow SDN controllers.
* [:earth_americas:Pyretic](http://frenetic-lang.org/pyretic/) - A member of the Frenetic family of SDN programming languages that provides powerful abstractions over network switches or emulators.
* [:octocat:SDX Platform](https://github.com/sdn-ixp/internet2award) - :star: 9 :fork_and_knife: 4 - SDN based IXP implementation that leverages Mininet, POX and Pyretic.

## Hardware

*Libraries for programming with hardware.*

* [ino](http://inotool.org/) - Command line toolkit for working with [:earth_americas:Arduino](https://www.arduino.cc/).
* [:earth_americas:Pyro](http://pyrorobotics.com/) - Python Robotics.
* [:octocat:PyUserInput](https://github.com/SavinaRoja/PyUserInput) - :star: 438 :fork_and_knife: 103 - A module for cross-platform control of the mouse and keyboard.
* [:octocat:scapy](https://github.com/secdev/scapy) - :star: 461 :fork_and_knife: 124 - A brilliant packet manipulation library.
* [:octocat:wifi](https://github.com/rockymeza/wifi) - :star: 130 :fork_and_knife: 67 - A Python library and command line tool for working with WiFi on Linux.
* [:earth_americas:Pingo](http://www.pingo.io/) - Pingo provides a uniform API to program devices like the Raspberry Pi, pcDuino, Intel Galileo, etc.

## Compatibility

*Libraries for migrating from Python 2 to 3.*

* [:earth_americas:Python-Future](http://python-future.org/index.html) - The missing compatibility layer between Python 2 and Python 3.
* [:octocat:Python-Modernize](https://github.com/mitsuhiko/python-modernize) - :star: 411 :fork_and_knife: 30 - Modernizes Python code for eventual Python 3 migration.
* [:earth_americas:Six](https://pypi.python.org/pypi/six) - Python 2 and 3 compatibility utilities.

## Miscellaneous

*Useful libraries or tools that don't fit in the categories above.*

* [:octocat:blinker](https://github.com/jek/blinker) - :star: 343 :fork_and_knife: 43 - A fast Python in-process signal/event dispatching system.
* [:octocat:itsdangerous](https://github.com/pallets/itsdangerous) - :star: 912 :fork_and_knife: 80 - Various helpers to pass trusted data to untrusted environments.
* [:octocat:pluginbase](https://github.com/mitsuhiko/pluginbase) - :star: 381 :fork_and_knife: 28 - A simple but flexible plugin system for Python.
* [:octocat:Pychievements](https://github.com/PacketPerception/pychievements) - :star: 73 :fork_and_knife: 4 - A framework for creating and tracking achievements.
* [:earth_americas:Tryton](http://www.tryton.org/) - A general purpose business framework.

## Algorithms and Design Patterns

*Python implementation of algorithms and design patterns.*

* [:octocat:algorithms](https://github.com/nryoung/algorithms) - :star: 1502 :fork_and_knife: 393 - A module of algorithms for Python.
* [:octocat:python-patterns](https://github.com/faif/python-patterns) - :star: 8611 :fork_and_knife: 2009 - A collection of design patterns in Python.
* [:earth_americas:sortedcontainers](http://www.grantjenks.com/docs/sortedcontainers/) - Fast, pure-Python implementation of SortedList, SortedDict, and SortedSet types.

## Editor Plugins

*Plugins for editors and IDEs.*

* Emacs
    * [:octocat:Elpy](https://github.com/jorgenschaefer/elpy) - :star: 739 :fork_and_knife: 107 - Emacs Python Development Environment.
* Sublime Text
    * [:octocat:SublimeJEDI](https://github.com/srusskih/SublimeJEDI) - :star: 640 :fork_and_knife: 65 - A Sublime Text plugin to the awesome auto-complete library Jedi.
    * [:octocat:Anaconda](https://github.com/DamnWidget/anaconda) - :star: 1087 :fork_and_knife: 114 - Anaconda turns your Sublime Text 3 in a full featured Python development IDE.
* Vim
    * [YouCompleteMe](https://github.com/Valloric/YouCompleteMe) - Includes [:octocat:Jedi](https://github.com/davidhalter/jedi) - :star: 2121 :fork_and_knife: 177-based completion engine for Python.
    * [:octocat:Jedi-vim](https://github.com/davidhalter/jedi-vim) - :star: 2370 :fork_and_knife: 213 - Vim bindings for the Jedi auto-completion library for Python.
    * [:octocat:Python-mode](https://github.com/klen/python-mode) - :star: 3034 :fork_and_knife: 628 - An all in one plugin for turning Vim into a Python IDE.
* Visual Studio
    * [:octocat:PTVS](https://github.com/Microsoft/PTVS) - :star: 1106 :fork_and_knife: 286 - Python Tools for Visual Studio.

## IDEs

*Popular Python IDEs.*

* [:earth_americas:PyCharm](https://www.jetbrains.com/pycharm/) - Commercial Python IDE by JetBrains. Has free community edition available.
* [:earth_americas:LiClipse](http://www.liclipse.com/) - Free polyglot IDE based on Eclipse. Uses PyDev for Python support.
* [:octocat:Spyder](https://github.com/spyder-ide/spyder) - :star: 1120 :fork_and_knife: 279 - Open Source Python IDE.

# Services

Online tools and APIs to simplify development.

## Continuous Integration

*See: [:octocat:awesome-CIandCD](https://github.com/ciandcd/awesome-ciandcd#online-build-system) - :star: 187 :fork_and_knife: 26.*

* [Travis CI](https://travis-ci.org) - A popular CI service for your open source and [:earth_americas:private](https://travis-ci.com) projects. (GitHub only)
* [:earth_americas:CircleCI](https://circleci.com/) - A CI service that can run very fast parallel testing. (GitHub only)
* [:earth_americas:Vexor CI](https://vexor.io) - A continuous integration tool for private apps with pay-per-minute billing model.
* [:earth_americas:Wercker](http://wercker.com/) - A Docker-based platform for building and deploying applications and microservices.

## Code Quality

* [:earth_americas:Codecov](https://codecov.io/) - Code coverage dashboard.
* [:earth_americas:Codacy](https://www.codacy.com/) - Automated Code Review to ship better code, faster. Free for Open Source.
* [:earth_americas:Landscape](https://landscape.io/) - Hosted continuous Python code metrics.
* [:earth_americas:QuantifiedCode](https://www.quantifiedcode.com/) - A data-driven, automated, continuous code review tool.

# Resources

Where to discover new Python libraries.

## Websites

* [r/Python](https://www.reddit.com/r/python)
* [CoolGithubProjects](https://www.coolgithubprojects.com/)
* [Django Packages](https://www.djangopackages.com/)
* [Full Stack Python](https://www.fullstackpython.com/)
* [Python 3 Wall of Superpowers](http://python3wos.appspot.com/)
* [Python Hackers](http://pythonhackers.com/open-source/)
* [Python ZEEF](https://python.zeef.com/alan.richmond)
* [Trending Python repositories on GitHub today](https://github.com/trending?l=python)
* [PyPI Ranking](http://pypi-ranking.info/alltime)
* [Awesome Python @LibHunt](http://python.libhunt.com)

## Weekly

* [CodeTengu Weekly](http://weekly.codetengu.com/)
* [Import Python Newsletter](http://importpython.com/newsletter/)
* [Pycoder's Weekly](http://pycoders.com/)
* [Python Weekly](http://www.pythonweekly.com/)

## Twitter

* [@codetengu](https://twitter.com/codetengu)
* [@getpy](https://twitter.com/getpy)
* [@importpython](https://twitter.com/importpython)
* [@planetpython](https://twitter.com/planetpython)
* [@pycoders](https://twitter.com/pycoders)
* [@pypi](https://twitter.com/pypi)
* [@pythontrending](https://twitter.com/pythontrending)
* [@PythonWeekly](https://twitter.com/PythonWeekly)

# Other Awesome Lists

List of lists.

* Python
    * [pycrumbs](https://github.com/kirang89/pycrumbs/blob/master/pycrumbs.md)
    * [python-github-projects](https://github.com/checkcheckzz/python-github-projects)
    * [python_reference](https://github.com/rasbt/python_reference)
    * [pythonidae](https://github.com/svaksha/pythonidae)
* Monty
    * [awesome](https://github.com/sindresorhus/awesome)
    * [lists](https://github.com/jnv/lists)

# Contributing

Your contributions are always welcome! Please take a look at the [:octocat:contribution guidelines](https://github.com/vinta/awesome-python/blob/master/CONTRIBUTING.md) - :star: 21648 :fork_and_knife: 4040 first.

I would keep some pull requests open if I'm not sure whether the libraries are awesome, you could [:octocat:vote for them](https://github.com/vinta/awesome-python/pulls) - :star: 21648 :fork_and_knife: 4040 by adding :+1: to them.
