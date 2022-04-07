from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Mapping environment variables to class variable'
LONG_DESCRIPTION = 'A Python package that makes working with environment variables and configurations eazy'

# Setting up
setup(
    name="pyenvclass",
    version=VERSION,
    author="Mattias Strömdahl",
    author_email="Mattias.Stromdahl@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/Stromdahl/PyEnvClass',
    long_description=LONG_DESCRIPTION,
    py_modules=["module_envclass"],
    package_dir={'': 'src'},
    keywords=['python', 'env', 'environment', 'variables'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
