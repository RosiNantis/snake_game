module  : a file ending with .py
          (you can import them)

package : a folder with modules
          (you can import them)
 
library : something you install
          (usually a package)

namespace : collection of names inside a Python object
            (there is a global namespace, but every object has its own)
            use dir() to list the contents
            use del x to remove from the namespace

making things pip-installable:

            1) pip install name  (follow the tutorial for creating PyPi packages)
            2) pip install git-url
            3) pip install -e .  (for development, START WITH THIS)

import mechanism: check this

        import sys
        sys.path  # list of all directories
        sys.path.append('directoryname')

uninstall a library:

       pip uninstall name


creating a pip-installable package:

- create setup.py in the main folder
- edit setup.py (most important: package name=spicy_snake/)
- pip install -e .
- moved code into the package folder (spicy_snake/)