SHELL=/bin/bash
devops_state = main
working_dir = `pwd`

install: local_build_and_deploy

reinstall : create_env && install

rebuild: 
	pip uninstall hyperopt_prophet_spark -y \
	&& poetry build  \
	&& pip install .

local_build_and_deploy: 
	pip uninstall hyperopt_prophet_spark -y \
	&& python setup.py install \
	&& hyperopt_prophet_spark

package_build:
	python -m build

package_list:
	unzip -l dist/*.whl  

create_env:
	conda deactivate -n hyperopt_prophet_spark \
	&& conda env remove -n hyperopt_prophet_spark -y \
	&& conda create -n hyperopt_prophet_spark python=3.10 -y \
	&& conda activate hyperopt_prophet_spark
