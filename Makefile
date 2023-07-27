.ONESHELL:

SHELL=/bin/zsh
CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
devops_state = main
working_dir = `pwd`

install: create_env activate setup_env

create_env:
	conda create -n hyperopt_prophet python=3.8 -y

setup_env:
	conda install poetry ipykernel ipywidgets -y \
	&& poetry install    

reinstall : create_env && install

activate:
	$(CONDA_ACTIVATE) hyperopt_prophet

rebuild: 
	pip uninstall hyperopt_prophet -y \
	&& poetry build  \
	&& pip install .

local_build_and_deploy: 
	pip uninstall hyperopt_prophet -y \
	&& python setup.py install \
	&& hyperopt_prophet

package_build:
	python -m build

package_list:
	unzip -l dist/*.whl  


