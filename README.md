# Decision-Tree
Predict whether a movie will be a hit or not using decision tree.

Problem statement: Use categorical datasets with discrete and finite number of labels to build a decision tree which predicts the label of an unknown sample. 

Description: This is a supervised learning model which takes in a dataset and builds a decision tree from it using information gain of the features. The aim is to use the features of an unknown sample and follow the path they make in the decision tree. The leaf node of that path will be the predicted class. 

Output: The model takes any categorical dataset and builds a decision tree for it. The output is the preorder traversal of the decision tree.

The IDE used is PyCharm and the packages used are numpy, pandas and math.

Algorithm
1.	Find the entropies (measure of randomness. Higher the entropy, harder it is to draw any conclusions) of all the features of the dataset separately.
2.	To find the entropy, H(X), of a feature X, find the entropies of each of the groups in it one by one.
H(X) = w1* H(Group1)  +  w2*H(Group2) …so on
Where w1 is the portion of Group1 in the feature and w2 is the portion of Group2 in that feature.

H(Group1) = -p1*lg2(p1) – p0*lg2(p0)
Where p1 is the portion of positive class/label and p0 is the portion of negative class/label in the samples with group1

3.	Information Gain(feature) = 1 – Entropy(feautre)
4.	Choose the feature with the highest information gain to be the root of the decision tree.
5.	The different groups in that feature will be the child nodes of the root. For example, if ‘Country of origin’ is the feature with the maximum gain, it will be root. ‘US’, ‘Europe’ and ‘Rest’ will be the child nodes of root.
6.	Take each child node one by one. For each node, reduce the dataset to only the samples that have the same group. For example, for the node ‘US’, take only the samples with ‘US’ as the ‘Country of origin’. 
7.	Repeat steps 1-5 on this reduced dataset. Keep doing this until all the class/labels in the reduced dataset have the same value. This value will be the leaf node.
8.	To predict the class/label for an unknown sample, find the corresponding feature values in the tree. For example, if the sample has
Country = US	Big Star = no	Genre = comedy

![image](https://user-images.githubusercontent.com/54996440/168549295-4cb5ce6a-3ae8-4da4-9f32-93313b25e63c.png)

