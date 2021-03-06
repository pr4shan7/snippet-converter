import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='snippet-converter',
    packages=setuptools.find_packages(),
    version='0.1a9',
    license='MIT',
    description='A simple command line utility to convert and export snippets.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Prashant Tripathi',
    author_email='pr4shan7@gmail.com',
    url='https://github.com/pr4shan7/snippet-converter',
    download_url='https://github.com/pr4shan7/snippet-converter/archive/v0.1-alpha.9.tar.gz',
    project_urls={
        'Bug Reports': 'https://github.com/pr4shan7/snippet-converter/issues',
        'Source': 'https://github.com/pr4shan7/snippet-converter',
    },
    # scripts=['bin/snippet-converter'],
    entry_points={
        'console_scripts': [
            'scli=snippet_converter.cli:run',
        ],
    },
    keywords=['snippet'],
    # install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
    ],
    platforms=['Debian'],
    python_requires='>=3.6',
)
