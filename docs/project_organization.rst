|RTD| |License| |Issues| |PDF_Latest|

.. _proj_structure:

=================
Project Structure
=================

The organization of the project is the following:

.. code-block:: text

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

.. ----------------------------------------------------------------------------

Project based on the `modified <https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template>`_  version of the
` Vanderbilt University Thesis Template <https://www.sharelatex.com/templates/thesis/vanderbilt-university-thesis>`_.

.. |Issues| image:: https://img.shields.io/github/issues/VandyAstroML/Vanderbilt_Astro_PhD_Template.svg
   :target: https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template/issues
   :alt: Open Issues

.. |RTD| image:: https://readthedocs.org/projects/mnras-cookiecutter/badge/?version=latest
   :target: https://mnras-cookiecutter.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template/blob/master/LICENSE
   :alt: Project License

.. |PDF_Latest| image:: https://img.shields.io/badge/PDF-Latest-orange.svg
   :target: https://cdn.rawgit.com/VandyAstroML/Vandy_Starting_Grad_School/53e75f2c/docs/source/documents/phd_thesis/thesis.pdf
   :alt: PDF Latest