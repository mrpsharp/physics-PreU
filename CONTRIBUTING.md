# Contributing

You are very welcome to contribute to this fledgling either by writing or by raising an issue if you find something wrong. 

If you are contributing, please note the following:

1. All chapters have their own file with a documentclass of subfiles (see the file 1-mechanics.tex for an example). The subfiles package means that chapters work as both standalone documents and within the main document.
2. The actual points from the specification (including letter label) should be wrapped in the ```\spec{}``` environment. This allows styling in the preamble of main.tex. I am not auto-numbering to ensure that the points relate directly to the Pre-U specification.
