MAINFILE = main.tex

$(MAINFILE): FORCE

.PHONY: FORCE

FORCE:
	latexmk -pdf $(MAINFILE)
    
.PHONY: clean
clean:
	latexmk -c

all:
	latexmk -pdf
    
Clean:
	latexmk -C
    
%: 
	latexmk -pdf $@.tex