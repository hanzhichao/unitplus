

cd docs && sphinx-apidoc -o . ../python_yapi && make html && cd - || exit


#sphinx-build -b gettext . locale
#sphinx-intl update -p locale -l zh_CN
