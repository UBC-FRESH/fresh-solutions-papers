.PHONY: all clean

all: paper2-manuscript.pdf

paper2-manuscript.pdf: paper2-manuscript.tex references.bib
	latexmk -pdf -interaction=nonstopmode -halt-on-error paper2-manuscript.tex

clean:
	latexmk -C paper2-manuscript.tex
