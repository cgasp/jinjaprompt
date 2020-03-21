import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jinjaprompt",
    version="0.0.1",
    author="cgaspar",
    author_email="me@cgaspar.net",
    description="Package to facilitate the file creation with templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cgasp/jinjaprompt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'jinjaprompt = jinjaprompt.__main__:main'
          ]
    }
)