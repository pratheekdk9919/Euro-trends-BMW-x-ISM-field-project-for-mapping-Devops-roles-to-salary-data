"""
Setup configuration for Euro Trends BMW x ISM DevOps Salary Dashboard
"""

from setuptools import setup, find_packages
import os

# Read long description from README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("backend/requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="euro-trends-bmw-ism",
    version="1.0.0",
    author="Pratheek DK",
    description="A full-stack analytics platform for DevOps salary intelligence across European markets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data",
    project_urls={
        "Bug Tracker": "https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data/issues",
        "Documentation": "https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data#readme",
        "Source Code": "https://github.com/pratheekdk9919/Euro-trends-BMW-x-ISM-field-project-for-mapping-Devops-roles-to-salary-data",
    },
    packages=find_packages(where="backend", exclude=["tests*"]),
    package_dir={"": "backend"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business :: Financial",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: German",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    keywords=[
        "devops",
        "salary",
        "analytics",
        "machine-learning",
        "data-visualization",
        "flask",
        "react",
        "bmw",
        "ism",
        "europe",
        "germany",
        "workforce-planning",
    ],
    license="MIT",
)
