# Copyright (c) 2019 Uber Technologies, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from setuptools import find_packages, setup

CMD_NAME = "bob"

# Derive install requires from base.in first order requirements
with open("requirements/base.in") as f:
    requirements = f.read().strip()
requirements = requirements.replace("==", ">=").split()  # Convert to non-pinned for setup.py

with open("requirements/optimizers.in") as f:
    opt_requirements = f.read().strip()
opt_requirements = opt_requirements.replace("==", ">=").splitlines()  # Convert to non-pinned for setup.py
opt_requirements = [pp for pp in opt_requirements if pp[0].isalnum()]

with open("requirements/ipynb.in") as f:
    ipynb_requirements = f.read().strip()
ipynb_requirements = ipynb_requirements.replace("==", ">=").splitlines()  # Convert to non-pinned for setup.py
ipynb_requirements = [pp for pp in ipynb_requirements if pp[0].isalnum()]

with open("README.md") as f:
    long_description = f.read()

setup(
    name="bo_benchmark",
    version="0.0.1",
    packages=find_packages(),
    url="https://github.com/uber/bo-benchmark/",
    author="Ryan Turner",
    author_email=("rdturnermtl@github.com"),
    license="Apache v2",
    description="Bayesian optimization benchmark system",
    install_requires=requirements,
    extras_require={"optimizers": opt_requirements, "notebooks": ipynb_requirements},
    long_description=long_description,
    long_description_content_type="text/markdown",
    platforms=["any"],
    entry_points={
        "console_scripts": [
            CMD_NAME + "-init = bo_benchmark.experiment_db_init:main",
            CMD_NAME + "-launch = bo_benchmark.experiment_launcher:main",
            CMD_NAME + "-agg = bo_benchmark.experiment_aggregate:main",
            CMD_NAME + "-baseline = bo_benchmark.experiment_baseline:main",
            CMD_NAME + "-anal = bo_benchmark.experiment_analysis:main",
            CMD_NAME + "-exp = bo_benchmark.experiment:main",
        ]
    },
)