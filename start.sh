#!/bin/bash

## lancer les deux script à la fois
python Data_collect/pipeline_data/pipeline_collect_data.py &
python Data_collect/pipeline_data/pipeline_collect_data.py &

wait
# attend que tout le processus se termine