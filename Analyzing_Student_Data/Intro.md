I believe that section is the first real exercise in this course.
It was really nice to start getting to know the capability of pandas library. Having a python background and no experience in pandas, I was always
thinking of a very complicated way to do things and process the data, however I found out that pandas comes to the rescue to perform these complicated tasks 
in a much easier way. It really gives the programmer the ability/capacity to focus on the ML algorithm itself rather than how to perform these tasks.

Take for instance:

That's a really elegant way to perform the hot encoding:  pd.get_dummies(data['rank'], prefix='rank')
at first I was thinking of a for loop and a condition to check for the number then fill the corresponding column with a '1' & the rest
with zero, but I was surprised with the capabilities of get_dummies function.

Then concatinating these hot encoded columns to the data was so easy too using:
`one_hot_data = pd.concat([data, pd.get_dummies(data['rank'], prefix='rank')], axis=1)`


Also, random choosing for the training vs the testing data. This came to the rescue.

`sample = np.random.choice(processed_data.index, size=int(len(processed_data)*0.9), replace=False)`
`train_data, test_data = processed_data.iloc[sample], processed_data.drop(sample)`

`np.random.choice` function does what I would have done in a few steps, first using rand function to generate rundom numbers, then 
in a for loop, add these values whose indices are gnerated to a new list.

Also, `iloc` function is very efficient from pandas library, it returns the whole row with the given number. Drop performs the opposite too.
So, in just 1 line, we were able to randomly select rows and assign t hem to train_data & the rest are assigned to test_data.
