############################################################
#
# Makefile für Abschlussarbeit
#
# Mögliche Aufrufe:
#  - make        : erzeugen der gesamten Arbeit als pdf
#  - make clean  : löschen fast aller Dateien im Verzeichnis
#
# Mögliche/nötige Anpassungen gekennzeichnit mit ???
#
############################################################

# ??? Name des LaTeX-Datei mit Endung .tex (ggfs. anpassen)
NAME	= abschlussarbeit

# Überschreiben Default-Regel für .tex Endungen
%.dvi: %.tex

# Regel, um aus .bib eine .bbl zu machen
%.bbl: %.bib
	bibtex $*

# Verhindert das Löschen von Zwischendateien nach make
.SECONDARY: $(NAME).bbl $(NAME).dvi

.PHONY: default clean


############################################################
#
# ??? LaTeX kennt entweder LaTeX+dvips oder pdflatex
# Unterschiede selber rausfinden (z.B.- unterstützte Grafikformate)
# Eine Version davon muss man sich aussuchen.
#
############################################################

# Version 1 (LaTeX + dvips; hier auskommentiert)
#TEX	= latex
#DVIPDF	= dvipdf
# aus tex-Datei pdf-datei generieren inkl. aktuellem Literaturverzeichnis
#%.pdf: %.tex
#	$(TEX) $*
#	-bibtex $*
#	$(TEX) $*
#	$(TEX) $*
#	$(DVIPDF) $*

# Version 2 (pdflatex; derzeit auskommentiert)
TEX	= pdflatex
# aus tex-Datei pdf-datei generieren
%.pdf: %.tex
	$(TEX) $*
	-bibtex $*
	$(TEX) $*
	$(TEX) $*

############################################################
# das sind die möglich Ansprungziele beim Aufruf

default:: $(NAME).pdf

clean::
	-rm -f	*.aux *.toc *.dvi *.ind *.ilg *.cb *.cb2 *.idx *.log *.bbl *.blg *.pdf *.out *.lof *.lot

############################################################


