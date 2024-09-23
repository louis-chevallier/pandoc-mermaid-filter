

VERSION=$(shell python pandoc_filter_lc/pandoc.py)


start :
	echo install

wheel :
	VERSION=$(VERSION) python setup.py bdist_wheel --universal
	check-wheel-contents dist/pandoc_filter_lc-$(VERSION)-py2.py3-none-any.whl
	pip install dist/pandoc_filter_lc-$(VERSION)-py2.py3-none-any.whl
#	pip install --force-reinstall dist/pandoc-filter-lc-$(VERSION)-py2.py3-none-any.whl
# 	user = heaulier, pw <Laboite_IV> for PyPI

#       https://pypi.org/help/#apitoken
	python -m twine upload dist/pandoc_filter_lc-$(VERSION)-py2.py3-none-any.whl -uchevallier -p$(PYPI_CHEVALLIER_TOKEN) --verbose
#	-pip uninstall pandoc-filter-lc
	pip install pandoc_filter_lc
# 	cp test.py /tmp
#	( cd /tmp ; MINEKOLEVEL=0 python test.py  2>&1 | tee  pandoc-filter-lc.trc )



test :
	pandoc --filter==./mermaid.py readme.md


