# exercise-compiler
#
# 2023, Matthias Rüdt, HES-SO Valais-Wallis

import argparse
import os
import subprocess


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
                    prog='exercise-compilter',
                    description='Convert Jupyter notebook based exercises to solutions and exercises')
    parser.add_argument('filename')
    args = parser.parse_args()
    notebook = args.filename
    
    # generate subcommands
    # TODO convert to conversion based on library
    command_base = f'jupyter nbconvert {notebook} --output-dir="./output" '
    remove_solution = '--TagRemovePreprocessor.enabled=True ' +\
        ' --TagRemovePreprocessor.remove_cell_tags="[' + "'solution'" + ']" '
    to_html = '--to HTML '
    to_notebook = '--to notebook '


    # Generate folder
    try:
        os.mkdir('output')
    except FileExistsError:
        # if folder exists, this is no issue
        pass

    # generate HTML without solution
    cmd = command_base + remove_solution + to_html
    subprocess.run(cmd, shell=True)

    # generate ipynb witout solution
    cmd = command_base + remove_solution + to_notebook
    subprocess.run(cmd, shell=True)

    # generate HTML with solution
    cmd = command_base + to_html
    cmd += ' --output ' + notebook[:-5] + 'solution'
    subprocess.run(cmd, shell=True)

    # generate notebook with solution
    cmd = command_base + to_notebook
    cmd += '--output ' + notebook[:-5] + 'solution'
    subprocess.run(cmd, shell=True)