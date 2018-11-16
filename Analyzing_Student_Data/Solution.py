# TODO:  Make dummy variables for rank
one_hot_data = pd.concat([data, pd.get_dummies(data['rank'], prefix='rank')], axis=1)
# TODO: Drop the previous rank column
one_hot_data = one_hot_data.drop('rank', axis=1)

# Print the first 10 rows of our data
one_hot_data[:10]


# Making a copy of our data
processed_data = one_hot_data[:]

# TODO: Scale the columns
processed_data['gpa'] = processed_data['gpa']/4.0
processed_data['gre'] = processed_data['gre']/800

# Printing the first 10 rows of our procesed data
processed_data[:10]
