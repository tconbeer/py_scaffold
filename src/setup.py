from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="new_project",
    version="0.1.0a1",
    author="Ted Conbeer",
    author_email="ted@shandy.io",
    description="new descriptoin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["new_project"],
    package_dir={"": "src"},
    license="Apache-2.0",
    python_requires=">=3.9.0",
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "new_project = new_project.cli:new_project",
        ],
    },
)
