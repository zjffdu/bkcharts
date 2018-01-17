#!/bin/bash

set -e
set -x

pip install bokeh==${BOKEH_VER} pandas mock pytest
python setup.py install
