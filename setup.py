Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@UmbraVenus 
UmbraVenus
/
ml4a
forked from ml4a/ml4a
0
1
281
Code
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
ml4a/setup.py /
@UmbraVenus
UmbraVenus fixed neural-synth
Latest commit a192a51 21 minutes ago
 History
 3 contributors
@genekogan@UmbraVenus@Mayukhdeb
104 lines (94 sloc)  4.21 KB
  
import pathlib
from setuptools import setup, find_packages

packages = ['awca']


install_requires = [
    'torch',
    'transformer==3.1.0',
]


readme_file = pathlib.Path(__file__).parent / "README.md"

short_description = 'A toolkit for making art with machine learning, including an API for popular deep learning models, recipes for combining them, and a suite of educational examples'

for submodule, subfolders in submodules.items():
    submodule_packages = ['{}.{}'.format(submodules_root, submodule)]
    submodule_packages.extend(['{}.{}.{}'.format(submodules_root, submodule, f) for f in subfolders])
    packages.extend(submodule_packages)

setup(
    name='awca',
    version='0.0.1',
    description=short_description,
    long_description=readme_file.read_text(),
    long_description_content_type="text/markdown",
    url='http://github.com/UmbraVenus/',
    author='Sage Ren (Umbra Venus)',
    author_email='sage.shijie.ren@gmail.com',
    license='MIT',
    packages=packages, 
    install_requires=install_requires,
    zip_safe=False
)