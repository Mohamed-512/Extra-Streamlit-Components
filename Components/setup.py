import setuptools

setuptools.setup(
    name="extra-streamlit-components",
    version="0.0.1",
    author="Mohamed Abdou",
    author_email="",
    description="@Mohamed512a",
    long_description="",
    long_description_content_type="text/plain",
    url="https://github.com/Mohamed-512/Extra-Streamlit-Components",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    keywords=['Python', 'Streamlit', 'React'],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
