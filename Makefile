# Minimal makefile for Sphinx documentation
#
# Copyright (c) 2022-2023 TiaC Systems
# SPDX-License-Identifier: CC-BY-SA-4.0

TOP := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))

### FIXME ###
# avoid ugly issues with online images, warning was:
# WARNING: Could not fetch remote image:
# [time data '...' does not match format '...']
LANG=
export LANG
LC_TIME=
export LC_TIME
### FIXME ###

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXTAGS    ?= -t tiac
SPHINXOPTS    ?= -v -W --keep-going
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

DECKTAPEBUILD ?= $(TOP)$(BUILDDIR)/revealjs/decktape-build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@echo
	@echo "Add-ons:"
	@echo "  revealjs    to make Reveal.js standalone HTML presentation (if enabled)"
	@echo "  revealjspdf to make PDF export from Reveal.js presentation (if enabled)"
	@echo "  spelling    to check spelling in the documentation (if enabled)"

.PHONY: help Makefile

revealjspdf: $(DECKTAPEBUILD) revealjs
	@$<

.PHONY: revealjspdf $(DECKTAPEBUILD)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" -t $@ $(SPHINXTAGS) $(SPHINXOPTS) $(O)
