@echo off
:: add to pythonpath 
set PYTHONPATH=%PYTHONPATH%;./.
coverage run -m pytest
coverage report -m
coverage html
