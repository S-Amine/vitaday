from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vitaday/__init__.py
from vitaday import __version__ as version

setup(
	name="vitaday",
	version=version,
	description="a css theme for vitaday",
	author="Saidi Amine",
	author_email="contact",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
