from setuptools import setup, find_packages

setup(
    name="crack-pdf",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "PyPDF2",
    ],
    entry_points={
        "console_scripts": [
            "crack-pdf=crack_pdf.core:main",
        ],
    },
)
