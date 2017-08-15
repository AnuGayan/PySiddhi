from subprocess import check_call

from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        # Compile JAVA Code here
        check_call("mvn clean install".split(), cwd="__PySiddhi4Proxy/")

        install.run(self)


packages = find_packages()
filtered_packages = []
for package in packages:
    if package.startswith("Tests"):
        continue
    filtered_packages.append(package)

setup(
    name="PySiddhi4",
    version="0.1.dev",
    packages=filtered_packages,
    install_requires=["pyjnius","future"],

    package_data={
                  "PySiddhi4": ["../__PySiddhi4Proxy/target/lib/*.jar",
                                 "../__PySiddhi4Proxy/target/*.jar",
                                 "../*.so"]
                  },

    # metadata for upload to PyPI
    author="WSO2",
    author_email="madhawavidanapathirana@gmail.com",
    description="Distribution of Siddhi CEP Python Wrapper",
    license="Apache2",
    cmdclass={
        'install': PostInstallCommand,
    },
    url="https://github.com/wso2/PySiddhi",  # project home page, if any

    # could also include long_description, download_url, classifiers, etc.
)
