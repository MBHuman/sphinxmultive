from setuptools import setup
from pathlib import Path
from sphinxmultive.version import __version__

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="sphinx-mutive",
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="Sphinx extension to build multiple versions of the same documentation",
    author="Evgeny Dmitriev",
    author_email="zenka712@mail.ru",
    download_url="",
    url="",
    install_requires=["sphinx"],
    license="MIT",
    packages=["sphinxmultive"],
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        'console_scripts': [
            'sphinxmultive = sphinxmultive.cli:main',
        ]
    },
    install_package_data=True
)
