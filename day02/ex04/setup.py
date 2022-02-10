from setuptools import setup

setup(
    name="my-minipack",
    version="1.0.0",
    description="How to create a package in Python",
    author="lboukrou",
    author_email="lboukrou@student.42.fr",
    install_requires=[
        'ftmuart==0.0.5',
        'python_ble_client==1.11.0',
        'crccheck==1.0',
        'RPi.GPIO==0.7.0',
        'timeout-decorator==0.5.0',
        'pyserial==3.5',
        'pytest==6.2.4',
    ],
    packages=[
        "ylesia",
        "ylesia.ble_protocol",
        "ylesia.uart_protocol",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    # packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)