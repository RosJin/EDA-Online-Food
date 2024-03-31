# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv('../DA Hotel Booking/Data/onlinefoods.csv')

df.head()

df.tail()

df.shape

df.drop(columns='Unnamed: 12', inplace=True)

df.info()

df.columns

df.isnull().sum()

# Data Visualization

plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Age', bins=10, kde=True)
plt.title('Age Distribution of Customer')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.show()

gender_counts = df['Gender'].value_counts()

plt.figure(figsize=(10,6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()

marital_counts = df['Marital Status'].value_counts()

plt.figure(figsize=(10,6))
marital_counts.plot(kind='bar', color='skyblue')
plt.xlabel('Marital Status')
plt.ylabel('Count')
plt.title('Marital Status Distribution')
plt.xticks(rotation=45)
plt.show()

occupation_counts = df['Occupation'].value_counts().reset_index()
occupation_counts.columns = ['Occupation', 'Count']

occupation_counts = occupation_counts.sort_values(by='Count', ascending=False)

plt.figure(figsize=(10, 6))
plt.bar(occupation_counts['Occupation'], occupation_counts['Count'], color='skyblue')
plt.xlabel('Occupation')
plt.ylabel('Count')
plt.title('Distribution of Customers by Occupation')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(df['Monthly Income'], bins=20, kde=True)
plt.title('Distribution of Monthly Incomes')
plt.xlabel('Monthly Income')
plt.ylabel('Frequency')
plt.show()

education_counts = df['Educational Qualifications'].value_counts()

plt.figure(figsize=(10, 6))
education_counts.plot(kind='bar', color='skyblue')
plt.title('Distribution of Customers by Educational Qualifications')
plt.xlabel('Educational Qualifications')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.show()

family_size_counts = df['Family size'].value_counts()
plt.figure(figsize=(4, 4))
plt.pie(family_size_counts, labels=family_size_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Customers by Family Size (Pie Chart)')
plt.show()

feedback_counts = df['Feedback'].value_counts()

plt.figure(figsize=(6, 4))
sns.countplot(x='Feedback', data=df)
plt.title('Distribution of Feedback')
plt.xlabel('Feedback')
plt.ylabel('Count')
plt.show()