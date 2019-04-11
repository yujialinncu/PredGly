# PredGly
PredGly uses a machine learning method to predit lysine glycation sites for homo sapiens. Users can run program with specified protein sequences.

# Installation
* Install [Python 2.7](https://www.python.org/downloads/) in Linux and Windows.
* Because the program is written in Python 2.7, python 2.7 with the pip tool must be installed first. Glycation uses the following dependencies: numpy, pandas, matplotlib, scipy and scikit-learn. You can install these packages first, by the following commands:
```
pip install numpy
pip install pandas
pip install matplotlib
pip install scipy
pip install scikit-learn
```
* If you meet an error after inputting above commands in Linux, the specific contents are as follows:
</br>Could not install packages due to an EnvironmentError: [Errno 13] Permission denied: '/usr/local/lib/python2.7/dist-packages/sklearn'
Consider using the '--user' option or check the permissions.
</br>Users can change the commands into:
```
pip install numpy --user
pip install pandas --user
pip install matplotlib --user
pip install scipy --user
pip install scikit-learn --user
```

# Running PredGly
open cmd in Windows or terminal in Linux, then cd to the PredGly-master/codes folder which contains predict.py
</br>**For general glycation site prediction using our model, run:**
</br>`python predict.py -input [custom predicting data in txt format] -threshold [threshold value] -output [ predicting results in csv format]`  
</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5 -output ../codes/results.csv`
</br>-output is optional parameter, while -input and -threshold are required parameters. Prediction results will show in the cmd or terminal, and if you don't want to save results, you need not input -output.

</br>**Example:**
</br>`python predict.py -input ../codes/example.txt -threshold 0.5`

</br>**For details of -input,-threshold and -output, run:**
</br>`python predict.py -h`

# Announcements
* In order to obtain the prediction results, please save the query protein sequences and protein name in txt format. Users can refer to the example.txt under the codes folder. Also of note, each protein name should be added by '>', otherwise the program will occur error.
* The accepted amino acids are: A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y, and a virtual amino acid O. If the protein fragments contain other amino acids, the program only will predict fragments which contain above-mentioned 21 amino acids. 
* To save the prediction results, the -ouput should be in csv format.
