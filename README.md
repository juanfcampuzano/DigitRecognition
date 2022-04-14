# MNIST digit recognizer
- Created a tool that identifies handwritten digits (from 0 to 9).
- Used Kaggle’s datasets to train and evaluate the model.
- Preprocessed the images using normalization and binning techniques.
- Optimized a Convolutional Neural Network to reach the highest accuracy.
- Performed error analysis to make decisions to improve model performance.
- Built a client facing API using Django. 
# Code and Resources Used
**Python Version:** 3.7

**Packages:** tensorflow, matplotlib, sklearn, numpy, pandas, seaborn
# Feature Engineering
First, I preprocessed the data. For that I first normalized the images, then I binned the pixel values into three groups according to their intensity.
I thought this would be helpful because of the weakness of some strokes in the misclassified pictures, I thought that making them stronger would make it easier for the model to classify the image.

# Model Building
I split the data into train and validation sets with a validation size of 20% (for testing I used the given test set and submitted it to get a public score).

I used a Convolutional Neural Network model and evaluated it using Accuracy.

The first step was to overfit the training set to reduce bias and then make adjustments to the model to reduce variance. 
Techniques to reduce bias: train the model for a longer time, make the neural network deeper, add more neurons to the network.
Techniques to reduce variance: add dropout layers, l2 regularization, batch normalization.

# Model Performance
The performance of the Convolutional Neural Network was satisfactory. 

# Productionalization
