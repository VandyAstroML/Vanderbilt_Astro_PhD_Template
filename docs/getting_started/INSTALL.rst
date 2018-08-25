|RTD| |License| |Issues| |PDF_Latest|

**Author**: `Victor Calderon <http://vcalderon.me>`_ (`victor.calderon@vanderbilt.edu <mailto:victor.calderon@vanderbilt.edu>`_)

**Description**: An easy, reasonably standardized, but flexible template for 
creating Ph.D. theses from 
the `Vanderbilt University <https://www.vanderbilt.edu/>`_

This documentation is part of the repository
`Vanderbilt Ph.D. Thesis - Cookiecutter <https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template>`_

.. _phd_thesis_steps:

========================================
Steps to take to write your dissertation
========================================

The dissertation can be found at: `Vanderbilt Astro PhD Template <https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template>`_ 

This template is easy to use, and you only need to answer some questions.

.. _install_requirements:

---------------------------------------------
Requirements to use `cookiecutter` templates
---------------------------------------------

The minimum rquirements for creating `cookiecutter` templates are:

- Python 2.7 or 3.5
- `Cookiecutter Python package <http://cookiecutter.readthedocs.org/en/latest/installation.html>`_ >= 1.4.0: This can be installed with `pip` or `conda` depending on how you manage your Python packages.

You  can install it by typing this on the terminal

.. code-block:: bash

    pip install cookiecutter

or via Anaconda:

.. code-block:: bash

    conda config --add channels conda-forge
    conda install cookiecutter

Now you can use `cookiecutter` to create new templates for projects and papers!

.. _vandy_phd_download:

---------------------------------
Downloading Vanderbilt PhD Thesis
---------------------------------

After having done the steps in :ref:`_install_requirements`, you can start
creating the skeleton for the thesis.

You first need to run:

.. code-block:: shell
    
    cd /path/to/where/main/thesis/will/be/
    pip install cookiecutter
    cookiecutter https://github.com/VandyAstroML/Vanderbilt_Astro_PhD_Template

This will install the necessary packages and directories for the PhD Thesis.
It will also prompt you to anwer a few questions, and based on what you answer,
it will create fill in the template **for you**.

.. note::

    Make sure you :code:`cd` into the **correct path**. Otherwise, you will 
    be downloading the repository to the wrong directory.

.. _vandy_phd_fields:

---------------------------------
``cookiecutter`` Prompts
---------------------------------

Next, it will prompt you for some answers.
The different prompts are:

+-------------------------+----------------------------------------------------+
|Question                 | Description                                        |
+=========================+====================================================+
|:code:`thesis_title`     | Title of the thesis. Should not have '_' symbols   |
|                         | in it.                                             |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Understanding Exoplanets and Other Sources       |
|                         | * The Clustering of Galaxies on Smallest Scales    |
|                         |   Across Cosmic Time                               |
+-------------------------+----------------------------------------------------+
|:code:`first_name`       | Author's first name. :code:`first_name` will used  |
|                         | for the *title page* of the dissertation.          |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Adam                                             |
|                         | * Rose                                             |
+-------------------------+----------------------------------------------------+
|:code:`last_name`        | Author's **last** name. :code:`last_name` will     |
|                         | used for the *title page* of the dissertation.     |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Calderon                                         |
|                         | * Piscionere                                       |
+-------------------------+----------------------------------------------------+
|:code:`repo_name`        | Name of the directory/repository, in which the     |
|                         | theis will be saved. This name is selected by      |
|                         | default, but it can be changed. This field         |
|                         | **should not contain spaces**                      |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Calderon_Victor_Astro_PhD_Thesis                 |
|                         | * Szewciw_Adam_Astro_PhD_Thesis                    |
+-------------------------+----------------------------------------------------+
|:code:`add_signatures`   | Option for adding signatures to the thesis.        |
|                         |                                                    |
|                         | Options:                                           |
|                         |                                                    |
|                         | 1. "y" ... Add signatures                          |
|                         | 2. "n" ... Do not add signatures                   |
+-------------------------+----------------------------------------------------+
|:code:`department_name`  | Name of the department.                            |
|                         | Default: **Physics and Astronomy**.                |
|                         | Should **not** contain '_' (underscores) symbols.  |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Physics and Astronomy                            |
|                         | * Name of another department                       |
+-------------------------+----------------------------------------------------+
|:code:`dissertation_date`| Date of the Dissertation presentation.             |
|                         | Format: :code:`Month Year`.                        |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * May 2019                                         |
|                         | * August 2020                                      |
+-------------------------+----------------------------------------------------+
|:code:`name_committee_1` | First and last name of the committee member 1.     |
|                         | Should not have '_' symbols in it.                 |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Keivan Stassun                                   |
|                         | * Andreas Berlind                                  |
+-------------------------+----------------------------------------------------+
|:code:`name_committee_2` | First and last name of the committee member 2.     |
|                         | Should not have '_' symbols in it.                 |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Keivan Stassun                                   |
|                         | * Andreas Berlind                                  |
+-------------------------+----------------------------------------------------+
|:code:`name_committee_3` | First and last name of the committee member 3.     |
|                         | Should not have '_' symbols in it.                 |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Keivan Stassun                                   |
|                         | * Andreas Berlind                                  |
+-------------------------+----------------------------------------------------+
|:code:`name_committee_4` | First and last name of the committee member 4.     |
|                         | Should not have '_' symbols in it.                 |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Keivan Stassun                                   |
|                         | * Andreas Berlind                                  |
+-------------------------+----------------------------------------------------+
|:code:`name_committee_5` | First and last name of the committee member 5.     |
|                         | Should not have '_' symbols in it.                 |
|                         |                                                    |
|                         | Examples:                                          |
|                         |                                                    |
|                         | * Keivan Stassun                                   |
|                         | * Andreas Berlind                                  |
+-------------------------+----------------------------------------------------+

.. _vandy_phd_writing:

------------------
Writing the Thesis
------------------

Once you've downloaded the repository and answered all of the questions,
you can start writing your thesis.

My advice would be to follow these steps to guarantee that you're doing it 
correctly:

1. Create a new repository on `Github <http://www.google.com>`_.
   This will be the repository for your newly created local repository.
2. :code:`git init` your local repository.
3. Follow the instructions to upload the files of your dissertation to Github.
4. Write your dissertation.


After having downloaded and answered the questions, the repository should look like this:

.. code-block:: shell

    Calderon_Victor_Vanderbilt_Astro_PhD_Thesis/
    ├── Bibliography
    │   └── bibliography.bib
    ├── Chapters
    │   ├── acknowledgments.tex
    │   ├── appendix_A.tex
    │   ├── chapter_1.tex
    │   ├── chapter_2.tex
    │   ├── chapter_3.tex
    │   ├── chapter_4.tex
    │   ├── dedication.tex
    │   ├── future_work.tex
    │   ├── introduction.tex
    │   └── titlepage.tex
    ├── Extras
    │   ├── commands.tex
    │   ├── headings_settings.tex
    │   └── packages.tex
    ├── Figures
    │   ├── project_1
    │   ├── project_2
    │   └── project_3
    ├── Makefile
    ├── README.md
    ├── Thesis
    │   └── thesis.tex
    └── requirements.txt

    8 directories, 18 files

This is the file structure after creating the new repository.

The main file of the repository is: :code:`Thesis/thesis.tex`.
This is the file that will get compiled by LaTeX, and will produce a PDF 
version.

The only files that you will need to **edit** (aside from :code:`thesis.tex`)
are located in the :code:`Chapters` directory. These are the ones 
that you need to edit.

.. _using_template:

=====================
Using the Template
=====================

Now that one has answered the questions from :ref:`_vandy_phd_fields`,
you just need to fill in the documents in the ``Chapters`` directory
according to your thesis' needs.

The structure of the finalized thesis can be found in the
:ref:`proj_structure` section.

.. _uploading_overleaf:

==================================
Uploading your Thesis to Overleaf
==================================

Once you have completed setting up your Thesis, and are ready to start
the writing process, you can upload your paper to
`Overleaf <https://www.overleaf.com/>`_.

Overleaf, as explained on their website, is:

.. epigraph::

   Overleaf is a free service that lets you create, edit and share your
   scientific ideas easily online using LaTeX, a comprehensive and powerful
   tool for scientific writing.

   -- Overleaf Team

For a more in-depth tutorial on how to use
`Overleaf <https://www.overleaf.com/>`_, you can visit
`Overleaf Tutorial <https://www.overleaf.com/tutorial>`_ and watch the
attached video.

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; max-height: 100%; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/g8Ejj0T0yG4" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

.. _steps_overleaf:

--------------------------------------------------
Steps to follow to upload your Thesis to Overleaf
--------------------------------------------------

In order to upload your project to Overleaf, you need to follow the
following steps:

- Compress the output of ``cookiecutter`` template to a ``zip`` file.
- Create an account on Overleaf. Go to `Overleaf Sign-up <https://www.overleaf.com/signup>`_ 
- Create a **new, empty** "New Project"
- Click on **"Upload Project"**
- **Drag and drop** or click on **Select a .zip file**
- Connect your `Mendeley <https://www.mendeley.com/>`_ account. Open one if
  you don't have one. This will link your bibliography with Overleaf.
  See more `here <https://www.overleaf.com/blog/184-mendeley-integration-is-here-import-your-mendeley-reference-library-into-overleaf#.W4FGoZNKhhE>`_ 
- Remove the current 'Mendeley.bib' file from the project tree
- Click on "New file" > "From Mendeley" and name it **Mendeley.bib** and put
  it in the *root* directory of the project.

For a brief video on how to do this, see the following video:

.. raw:: html

    <div style="position: relative; padding-bottom: 56.25%; max-height: 100%; overflow: hidden; max-width: 100%; height: auto;">
        <iframe src="https://www.youtube.com/embed/t21IDEdGAUw" frameborder="0" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>

**And now you have a new, working PhD. Thesis.**

You can start writing now!

.. _vandy_phd_compiling:

---------------------
Compiling your Thesis
---------------------

This repository includes a :code:`Makefile`. This file serves as the file 
that will make the *cleaning*, *compiling*, and *opening the pdf* of the
:code:`thesis.tex` file.

To show all of the options of the Makefile, write:

.. code-block:: shell

    make show-help

This will show you a list of options:

.. code-block:: shell

    ./Calderon_Victor_Vanderbilt_Astro_PhD_Thesis: make show-help
    Available rules:

    all                 Perform all tasks
    clean               Clean all unnecessary latex-related files
    open_pdf            List all unnecessary files
    thesis.tex          Compiles Main Thesis file

To compile your thesis, you will need to run the following commands:

.. code-block:: shell

    make all

or 

.. code-block:: shell

    make thesis.tex

This will create all of the necessary files for compiling your thesis.

To open the PDF version of the thesis, run:

.. code-block:: shell

    make open_pdf

and a PDF version of the :code:`thesis.tex` file will pop up.

.. note::

    In order to properly use the Makefile and compile :code:`thesis.tex`,
    you will need :code:`latexmk` installed. If you're on a MAC, you want 
    to check out `the Latexmk documentation <https://mg.readthedocs.io/latexmk.html>`_,
    and make sure to have `MacTex <https://www.tug.org/mactex/>`_ installed 
    on your computer.

An example of the resulting PDF can be found in: 

.. image:: https://img.shields.io/badge/PDF-Latest-orange.svg
    :target: https://cdn.rawgit.com/VandyAstroML/Vandy_Starting_Grad_School/53e75f2c/docs/source/documents/phd_thesis/thesis.pdf
    :alt: Documentation Status



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
