#!/bin/bash

mkdir .evo-1
cd .evo-1
git clone https://github.com/ToniRV/evo-1.git
cd evo-1
pip install .
cd ../../
mkdir .kimera-eval
cd .kimera-eval
git clone https://github.com/MIT-SPARK/Kimera-VIO-Evaluation.git
cd Kimera-VIO-Evaluation
pip install -e .
cd ../../
pip install -r requirements.txt
