import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vizion",
    version="0.0.1",
    author="Misael Borges",
    author_email="nexcsbr@gmail.com",
    description="Python Library to create your own IA for object detection.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/misaelbg/vizion",
    download_url="https://github.com/misaelbg/vizion/archive/0.0.1.tar.gz",
    keywords=['tensorflow', 'computer vision', 'object detection', 'Artificial inteligence', 'IA'],
    packages=['vizion'],
    install_requires=[
        'opencv-contrib',
        'argparse',
        'pathlib',
        'numpy',
    ],
    classifiers=(
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts':
        ['vizion=vizion.console:main'],
    }
)