import sys
from paver.easy import *

@task
def pep8():
    try:
        import pep8
    except:
        print('Please install pep8 first!')
        sys.exit(1)

    styleguide = pep8.StyleGuide(show_source=True, repeat=1, max_line_length=120)
    styleguide.input_dir('.')


