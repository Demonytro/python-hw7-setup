from setuptools import setup, find_namespace_packages

with open('README.md','r', encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name = 'clean_folder',
    version = '1.0.3',
    description = 'Sort folder code',
    url = 'https://github.com/Demonytro/python-hw7-sort.git',
    author = 'Dmytro Oseledko',
    author_email = 'd.oseledko@outlook.com',
    long_description = 'long_description',
    classifiers = [
        'Python version :: Python :: 3.10',
        'Operating System :: Windows'
    ],
    license = 'MIT license',
    packages = find_namespace_packages(),
    install_requires = ["requests"],
    entry_points = {'console_scripts': ['clean-folder = clean_folder.clean:main']}
)