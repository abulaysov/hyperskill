import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns', 8)

general = pd.read_csv('general.csv')
prenatal = pd.read_csv('prenatal.csv')
sports = pd.read_csv('sports.csv')

sports.rename(columns=({'Hospital': 'hospital', 'Male/female': 'gender'}), inplace=True)
prenatal.rename(columns=({'HOSPITAL': 'hospital', 'Sex': 'gender'}), inplace=True)
df = pd.concat([general, prenatal, sports], ignore_index=True)

df.drop(df.columns[0], 1, inplace=True)

df.dropna(axis=0, how='all', inplace=True)
df.replace({'gender': {'woman': 'f', 'female': 'f', 'male': 'm', 'man': 'm'}}, inplace=True)
df.gender.fillna('f', inplace=True)
df.fillna(0, inplace=True)


"""
print(f'The answer to the 1st question is {df.hospital.value_counts().idxmax()}')

diagnosis_in_general = df.loc[df.hospital == "general", "diagnosis"]
total_stomach = diagnosis_in_general.value_counts().stomach
total_diagnosis = diagnosis_in_general.count()
print(f'The answer to the 2nd question is {round(total_stomach / total_diagnosis, 3)}')


diagnosis_in_sports = df.loc[df.hospital == "sports", "diagnosis"]
total_dislocation = diagnosis_in_sports.value_counts().dislocation
total_diagnosis = diagnosis_in_sports.count()
print(f'The answer to the 3rd question is {round(total_dislocation / total_diagnosis, 3)}')


mean_age_general = df.loc[df.hospital == "general", "age"].mean()
mean_age_sports = df.loc[df.hospital == "sports", "age"].mean()
print(f'The answer to the 4th question is {abs(int(mean_age_sports - mean_age_general))}')


dict_tests = {'general': df.loc[df.hospital == "general", "blood_test"].value_counts().get('t', 0),
              'prenatal': df.loc[df.hospital == "prenatal", "blood_test"].value_counts().get('t', 0),
              'sports': df.loc[df.hospital == "sports", "blood_test"].value_counts().get('t', 0)}

max_test = max(dict_tests, key=lambda x: dict_tests[x])
print(f'The answer to the 5th question is {max_test}, {dict_tests[max_test]} blood tests')

print(df.shape)
print(df.sample(20, random_state=30))
"""

df.plot(y='age', bins=[0, 15, 35, 55, 70], kind='hist')
print('The answer to the 1st question: 15-35')
plt.show()

df['diagnosis'].value_counts().plot(kind='pie')
plt.show()
print('The answer to the 2nd question: pregnancy')

sns.violinplot(x='hospital', y='height', data=df)
plt.show()
print('The answer to the 3rd question: It\'s because athletes are usually bigger.')



