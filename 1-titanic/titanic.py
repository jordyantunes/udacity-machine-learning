import numpy as np
import pandas as pd


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. """
    
    # Ensure that the number of predictions matches number of outcomes
    if len(truth) == len(pred): 
        
        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)
    
    else:
        return "Number of predictions does not match number of outcomes!"

def predictions_3(data):
    
    predictions = []
    for _, passenger in data.iterrows():
    	# some super ugly nested ifs, it does give the idea of a decision tree though
        if passenger['Sex'] == 'female' :
            if passenger['Pclass'] == 3 :
                if passenger['SibSp'] > 2 :
                    predictions.append(0)
                else :
                    predictions.append(1)
            else :
                predictions.append(1)
        elif passenger['Age'] < 10:
            predictions.append(1)
        else : 
            predictions.append(0)
    
    # Return our predictions
    return pd.Series(predictions)

def main():
	in_file = 'titanic_data.csv'
	full_data = pd.read_csv(in_file)

	outcomes = full_data['Survived']
	data = full_data.drop('Survived', axis = 1)

	predictions = predictions_3(data) 
	print accuracy_score(outcomes, predictions)

if __name__ == '__main__':
	main()