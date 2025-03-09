import pandas as pd

data = input('Please input the file path for the cleaned data: ')

clean_data = pd.read_csv(data)

#creates seperate dataframe for participants with frailty
indexYes = clean_data.copy()
indexYes.drop(indexYes[indexYes['Frailty'] == 'N'].index, inplace=True)

#creates separate dataframe for participants without frailty
indexNo = clean_data.copy()
indexNo.drop(indexNo[indexNo['Frailty'] == 'Y'].index, inplace=True)

#find average grip strength of those with frailty
meanYes = indexYes['Grip Strength'].mean()

#find average grip strength of those without frailty
meanNo = indexNo['Grip Strength'].mean()

file = open('venv/results/results.txt', 'w')
file.write(f'Average grip strength among participants with frailty: {meanYes} \n')
file.write(f'Average grip strength among participants without frailty: {meanNo} \n')
file.close()
