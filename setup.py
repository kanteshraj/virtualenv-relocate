import sys
from setuptools import setup


if __name__ == '__main__' and sys.version_info < (2, 5):
    raise SystemExit("Python >= 2.5 required for virtualenv-clone")


setup(name="virtualenv-relocate",
    version='0.1.0',
    description='script to relocate virtualenvs',
    author='Kantesh Raj',
    author_email='kanteshraj@gmail.com',
    url='https://github.com/kanteshraj/virtualenv-relocate',
    license="MIT",
    py_modules=["relocate"],
    entry_points={
        'console_scripts': [
            'virtualenv-relocate=relocate:main',
    ]},
    classifiers=[
        "License :: MIT License",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
    ]
)