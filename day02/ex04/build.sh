python3 -m pip install --upgrade pip

python3 -m pip install --upgrade build
python3 -m build
# should output something like this :
# dist/
#  my_minipack-1.0.0-py3-none-any.whl  --> built distribution file
#  my_minipack-1.0.0.tar.gz  --> source archive file

python3 -m pip install --upgrade twine
twine upload --repository testpypi dist/*

#python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-YOUR-USERNAME-HERE

pip install -i https://test.pypi.org/simple/ my-minipack-lboukrou==1.0.0