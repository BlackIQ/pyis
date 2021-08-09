from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup (
	name = 'pyis',
	packages = find_packages(),
	version = '0.12.0',
	author = 'Amirhossein Mohammadi',
	license = 'MIT',
	author_email = "amirhosseinmohammadi1380@yahoo.com",
    description = "A library to check your values in your projects",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/BlackIQ/pyis"
)