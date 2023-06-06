#!/usr/bin/env -vS make -f

# Minimal makefile for ASCIInema recording and convertion to SVG
#

TOP   := $(dir $(realpath $(lastword $(MAKEFILE_LIST))))
PATH  := $(TOP)tools/asciinema-rec_script/bin:$(PATH)
TOUCH := touch -cm
MKDIR := mkdir -pv
CHDIR := cd -P

# You can set these variables from the command line, and also
# from the environment for the first two. Please, respect the
# Node.js options to increase the default V8 heap memory for
# garbage collection (GC) from 4GB to 12GB. For details, see:
#
#   - https://nodejs.org/api/cli.html#useful-v8-options
#   - https://nodejs.org/api/cli.html#node_optionsoptions
#
# That avoids "JavaScript heap out of memory" error conditions.
# If still happen in future, increase again from currently 12GB.
TOSVGRANGE    ?=
TOSVGOPTS     ?= --no-optimize --no-cursor --window
TOSVGTHEME    ?= --term iterm2 --profile $(COLOR)
TOSVG         = NODE_OPTIONS=--max-old-space-size=12288 svg-term

# The Solarized Light colors in iTerm2 format:
COLOR := "$(TOP)tools/colors_solarized/iterm2-colors-solarized/Solarized Light.itermcolors"

# List of ASCIInema recording files that have to generate automatically:
ASCREC_CASTS := $(TOP)source/revealjs/materials/getting-started-in-practice/bridle-workspace.cast

.PHONY: asciicast
asciicast: $(ASCREC_CASTS)

# Run time path for the automated ASCIInema recording. It will lay under
# a standard temporary directory that are preserved between system reboots.
# See FHS 3.0: https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.html
ASCREC_RUNDIR ?= /var/tmp/ascrec

$(ASCREC_RUNDIR):
	@$(MKDIR) "$@"

%.asc: %.env %.tmux
	@$(TOUCH) "$@"

%.cast: %.asc $(ASCREC_RUNDIR)
	@$(CHDIR) "$(ASCREC_RUNDIR)" && \
	 ASCDIR="$(realpath $(<D))" "$(realpath $<)"
# TODO:	With GNU Make 4.2.93 the support of special variable .EXTRA_PREREQS
#	was introduced and can avoid the sully prerequisites for %.cast, see:
#	https://www.gnu.org/software/make/manual/make.html#Special-Variables
# %.cast: .EXTRA_PREREQS = $(ASCREC_RUNDIR)

ASCREC_SVG := $(addsuffix .svg,$(basename $(ASCREC_CASTS)))

.PHONY: asciisvg
asciisvg: $(ASCREC_SVG)

%.svg: %.cast
	@echo -n "SVG $(@F) from $(<F) ... "
	@$(TOSVG) $(TOSVGTHEME) $(TOSVGOPTS) $(TOSVGRANGE) \
	 --in "$(realpath $<)" --out "$(realpath $(@D))/$(@F)"
	@echo "DONE"
