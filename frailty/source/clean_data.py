import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/sava-stew/Principles-of-Data-Science-Assignment1/refs/heads/main/Frailty.csv')

clean_data = df.copy()

#omits participants that should have frailty based on grip strength alone
#grip strength of < 20 should signify frailty in females
clean_data.drop((clean_data[(clean_data['Grip Strength'] < 20)].index), inplace = True)

clean_data.to_csv('clean_data.csv', index=False)