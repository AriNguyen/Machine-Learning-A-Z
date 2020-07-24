# Data Processing

# Importing the dataset
dataset = read.csv('Data.csv')
#   take subset of dataset
# dataset = dataset[, 2:3]

# Taking care of missing data
#   take column Age of the dataset
#   ifelse: condition, return if True, return if False
#   is.na: function tells if value is missing or not
dataset$Age = ifelse(is.na(dataset$Age),
                     ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary),
                     ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                     dataset$Salary)

# Encoding categorial data
#   factor: function that 
#   first argument: data that want to tranforms into vector
#   second arguemnt: levels: name of categories in Country column
#   c: create vector of 3 elements
#   third argument: label: choose which number give to F, S, G
dataset$Country = factor(dataset$Country,
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))
dataset$Purchased = factor(dataset$Purchased,
                         levels = c('No', 'Yes'),
                         labels = c(0, 1))

# Splitting the dataset into Training set and Test set
# install.packages('caTools')
# .split: return True or False fro each of your observation:
# True if go to trainign set, False if go to Test Set
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)

# Feature Scaling
training_set[, 2:3] = scale(training_set[, 2:3])
test_set[, 2:3] = scale(test_set[, 2:3])






