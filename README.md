[![Documentation Status](
https://readthedocs.org/projects/vanderbilt-astro-phd-template/badge/?version=latest)](
https://vanderbilt-astro-phd-template.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](
https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template/blob/master/LICENSE)
[![GitHub issues](
https://img.shields.io/github/issues/VandyAstroML/Vanderbilt_Astro_PhD_Template.svg)](
https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template/issues)
[![Documentation Status](https://img.shields.io/badge/PDF-Latest-orange.svg)](
https://cdn.rawgit.com/VandyAstroML/Vandy_Starting_Grad_School/53e75f2c/docs/source/documents/phd_thesis/thesis.pdf)

# Cookiecutter - Vanderbilt Ph.D. Thesis

_**An easy, reasonably standardized, but flexible template for the Vanderbilt Ph.D. Thesis.**_

## Author

- [Victor Calderon](http://vcalderon.me) ([victor.calderon@vanderbilt.edu](victor.calderon@vanderbilt.edu))

## Description

This template was based on the [Cookiecutter Data Science Project](http://drivendata.github.io/cookiecutter-data-science/)

An example of the resulting PDF can be found in:

[![Documentation Status](https://img.shields.io/badge/PDF-Latest-orange.svg)](https://cdn.rawgit.com/VandyAstroML/Vandy_Starting_Grad_School/53e75f2c/docs/source/documents/phd_thesis/thesis.pdf)

For the **full documentation**, see:

[![Documentation Status](https://readthedocs.org/projects/vanderbilt-astro-phd-template/badge/?version=latest)](https://vanderbilt-astro-phd-template.readthedocs.io/en/latest/?badge=latest)

## Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
pip install cookiecutter
```

or

``` bash
conda config --add channels conda-forge
conda install cookiecutter
```

## To start a new project, run:
------------

In order to create the skeleton of the template, you have to run this from the terminal:

    cookiecutter https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template

For an example on how to properly do this, see the following video. It serves as a demonstration on how `cookiecutter` works.

[![asciicast](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02.png)](https://asciinema.org/a/9bgl5qh17wlop4xyxu9n9wr02)

## The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── Bibliography             <- Folder with the .bib bibiography used in the thesis.
│   └── bibliography.bib
│
├── Chapters                 <- Folder with the thesis' chapters, appendices, dedication section, and other sections.
│   ├── acknowledgments.tex
│   ├── appendix_A.tex
│   ├── chapter_1.tex
│   ├── chapter_2.tex
│   ├── chapter_3.tex
│   ├── chapter_4.tex
│   ├── dedication.tex
│   ├── future_work.tex
│   ├── introduction.tex
│   └── titlepage.tex
│
├── Extras                  <- Folder with documents like main `aliases`, `packages`, etc.
│   ├── commands.tex        <- List of commands used throughout the thesis
│   ├── headings_settings.tex <- Settings used for the different sections, chapters, etc.
│   └── packages.tex        <- List of packages to load for the thesis.
│
├── Figures                 <- Directory for project figures
│   ├── project_1           <- Each project has its own folder for figures
│   ├── project_2
│   └── project_3
│
├── Thesis
│   └── thesis.tex          <- Main `Thesis` file. The main thesis goes here
│
├── Makefile                <- Makefile with commands like `make main.tex` or `make clean`
├── requirements.txt        <- File with a list of packages required for running this
└── README.md               <- The top-level README for students

```

## Contributing

Contributions are welcomed! If you have any suggestions, feel free to submit a _Pull Request_.

## Installing development requirements
------------

    pip install -r requirements.txt
