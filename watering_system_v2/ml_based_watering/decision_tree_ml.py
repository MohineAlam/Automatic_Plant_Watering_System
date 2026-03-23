import numpy as np

# gini impurity calc - how homogenous is the class
def gini_impurity(y):
	impurity = 1
	classes = np.unique(y)
	for cls in classes:
		p = np.sum(cls == y) / len(y)
		impurity -= p ** 2
	return impurity

# split data set based on threshold and feature
def split_dataset(x, y, threshold, feature):
	left_map = x[:,feature] <= threshold
	right_map = x[:,feature] > threshold
	return x[left_map], x[right_map], y[left_map], y[right_map]

# return best feature and threshold
def best_split(x, y):
	best_feature = None
	best_threshold = None
	best_gini = float("inf")

	# extract rows and columns
	n_samples, n_features = x.shape
	# extract column and threshold (value in each column)
	for feature in range(n_features):
		thresholds = x[:, feature]
		for threshold in thresholds:
			# feed valued into split database function
			x_left, x_right, y_left, y_right = split_dataset(x,y,threshold,feature)
			# if yleft or yright are empty, skip and continue search
			if len(y_left) == 0 or len(y_right) == 0 :
				continue

			# find gini impurtiy of left and right
			left_gini = gini_impurity(y_left)
			right_gini = gini_impurity(y_right)

			# weighted gini - give  more significance to larger classes found in left anf right
			weighted_gini = (len(y_left) / n_samples * left_gini) + (len(y_right) / n_samples * right_gini)

			# replace best gini with weighted gini if it is more pure/homogenous
			if weighted_gini < best_gini:
				best_gini = weighted_gini
				best_threshold = threshold
				best_feature = feature

	return best_feature, best_threshold

# recursively build tree
def build_tree(x, y, depth=0, max_depth=5):
	# stop conditions:
	# pure node
	if len(np.unique(y)) == 1:
		return y[0]
	# reached max depth
	if depth >= max_depth:
		return np.bincount(y).argmax()
	# no valid split - e.g. all features are the same (puts values into one side and leave othersie empty)
	feature, threshold = best_split(x,y)
	if feature == None:
		return np.bincount(y).argmax()

	# split data set
	x_left, x_right, y_left, y_right = split_dataset(x, y, threshold, feature)

	# return node, and call data split recursively using build tree, on right and left
	return {
		"threshold" : threshold,
		"feature" : feature,
		"left" : build_tree(x_left, y_left, depth + 1, max_depth),
		"right" : build_tree(x_right, y_right, depth + 1, max_depth)
	}

# prediction
def predict_one(sample, tree):
	# return leaf node if dictionary is not given
	if not isinstance(tree, dict):
		return tree

	# unpack model
	threshold = tree["threshold"]
	feature = tree["feature"]

	# predict using built tree
	if sample[feature] <= threshold:
		return predict_one(sample, tree["left"])
	else:
		return predict_one(sample, tree["right"])

def predict(x, tree):
	return np.array([predict_one(sample,tree) for sample in x])

#========================#
# create model and apply
#=======================#
# e.g.
# x = ([1,2],[3,4],[5,4],[1,2])
# y = [1,0,0,1]
# tree = build_tree(x,y)
# prediction = predict(x, tree)
# print("predictions: ", prediction)
