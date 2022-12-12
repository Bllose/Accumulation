from setuptools import setup
The magic is in the entry_points parameter. Below console_scripts, each line identifies one 
console script. The first part before the equals sign (=) is the name of the script that 
should be generated, the second part is the import path followed by a colon (:) with the 
Click command
    name='yourscript',
    version = '0.1.0',
    py_modules=['yourscript'],
    install_requires=['Click',],
    entry_points = {
        'console_scripts':[
            'yourscript=yourscript:cli',
        ],
Scripts in Packages
    yourpackage/
        __init__.py
        main.py
        utils.py
        scripts/
            __init__.py
            yourscript.py
    setup.py
In this case instead of using py_modules in your setup.py file you can use packages and the 
automatic package finding support of setuptools.
These would be the modified contents of setup.py:
=================================================
from setuptools import setup
    name='yourscript',
    version = '0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Click',],
    entry_points = {
        'console_scripts':[
            'yourscript=yourpackage.scriptes.yourscript:cli',
        ],
=================================================
