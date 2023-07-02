#!/usr/bin/env python
# coding: utf-8

# ## # Introduction
# <p><img src="https://i.imgur.com/kjWF1So.jpg" alt="Different characters on a computer screen"></p>
# <p>According to a 2019 <a href="https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/PasswordCheckup-HarrisPoll-InfographicFINAL.pdf">Google / Harris Poll</a>, 24% of Americans have used common passwords, like <code>abc123</code>, <code>Password</code>, and <code>Admin</code>. Even more concerning, 59% of Americans have incorporated personal information, such as their name or birthday, into their password. This makes it unsurprising that 4 in 10 Americans have had their personal information compromised online. Passwords with commonly used phrases and personal information makes cracking a password drastically easier.</p>
# <p>You may have noticed over the years that password requirements have increased in complexity, including recommendations to change your passwords every couple of months. Compiled from industry recommendations, below is a list of passwords requirements you will be asked to test: </p>
# <p><strong>Password Requirments:</strong></p>
# <ol>
# <li>Must be at least 10 characters in length</li>
# <li>Must contain at least:<ul>
# <li>one lower case letter </li>
# <li>one upper case letter </li>
# <li>one numeric character </li>
# <li>one non-alphanumeric character</li></ul></li>
# <li>Must not contain the phrase <code>password</code> (case insensitive)</li>
# <li>Must not contain the user's first or last name, e.g., if the user's name is <code>John Smith</code>, then <code>SmItH876!</code> is not a valid password.</li>
# </ol>
# <p>Here is the dataset that you will investigate this project:</p>
# <div style="background-color: #ebf4f7; color: #595959; text-align:left; vertical-align: middle; padding: 15px 25px 15px 25px; line-height: 1.6;">
#     <div style="font-size:20px"><b>datasets/logins.csv</b></div>
# Each row represents a login credential. There are no missing values and you can consider the dataset "clean".
# <ul>
#     <li><b>id:</b> the user's unique ID.</li>
#     <li><b>username:</b> the username with the format {firstname}.{lastname}.</li>
#     <li><b>password:</b> the password that may or may not meet the requirements. <i>Note, passwords should never be saved in plaintext, always encrypt them when working with real live passwords!</i></li>
# </ul>
# </div>
# <p>Warning: This dataset contains some <strong>real</strong> passwords leaked from <strong>real</strong> websites. These passwords have been filtered, but may still include words that are explicit and offensive.</p>
# <p>From here on out, it will be your task to explore and manipulate the existing data until you can answer the two questions described in the instructions panel. Feel free to import as many packages as you need to complete your task, and add cells as necessary. Finally, remember that you are only tested on your answer, not on the methods you use to arrive at the answer!</p>
# <p><strong>Note:</strong> To complete this project, you need to know how to manipulate strings in pandas DataFrames and be familiar with regular expressions. Before starting this project we recommend that you have completed the following courses: <a href="https://learn.datacamp.com/courses/data-cleaning-in-python">Data Cleaning in Python</a> and <a href="https://learn.datacamp.com/courses/regular-expressions-in-python">Regular Expressions in Python</a>.</p>

# In[2]:


# Imports
import pandas as pd

#Creating the dataframe
df = pd.read_csv("datasets/logins.csv")

#Functions
def bad_password(username, password):
    rules = [lambda password: len(password) >= 10,
             lambda password: any(letter.isupper() for letter in password),
             lambda password: any(letter.islower() for letter in password),
             lambda password: any(letter.isdigit() for letter in password),
             lambda password: not all(letter.isalnum() for letter in password),
             lambda password: "password" not in password.lower(),
             lambda password: username.split('.')[0].lower() not in password.lower() ,
             lambda password: username.split('.')[1].lower() not in password.lower()]
    
    if all(rule(password) for rule in rules):
        return False
    else:
        return True

# Main
df['bad password'] = df.apply(lambda df: bad_password(df.username, df.password), axis = 1)


# Test 1: What percentage of users have invalid passwords?
bad_pass = round(len(df[df['bad password'] == True].index)/len(df.index), 2)

# Test 2: Which users need to change their passwords?
email_list = df[df["bad password"] == True]['username'].sort_values()

