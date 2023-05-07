import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.1.0"

requirements = []
setup_requirements = []
test_requirements = []

setuptools.setup(
    name="s3-file-uploader",
    version=__version__,
    author="Ozer, Ozge and Tugrul",
    author_email="deliyurek_22@hotmail.com",
    description="API to upload files to AWS S3",
    long_description=long_description,
    url="https://github.com/oozdal/s3-file-uploader",
    project_urls={
        "Bug Tracker": "https://github.com/oozdal/s3-file-uploader/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires="==3.8.8",
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
)
