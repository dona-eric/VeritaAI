#!/bin/bash

## lancer les deux script à la fois
python Data_collect/pipeline_connection_database_collect_data/connect_database.py &
python Data_collect/pipeline_connection_database_collect_data/pipeline_collect_data.py &
python Data_collect/pipeline_connection_database_collect_data/pipeline_save_data.py

wait
# attend que tout le processus se termine