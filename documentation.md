# Implementing a DataFrame

## Introduction
I'v been thinking about this project for a while and only now getting to it, I was doing some python rehearsal and practice to get to more advanced topics and this is my way of putting some stuff I learned to work and practicing, In this documentation I'm going to write out all my thoughts and ideas throughout this project and try as much as I can to share the difficulties and solutions I find, hope you enjoy it!

## Journey
Numpy's ndarray (N-dimensional array) size can't change after initialization, current idea is to either create a new one with the new length and data or use the resize method by numpy for the ndarray.

Based on my knowledge of the DataFrame, when we store a singular column the data type of it is a pandas.Series, and the pandas Series is a One-dimensional ndarray with axis labels, so the current step is to create the Series class and after finishing its functionality move on to building the DataFrame with the help of the Series.

For a high performance DataFrame my idea is a dictionary of columns where the key is the name of the column and the value is the numpy ndarray.

The current idea for the flow is to take the data argument in the series constructor, pass it through a type checker method that I'm building and hopefully be able to convert the elements to a single uniform datatype, otherwise return a generic object datatype if complex types are present like lists or dicts.
The way to determine the datatype to use for the series to my understanding depends on the type hierarchy where we try to find the most general and safest datatype to convert the data to so that we have minimal data loss.