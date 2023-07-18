import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

# if we want to publish this package in PyPI, in the homepage it will be readme

__version__ = "0.0"

REPO_NAME = "End-to-End_NLP_Text_Summarization"
AUTHOR_USER_NAME = 'Tirth'
SRC_REPO = 'TextSummarization'
AUTHOR_EMAIL = 'tirthdatascience@gmail.com'

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "End-to-End NLP Text Summarization",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/tirthhvora/End-to-End_NLP_Text_Summarization",
    project_urls = {
        "Bug tracker": "https://github.com/tirthhvora/End-to-End_NLP_Text_Summarization/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)