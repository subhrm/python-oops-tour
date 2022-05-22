# add to pythonpath 
export PYTHONPATH=$PYTHONPATH:.
coverage run -m pytest
coverage report -m
coverage html
