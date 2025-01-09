from setuptools import setup, find_packages

setup(
    name="ia_lib_renaneunao",
    version="0.0.1",
    description="Descrição da sua biblioteca",
    author="@renaneunao",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "dependencia1>=1.0.0",
        "dependencia2>=2.0.0",
    ],
)
