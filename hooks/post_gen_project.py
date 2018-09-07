#!/usr/bin/env python

import os
import shutil


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))


def copy_file(original_filepath, new_filepath):
    shutil.copyfile(os.path.join(PROJECT_DIRECTORY, original_filepath),
                    os.path.join(PROJECT_DIRECTORY, new_filepath))

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

license_files = {"BSD 3-Clause": 'BSD3.rst',
                 "GNU GPL v3+": 'GPLv3.rst',
                 "Apache Software Licence 2.0": 'APACHE2.rst',
                 "BSD 2-Clause": 'BSD2.rst',
                 "MIT": 'MIT.rst'}

def process_licence(licence_name):
    """
    Processes the License file for the document.

    Parameters
    ----------
    licence_name : str
        Name of the License to use.
    """
    if licence_name in license_files:
        shutil.copyfile(os.path.join(PROJECT_DIRECTORY, 'licenses', license_files[licence_name]),
                        os.path.join(PROJECT_DIRECTORY, 'LICENSE.rst'))
    ##
    ## Remove `licenses` folder
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, 'licenses'))

def bibliography_create():
    """
    Creates the `.bib` file, based on the answer from cookiecutter.use_Overleaf
    """
    if ('{{ cookiecutter.use_Overleaf.lower() }}' == 'yes'):
        bib_path = 'bibliography.bib'
    else:
        bib_path = './Bibliography/bibliography.bib'
    ## Creating file
    try:
        open(bib_path, 'a').close()
        assert(os.path.exists(bib_path))
    except:
        raise ValueError('`{0}` file could not be created'.format(bib_path))

# Running command
if __name__ == '__main__':

    ## Licence
    process_licence('{{ cookiecutter.open_source_license }}')
    ##
    ## Bibliography
    bibliography_create()
    ##
    ## Initializing repository
    try:
        from git import Repo

        new_repo = Repo.init(PROJECT_DIRECTORY)
        new_repo.git.add('.')
        new_repo.index.commit(
            "Creation of {{ cookiecutter.repo_name }} from MNRAS template"
        )
    except ImportError:
        err_msg  = 'gitpython is not installed. '
        err_msg += 'The repository will not be initialized!'
        print(err_msg)
