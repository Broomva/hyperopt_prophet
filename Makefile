SHELL=/bin/bash
devops_state = main
working_dir = `pwd`

install: local_build_and_deploy

reinstall : create_env && install

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

create_env:
	conda deactivate -n hyperopt_prophet \
	&& conda env remove -n hyperopt_prophet -y \
	&& conda create -n hyperopt_prophet python=3.10 -y \
	&& conda activate hyperopt_prophet
