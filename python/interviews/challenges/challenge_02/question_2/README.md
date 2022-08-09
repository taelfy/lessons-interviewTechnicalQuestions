## Question 2
### Create a simple linear regression model

You will find the original files for this question in `raw` directory.

You will have to fill in the gaps in the `SimpleLinearRegression` class so that the code will run successfully.
   
The following functions need to be filled:

-  `__loss`: This function defines the loss function of your choice.
-  `__sgd`: We will use the Stochastic Gradient Descent Algorithm to optimise the slope and the intercept of our linear function. There are many resources online about SGD, However
the most important formulas are :
    
![img.png](img.png) 

Where `n`is the number of sample in the training dataset. 

Do your best to vectorize the formulas.

-  `__predict`our linear function to predict the outcome. The function of a simple line is defined as `y= wX + b`

We have provided the benchmark code `benchmark.py`. Execute it and you should get the Coefficient of determination around `0.42`.
A good implementation should return about the same Coefficient of determination or slightly higher. During the interview we could explore the time and memory complexity of your code. 

**PS: If you are struggling implementing the above, consider using scikit-learn to progress to the next stages (but this is not encouraged).**

## Solution

1. Go to `./question_2` directory to set as root directory.
2. Run `python simple_linear_regr.py` to see the result.
3. Run `python benchmark.py` to see the benchmark.