import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="extra_streamlit_components",
    version="0.1.42",
    author="Mohamed Abdou",
    author_email="matex512@gmail.com",
    description="An all-in-one place, to find complex or just natively unavailable components on streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mohamed-512/Extra-Streamlit-Components",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords=['Python', 'Streamlit', 'React', 'JavaScript'],
    python_requires=">=3.6",
    install_requires=[
        "streamlit >= 0.80",
    ],
)
