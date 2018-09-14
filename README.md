# PredGly
PredGly uses a machine learning method to predit lysine glycation sites for homo sapiens. Users can run program with specified protein sequences.
# Installation
* Install [Python 2.7](https://www.python.org/downloads/) in Linux and Windows.
* Because the program is written in Python 2.7, python 2.7 with the pip tool must be installed first. Glycation uses the following dependencies: numpy, pandas, matplotlib, scipy and scikit-learn. You can install these packages first, by the following commands:
</br>`pip install numpy`   
</br>`pip install pandas`  
</br>`pip install matplotlib`
</br>`pip install scipy`
</br>`pip install scikit-learn`
# Running PredGly
cd to the PredGly/codes folder which contains predict.py
For general glycation site prediction using our model, run:
</br>`python predict.py -input [custom predicting data in txt format] -threshold [threshold value]`  
