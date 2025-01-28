import numpy as np
import pandas as pd

# Function to calculate entropy
def entropy(target_col):
    elements, counts = np.unique(target_col, return_counts=True)
    entropy = -np.sum([(counts[i] / np.sum(counts)) * np.log2(counts[i] / np.sum(counts)) for i in range(len(elements))])
    return entropy

def information_gain(data, split_attribute, target_name="class"):
    total_entropy = entropy(data[target_name])

    values, counts = np.unique(data[split_attribute], return_counts=True)
    weighted_entropy = np.sum([(counts[i] / np.sum(counts)) *
                                entropy(data.where(data[split_attribute] == values[i]).dropna()[target_name]) for i in
                                range(len(values))])

    
    information_gain = total_entropy - weighted_entropy

    return information_gain


def id3(data, original_data, features, target_name="class", parent_node_class=None):
    # If all target values have the same class, return this class
    if len(np.unique(data[target_name])) <= 1:
        return np.unique(data[target_name])[0]

    # If the dataset is empty, return the mode target feature value from the original dataset
    elif len(data) == 0:
        return np.unique(original_data[target_name])[np.argmax(np.unique(original_data[target_name], return_counts=True)[1])]

    # If no more features, return the mode target feature value
    elif len(features) == 0:
        return parent_node_class
    else:
        parent_node_class = np.unique(data[target_name])[np.argmax(np.unique(data[target_name], return_counts=True)[1])]
        item_values = [information_gain(data, feature, target_name) for feature in features]
        best_feature_index = np.argmax(item_values)
        best_feature = features[best_feature_index]

        tree = {best_feature: {}}
        features = [i for i in features if i != best_feature]
        for value in np.unique(data[best_feature]):
            value_data = data.where(data[best_feature] == value).dropna()
            subtree = id3(value_data, original_data, features, target_name, parent_node_class)
            tree[best_feature][value] = subtree

        return tree
data = pd.DataFrame({
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny', 'Sunny', 'Rain',
                'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool', 'Mild', 'Mild', 'Mild',
                    'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'Normal',
                 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['False', 'True', 'False', 'False', 'False', 'True', 'True', 'False', 'False', 'False', 'True', 'True',
              'False', 'True'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
})
features = list(data.columns[:-1])
target = 'PlayTennis'
tree = id3(data, data, features, target)
print("Decision Tree:", tree)

