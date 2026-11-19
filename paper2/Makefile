.PHONY: all clean

all:
	cd submission/jors && latexmk -pdf -interaction=nonstopmode -halt-on-error paper2-jors.tex

clean:
	cd submission/jors && latexmk -C paper2-jors.tex
