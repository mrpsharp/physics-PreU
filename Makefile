TAG:=$(shell git describe --tags)
.PHONY: guides clean all release version

guides: version
	latexmk -pdf revision-guide.tex sixth-form.tex

clean:
	latexmk -C

all: version
	latexmk -pdf

release: guides
	gh release create $(TAG) 'sixth-form.pdf#Sixth Form Revision Guide' 'revision-guide.pdf#Pre-U Revision Guide'

version:
	git describe --tags > version.tex
	cat version.tex