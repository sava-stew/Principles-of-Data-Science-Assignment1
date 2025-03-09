import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

df = pd.read_csv('https://raw.githubusercontent.com/sava-stew/Principles-of-Data-Science-Assignment1/refs/heads/main/student_performance/data_raw/StudentsPerformance.csv')


#lunch_free_math_scores.png and lunch_standard_math_scores.png allow for easier analysis of if a participant's lunch payment status has an impact on their math scores
#creates a histogram that represents the frequency of math scores for those with free/reduced lunch
lunchFree = df.copy()
lunchFree.drop(lunchFree[lunchFree['lunch'] == 'standard'].index, inplace=True)
lunchFree['math score'].plot.hist(title = 'Free/Reduced Lunch Math Scores', xlabel = 'Percentage', ylabel='Frequency', bins = 50)
plt.savefig('lunch_free_math_scores.png')
plt.close()

#creates a histogram that represents the frequency of math scores for those with standard lunch
lunchStandard = df.copy()
lunchStandard.drop(lunchStandard[lunchStandard['lunch'] == 'free/reduced'].index, inplace=True)
lunchStandard['math score'].plot.hist(title = 'Standard Lunch Math Scores', xlabel = 'Percentage', ylabel = 'Frequency', bins=50)
plt.savefig('lunch_standard_math_scores.png')
plt.close()


#parentEd_on_writing_scores.png allows for easier analysis of if higher or lower average writing scores and correlated to different levels of parental education
#creates a bar graph that represents the correlation between writing scores and parental level of education
parentEd = df.groupby('parental level of education')
parentEd['writing score'].mean().plot.bar(title = 'Parent Education on Writing Scores', ylabel = 'Average Score')
plt.tight_layout()
plt.savefig('parentEd_on_writing_scores.png')
plt.close()


#test_scores_by_gender.png allows for easier analysis of if there is a trend in test score density due to gender across different subjects
#creates a series of density graphs that represent the density of different scores by gender
gender = df.groupby('gender')
plt.subplot(3, 1, 1)
gender['math score'].plot.kde(title = 'Math Scores by Gender', xlabel='Scores')
plt.subplot(3, 1, 2)
gender['reading score'].plot.kde(title = 'Reading Scores by Gender', xlabel='Scores')
plt.subplot(3, 1, 3)
gender['writing score'].plot.kde(title = 'Writing Scores by Gender', xlabel='Scores')
plt.legend()
plt.tight_layout()
plt.savefig('test_scores_by_gender.png')
plt.close()


#test_prep_on_averages.png allows for easier analysis of if there is a correlation between completeted test prep and higher or lower score averages across subjects
#creates a bar graph that represents the correlation between test prep completion and average test scores across subjects
testPrep = df.groupby('test preparation course')
mathMean = testPrep['math score'].mean()
readingMean = testPrep['reading score'].mean()
writingMean = testPrep['writing score'].mean()
data = {'Math Average': mathMean, 'Reading Average': readingMean, 'Writing Average': writingMean}
averages = pd.DataFrame(data)
averages.plot.bar(title = 'Test Prep on Average Scores', xlabel = 'test prep completion', ylabel = 'Average Score')
plt.tight_layout()
plt.savefig('test_prep_on_averages.png')
plt.close()


#parent_education_and_test_prep.png allows for easier analysis of if there is a correlation between parental education and completed test preparation
#creates bar graph that represents the frequency of correlation between parental education and completed test preparation
parentEd  = df.groupby('parental level of education')
parentEdPrep = parentEd['test preparation course'].value_counts()
parentEdPrep.plot.bar(title = 'Parent Education and Test Preparation', xlabel = 'Parent Education and Test Prep Completion')
plt.tight_layout()
plt.savefig('parent_education_and_test_prep.png')
plt.close()
