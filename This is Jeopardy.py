# This is Jeopardy Project - Zack Nguyen
import pandas as pd

# Display full contents of a column.
pd.set_option('display.max_colwidth', None)

# Reading the CSV and investigating.
jp = pd.read_csv('jeopardy.csv')
#print(jp.columns)

# Fixing column names.
jp.rename(columns={'Show Number': 'show number', ' Air Date': 'air date', ' Round': 'round', ' Category': 'category', ' Value': 'value', ' Answer': 'answer', ' Question': 'question'},inplace=True)
print(jp.columns)
print(jp['question'])

# Creating a function that filters dataset for questions taht contains all of the words in a list of words.
def question_in_list(data, words):
    # Lowercases all words in the list of words as well as the questions. Returns true if all of the words in the list appear in the question.
    filter = lambda x: all(word.lower() in x.lower() for word in words)
    # apply lambda func to Question column and returns the rows where the function returned True.
    return data.loc[data['question'].apply(filter)]

# Test
filtered = question_in_list(jp, ['King', 'England'])
print(filtered['question'])

# Test 2
words = ['king']
filtered2 = question_in_list(jp, words)
print(filtered2['question'])

# Adjusting column so that we can compute the mean of the "Value" column.
# Adding a new column. If the value of the float column is not "None", then we cut off the first character (which is a dollar sign), and replace all commas with nothing, and then cast that value to a float. If the answer was "None", then we just enter a 0.
jp['value'] = jp['value'].replace('None', 0)
jp['new values'] = jp['value'].str.replace('\$|','', regex= True)
jp['new values'] = jp['new values'].str.replace(',', '')
jp['new values'] = jp['new values'].astype(float)

# Filtering the dataset and finding the average value of those questions.
filtered2 = question_in_list(jp, ["King"])
print(filtered2['new values'].mean()) 

# Find the unique answers and count them.
def unique_ans(data):
    return data['answer'].value_counts()

print(unique_ans(filtered2))