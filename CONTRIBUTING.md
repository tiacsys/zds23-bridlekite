# Contributing

Contributions are welcome, and they are greatly appreciated! Every little
helps, and credit will always be given.

You can contribute in many ways:

## Types of Contributions

### Report Bugs

Report bugs to [our issue page][gh-issues]. If you are reporting a bug, please
include:

- Your operating system name and version.
- Any details about your local setup that might be helpful in troubleshooting.
- Detailed steps to reproduce the bug.

### Fix Bugs

Look through the GitLab issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

### Implement Features

Look through the GitLab issues for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement it.

### Write Documentation

The ZDS slide set material could always use more documentation and content,
whether as part of the official documentation, in [reStructuredText][rst-doc],
or even on the web in blog posts, articles, and such.

Further readings for you as new contributor:

- [reStructuredText User Documentation][rst-doc]
- [reStructuredText Primer by Sphinx][rst-primer]
- [Sphinx User Documentation][sphinx-doc]
- [Sphinx Primer by Li-Pro.Net][sphinx-primer]

### Submit Feedback

The best way to send feedback [our issue page][gh-issues] on GitLab. If you
are proposing a feature:

- Explain in detail how it would work.
- Keep the scope as narrow as possible, to make it easier to implement.
- Remember that this is a volunteer-driven project, and that contributions are
  welcome 😊

## Document Variation Matrix

Sphinx supports the [inclusion of content based on tags]. Based on this basic
feature, the existing documentation can be controlled externally by using our
own predefined tags to affect the appearance and content of the generated
documents.

The specification of tags is done by the mechanics of the existing build
environment and can be controlled by the environment variable `SPHINXTAGS`.
The default setting in the GNU [`Makefile`] or batch file [`make.bat`] is
`-t mpulnx`.

The following tags and their meaning and function are already available:

<!-- https://www.tablesgenerator.com/markdown_tables -->

| Meaning:<br>Tags:  | Branding                                       | Content                                              |
| ------------------ | ---------------------------------------------- | ---------------------------------------------------- |
| `tiac`             | **default:** *TiaC Systems*                    |                                                      |
| `mpul`             | *UL Method Park GmbH*                          |                                                      |
| `nx`               | *Navimatix GmbH*                               |                                                      |
| `mpulnx`           | *UL Method Park GmbH* **and** *Navimatix GmbH* |                                                      |
| `without_rtd`      |                                                | **EXCLUDES** chapter *Read-The-Docs!*                |
| `without_thankyou` |                                                | **EXCLUDES** chapter *Thank you for your attention!* |

> | ⚠ WARNING: Tag combination and implicit rules |
> | --------------------------------------------- |
>
> Not all conceivable tag combinations are supported. If errors occur, then
> these previously "unknown" and so far unsupported combinations must be fixed
> at the document structure level. New tags should be added in the table
> above.
>
> Furthermore, the mechanics of the existing build environment ensure that a
> corresponding tag is created and passed for each Sphinx builder, thus e.g.
> with `make revealjs` one will always be able to work with the tag `revealjs`
> on the level of the document structure **and** the Sphinx `conf.py`.
> However, this implicit rule disallows a direct call to `sphinx-build`.
>
> **One must always work with the `make` or `make.bat` process!**

## System Requirements

The ideal development environment is a Linux based system. A current Ubuntu
LTS, i.e. 22.04 or 20.04, is recommended and should be used. Windows 10 or 11
as well as MacOS are conceivable but are not preferred or recommended. Most
notations are written in such a way that these systems could also be used in
theory.

### System packages for Python 3

The pivot point as "programmed documentation" is a fully functioning Python 3
runtime environment. For later setup of a local Python 3 Virtual Environment
the following system packages are mandatory and must be installed:

```bash
$ sudo apt install --yes $(cat dpkg-tools-reqirements.txt)
$ sudo apt install --yes $(cat dpkg-nodejs-reqirements.txt)
$ sudo apt install --yes $(cat dpkg-python3-reqirements.txt)
```

… or as alternative without an already checked out local repository:

```bash
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/zds-spxrjs-template.git \
             --format=tar main dpkg-tools-reqirements.txt 2>/dev/null | tar xO)
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/zds-spxrjs-template.git \
             --format=tar main dpkg-nodejs-reqirements.txt 2>/dev/null | tar xO)
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/zds-spxrjs-template.git \
             --format=tar main dpkg-python3-reqirements.txt 2>/dev/null | tar xO)
```

### System packages for spell checking

If you consider running Sphinx's spell checking extension, the following
system packages must be installed:

```bash
$ sudo apt install --yes $(cat dpkg-spelling-reqirements.txt)
```

… or as alternative without an already checked out local repository:

```bash
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/zds-spxrjs-template.git \
             --format=tar main dpkg-spelling-reqirements.txt 2>/dev/null | tar xO)
```

### System packages for LaTeX

If you consider creating the PDF manual locally via Sphinx's LaTeX builder,
the following system packages must be installed:

```bash
$ sudo apt install --yes $(cat dpkg-latex-reqirements.txt)
```

… or as alternative without an already checked out local repository:

```bash
$ sudo apt install --yes \
       $(git archive \
             --remote=ssh://git@github.com:tiacsys/zds-spxrjs-template.git \
             --format=tar main dpkg-latex-reqirements.txt 2>/dev/null | tar xO)
```

## Get Started!

Ready to contribute? Here's how to set yourself up for local development.

1. Fork the repo on GitLab.

1. Create and activate a west workspace specific
   [Python 3 virtual environment](https://docs.python.org/3/library/venv.html):

   ```bash
   $ mkdir zds-spxrjs-workspace
   $ cd zds-spxrjs-workspace

   $ python3 -m venv --prompt="$(basename $(pwd))[$(python3 --version)]" \
                     --clear --copies .venv
   $ source .venv/bin/activate

   $ pip3 install --upgrade pip setuptools
   $ pip3 install --upgrade poetry west
   ```

1. Create a west workspace from your fork locally:

   ```bash
   $ west init --manifest-url git@github.com:tiacsys/zds-spxrjs-template.git \
               --manifest-rev main
   $ west update
   ```

1. Install the project dependencies with [Poetry](https://python-poetry.org):

   ```bash
   $ cd zds-spxrjs-template
   $ pip3 install --use-pep517 --isolated --no-cache 'sphinxcontrib-asciinema==0.3.5'
   $ poetry install --no-root
   ```

   **NOTE:** There is an
   [issue](https://github.com/divi255/sphinxcontrib.asciinema/issues/18) on
   package *sphinxcontrib-asciinema*. That have to be installed before all
   other Sphinx extensions of the namespace *sphinxcontrib* will be installed
   by poetry!

1. **OPTIONAL:** Setup a dedicated Node.js version for
   [DeckTape](https://www.npmjs.com/package/decktape) directly into the west
   workspace specific Python 3 virtual environment with
   [NodeEnv](https://pypi.org/project/nodeenv):

   ```bash
   $ nodeenv --node=lts --python-virtualenv --prebuilt \
             --requirements=nodeenv-reqirements.txt
   ```

1. Create a branch for local development:

   ```bash
   $ git checkout -b name-of-your-bugfix-or-feature
   ```

   Now you can make your changes locally.

1. When you're done making changes, check that your changes pass our tests:

   ```bash
   $ ### NOT YET ### poetry run pytest
   $ make spelling
   $ ### NOT YET ### make doctest
   $ ### NOT YET ### make coverage ; cat docs/build/coverage/python.txt
   $ make linkcheck
   ```

1. Linting is done through [pre-commit](https://pre-commit.com). Provided you
   have the tool installed globally, you can run them all as one-off:

   ```bash
   $ pre-commit run -a
   ```

   Or better, install the hooks once and have them run automatically each time
   you commit:

   ```bash
   $ pre-commit install --hook-type pre-commit --hook-type commit-msg
   ```

1. Optional run tests on documentation and build them offline:

   ```bash
   $ make html
   $ python3 -m http.server -d build/html 8000
   ```

1. Optional run tests on the reveal.js slide deck and build them offline:

   ```
   $ make revealjs
   $ python3 -m http.server -d build/revealjs 8001
   ```

   **OPTIONAL:** build high-quality PDF export from the reveal.js slide deck:

   ```
   $ make revealjspdf
   $ xdg-open build/revealjs/slides.pdf
   ```

1. Optional run tests on the LaTeX/PDF manual and build them offline:

   ```
   $ make latexpdf
   $ xdg-open build/latex/zds-spxrjs-template.pdf
   ```

1. Commit your changes and push your branch to GitLab:

   ```bash
   $ git add .
   $ git commit -m "feat(something): your detailed description of your changes"
   $ git push origin name-of-your-bugfix-or-feature
   ```

   Note: the commit message should follow
   [the conventional commits](https://www.conventionalcommits.org). **NOT
   YET** ~~We run
   [`commitlint` on CI](https://github.com/wagoid/commitlint-github-action) to
   validate it, and if you have installed pre-commit hooks at the previous
   step, the message will be checked at commit time.~~ **NOT YET**

1. Submit a merge request through the GitLab website or using the GitLab CLI
   (if you have it installed):

   ```bash
   $ glab mr create --fill
   ```

## Merge Request Guidelines

We like to have the merge request open as soon as possible, that's a great
place to discuss any piece of work, even unfinished. You can use draft merge
request if it's still a work in progress. Here are a few guidelines to follow:

1. Include tests for feature or bug fixes.
1. Update the documentation for significant features.
1. Ensure tests are passing on CI.

## Tips

To run a subset of tests:

```bash
$ ### NOT YET ### make pytest tests
```

## Making a new release

The deployment should be automated and can be triggered from the Semantic
Release workflow in GitLab. The next version will be based on
[the commit logs](https://python-semantic-release.readthedocs.io/en/latest/commit-log-parsing.html#commit-log-parsing).
**NOT YET** ~~This is done by
[python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/index.html)
via a GitLab action.~~ **NOT YET**

[gh-issues]: https://github.com/tiacsys/zds-spxrjs-template/issues
[inclusion of content based on tags]: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#tags
[rst-doc]: https://docutils.sourceforge.io/rst.html
[rst-primer]: https://www.sphinx-doc.org/en/master/usage/restructuredtext
[sphinx-doc]: https://www.sphinx-doc.org/
[sphinx-primer]: https://lpn-doc-sphinx-primer.readthedocs.io/
[`make.bat`]: make.bat
[`makefile`]: Makefile
