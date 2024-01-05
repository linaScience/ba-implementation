# Implementation to predict human movement towards a specific Access Point

This is the implementation for my bachelor's thesis "Machine Learning-based User Movement Prediciton in Layer 2 Networks" at Hasso-Plattner-Institute.

The goal of this thesis is to find out, if human movement towards a specific Access Point can be predicted.

## Getting the data

1. To download the files needed for the analysis and machine learning part, please go to [dataset](https://www.kaggle.com/competitions/indoor-location-navigation/data).
2. Unzip the .zip file into the root folder of this repository.

## Working with the data

1. Make sure you have downloaded the data as described in [the previous step](#getting-the-data).
2. Execute any of the following scripts:
   * `data-ana.py`: To get an overview of the folder structure
   * `aggregate_file.py`: To aggregate all files of a floor to one file.
   * `count_wifi_lines.py`: To get to know, how many Wi-Fi data there is for the floor with the most files/traces (it uses the aggregate file).

## Preparation

Execute `preparation.ipynb` to prepare the data of the floor with the most traces for the LSTM model.

## Tune, train and test model

Execute `lstm.ipynb` for tuning, training and testing the LSTM model.

## Evaluate the model

Execute `evaluation.ipynb` to evaluate the model and compare it to a heuristic approach.
The results can be seen in `comparison_ml_heuristic_1_to_5.pdf`, `comparison_ml_heuristic_3.pdf` and `heuristic_plot.pdf`.
