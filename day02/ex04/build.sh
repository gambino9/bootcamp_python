echo '--------- Upgrading pip... ---------'
python3 -m pip install --upgrade pip

# The next step is to generate distribution packages for the package.
# These are archives that are uploaded to the Python Package Index and
# can be installed by pip.
echo '--------- Upgrading build... ---------'
python3 -m pip install --upgrade build
echo '--------- Building package... ---------'
python3 -m build
# should output something like this :
#  dist/
#  my_minipack-1.0.0-py3-none-any.whl  --> built distribution file
#  my_minipack-1.0.0.tar.gz  --> source archive file

# Upgrade twine, that uploads all the archives under dist repository
# The .pypirc file removes the need to enter a username/password when
# pushing to PyPI and It simplifies command line usage when pushing
# packages to a non-default package repository
echo '--------- Upgrading twine... ---------'
python3 -m pip install --upgrade twine
echo '--------- Uploading package... ---------'
twine upload --repository testpypi dist/*

echo '--------- Installing package... ---------'
pip install -i https://test.pypi.org/simple/ my-minipack-lboukrou==1.0.0