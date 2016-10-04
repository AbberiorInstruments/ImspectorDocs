Documentation for Imspector
===========================

What is Imspector
-----------------
Imspector is a software for image acquisition and analysis in high resolution microscopy. It is developed at the
Max Planck Institute of Biophysical Chemistry at the department of NanoBiophotonics and at the Abberior Instruments
GmbH.

Development Environment for this documentation
----------------------------------------------

1. have Python installed
1. have this repository cloned into `ImspectorDocs`
1. create and activate a python virtual environment
1. `pip install -U -r ImspectorDocs/requirements.txt`

After this you should be able to build the documentation:
1. `cd ImspectorDocs/docs/`
1. `make html` or `.\make.bat html`
1. now `ImspectorDocs\docs\_build\html` will contain the built docs