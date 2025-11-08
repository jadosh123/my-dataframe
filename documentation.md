# Implementing a DataFrame

## Introduction
In this documentation I'm going to write out all my thoughts and ideas throughout this project and try as much as I can to share the difficulties and solutions I find, hope you enjoy it!

## Journey
Numpy's ndarray (N-dimensional array) size can't change after initialization, current idea is to either create a new one with the new length and data or use the resize method by numpy for the ndarray.

Based on my knowledge of the DataFrame, when we store a singular column the data type of it is a pandas.Series, and the pandas Series is a One-dimensional ndarray with axis labels, so the current step is to create the Series class and after finishing its functionality move on to building the DataFrame with the help of the Series.

For a high performance DataFrame my idea is a dictionary of columns where the key is the name of the column and the value is the Series.

The current idea for the flow is to take the data argument in the series constructor, pass it through a type checker method that I'm building and hopefully be able to convert the elements to a single uniform datatype, otherwise return a generic object datatype if complex types are present like lists or dicts.
The way to determine the datatype to use for the series to my understanding depends on the type hierarchy where we try to find the most safe datatype to convert the data to (while still prioritizing numerical data types) so that we have minimal data loss.

For the typing hierarchy it seems that pandas uses this setup:
**bool -> int -> float -> complex -> object.**

this is why when a pandas series contains a string or a list or any mapping the dtype resolves to object.
Numpy's ndarray doesn't allow multiple types unless we specify dtype=object on initialization which allows us to store multiple types in it since everything in python is an object.

However when using object as dtype we cant use numpy's vectorized operations.

Now while implementing the dunder repr method in my Series class I thought the padding that pandas added was based on the line with the max length but it seems that it calculates it based on the longest value and longest label regardless of wether they are on the same line or not and adds between them 4 white spaces.

I first went with the concatenation method inside a loop but its terrible in terms of performance since each time python has to concatenate a new string it needs to first allocate memory to hold the new size string and copy the contents into it each concatenation, but if we choose to store the different strings in a list and then do a join operation on the strings with an empty string the time complexity is M since python calculates the amount of memory needed for housing all the strings and allocates it one time.

I found that for a series of length > 60 pandas truncates the data in the repr method and only displays first and last 5 elements with two dots between.

Currently implementing the dunder getitem method, when calling the pandas series object with one index it returns the element in the values array at that index, when calling it with a slice it returns a new object of type Series that represents the slice.

Pandas gives a warning for single index lookup that treating keys as positions is deprecated and in the future version, integer keys will always be treated as labels.

This means that for single index lookup we can either iterate over the index array and store the index that matches the requested label and then return the value at that index or we can store a private dictionary using the single leading underscore for O(1) lookup.

Now I'v implemented slicing, indexing by integer and by label, currently adding some unittests to try to cover some cases.
Next step will probably be implementing .iloc or .loc functionality? I need to learn decorators especially the @property decorator in order to open a function in the Series class that can handle indexing with these attributes.

After looking into it I see that when we print the object returned by pd.Series().iloc it shows us this: pandas.core.indexing._iLocIndexer

That means we need to implement the _iLocIndexer and the _LocIndexer as seperate classes with their own dunder getitem method and when we implement the property decorator we return a instance of that class with self as the argument.

I'v learned about decorators now is the time to use the @property decorator in order to implement the .iloc and .loc functionality.

I implemented the int only indexer iloc and the label indexer loc which also supports passing a list of labels and returns a new Series object with that data just like pandas.

Now its time to add some unit tests to cover the new stuff we implemented.

Moving forward, all the attributes that depend on the series current state will be implemented with the @property decorator to allow them to change along with any changes in the series.

Now I'm attempting to understand pandas behavior when it comes to missing values either in labels or values, in values it converts None to np.nan which is type float but in the labels array when encountering None it keeps it as None and casts the entire labels array to dtype object which is numpy object_.