# Bootcamp Python : Module02 ex04

How to create a package in Python

# Before installation

Before uploading your pacage on TesPypi or Pypi, make sure to follow the following steps :  
- Create an account on TestPypi/Pypi
- Get your api token
- Create a `~/pypirc` file to define your configuration, so you don't have to enter your username / password
- Set the permissions on .pypirc so that only you can view or modify it. `chmod 600 ~/pypirc`

For example, my configuration looks like this : 
<pre><code>[distutils]
index-servers=
    testpypi

[testpypi]
repository: https://test.pypi.org/legacy/
username: __token__
password: `your_TestPypi_token`
</code></pre>
# Installation

`bash build.sh`

# Resources

https://truveris.github.io/articles/configuring-pypirc/
https://packaging.python.org/en/latest/tutorials/packaging-projects/#packaging-python-projects
https://packaging.python.org/en/latest/specifications/pypirc/
