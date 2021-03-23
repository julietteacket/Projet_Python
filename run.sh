#!/bin/bash

echo "Looking for the environment named mon_env"
if [ ! -d "mon_env" ]
then
	echo "The virtual environment named mon_env doesn't exist. Creation of mon_env :"
	python3 -m venv mon_env
	echo "The virtuel environment is now created"
fi
	echo "The virtual environment named mon_env already exists"

echo " "



echo "Activation of the virtual environment"
source mon_env/bin/activate
echo "mon_env activated"
echo " "




echo "Loading the requirements"
pip install -r requirements.txt
echo "Requirements loaded"
echo " "



echo "Running the python code"
echo " "
python main.py
echo "End of the programm" 
