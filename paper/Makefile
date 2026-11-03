.PHONY: all clean

all: paper1-manuscript.pdf

paper1-manuscript.pdf: paper1-manuscript.tex references.bib
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper1-manuscript.tex

clean:
	latexmk -C paper1-manuscript.tex
