import pandas as pd
import numpy as np
import phe as paillier
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn.metrics import mean_squared_error, r2_score

class LinModel:
	def __init__(self):
		pass

	def model(self):
		df=pd.read_csv('mental_health_relapse_risk_dataset.csv')
		df=df.drop('patient_id',axis=1)
		y=df['mental_health_relapse_risk_score']
		X=df.drop('mental_health_relapse_risk_score',axis=1)
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
		reg = LinearRegression().fit(X_train, y_train)
		y_pred=reg.predict(X_test)
		RMSE=pow(mean_squared_error(y_pred, y_test),0.5)
		R=r2_score(y_pred, y_test)
		print("RMSE:", RMSE)
		print("R^2:", R)	
		return reg, y_pred, RMSE, R

	def getCoef(self):
		return self.model()[0].coef_


def main():
	cof=LinModel().getCoef()
	print(cof)


if __name__=='__main__':
	main()