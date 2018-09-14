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
* If you meet an error after inputting above commands in Linux, the specific contents are as follows:
</br>`Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/sklearn'
Consider using the `--user` option or check the permissions.`
</br>Users can change the commands into:
</br>`pip install numpy --user` 
</br>`pip install pandas --user`
</br>`pip install matplotlib --user`
</br>`pip install scipy --user`
</br>`pip install scikit-learn --user`

# Running PredGly
open cmd in Windows or terminal in Linux, then cd to the PredGly/codes folder which contains predict.py
</br>**For general glycation site prediction using our model, run:**
</br>`python predict.py -input [custom predicting data in txt format] -threshold [threshold value] -output [custom specified file for predicting results]`  
</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5`
**For details of other parameters, run:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5`
