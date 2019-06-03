define PROJECT_HELP_MSG

Usage:

    make help                   show this message
    make clean                  remove intermediate files (see CLEANUP)

    make install                initializes the project
    make docs					generates the docs for the project

endef
export PROJECT_HELP_MSG

help:
	echo $$PROJECT_HELP_MSG


install:
	( \
       /usr/local/bin/python3 -m venv venv; \
       source venv/bin/activate; \
       pip install -r requirements.txt; \
       mkdir ~/.portfolio_data; \
    )

docs:
	( \
       cd docs; \
       sphinx-apidoc -o source/ ../src/; \
       make html; \
    )

clean:
	rm -rf venv
	( \
       cd docs; \
       make clean; \
    )

.PHONY: docs clean