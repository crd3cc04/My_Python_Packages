from setuptools import find_packages, setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name="my_lambadata",
    version="1.0",
    author="Cortesha RosaRobinson",
    author_email="crd3cc04@gmail.com",
    description="For example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/crd3cc04/my_packages_crd3cc04",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)