from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
	name = 'pyis',
	packages = find_packages(),
	version = '0.1.0',
	author = 'Amirhossein Mohammadi',
	license = 'MIT',
	author_email = "amirhosseinmohammadi1380@yahoo.com",
    description = "PyIs library is a library to check values",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/BlackIQ/pyis"
)
