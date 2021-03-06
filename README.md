# Amazon-Alexa-Schoology-project
The goal of this project is to create a Schoology skill for the Amazon Alexa/Echo. This skill would allow the user to ask the Amazon Alexa about upcoming assignments on various days. It would be able to access information from Schoology and relay it back to the user.
## Sections:
1. Zappa + AWS Lambda
2. Flask-Ask
3. Amazon Skills Kit Developer Console
4. Selenium
5. Boto3
6. Cronjob
## Zappa + AWS Lambda
AWS (Amazon Web Service) Lambda is a cloud service that can be used to host or run code. Zappa is a tool used to deploy various Python related projects into AWS Lambda.

Setting up Zappa and AWS Lambda is demonstarated in this tutorial: https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/New-Alexa-Tutorial-Deploy-Flask-Ask-Skills-to-AWS-Lambda-with-Zappa
## Flask-Ask
Flask-Ask is a python framework used to write Amazon Alexa Skills. The interactions between the user and the Alexa are written using this. We will be using Zappa to deploy this python project.
## Amazon Skills Kit Developer Console
The Amazon Skills Kit Developer Console is where you can build, manage, or test newly created skills. Accessing this interface is also done in the tutorial under Zappa + AWS Lambda. The process of creating and uploading a new skill can be done with 4 steps:
1. Invocation Name
2. Intents/Utterances 
3. Build Model
4. Endpoints

Invocation Name: A name for your custom skill. A name for the skill is needed in order for the Alexa to recognize when to trigger such skill.

Intents/Utterances: An intent is a specific action the you want to achieve with the skill. Utterances are what triggers the action to be played. For this project, the intent would be searching for an assignment on a particular day. An example utterance would be, "What do I have on Monday?"

Build Model: Builds the current version of your skill. Whenever a change is made, you must re-build the model.

Endpoints: An url that points to the server that performs the skill. The url is generated through Zappa.
## Selenium
Selenium is a Python package that can simulate the the process of web browsing and data extraction. Using this package, we can simulate the process of logging on to Schoology and finding upcoming assignments. If written as a non-headless version, you can see the process of Selenium going through the various steps through a browser window. If written as a headless version, no browser window will be shown.

We can use Selenium to collect the assignments for each particular day.

In order for this to work, the proper Schoology link as well as the username and password must be suplied to the Selenium file.

## Boto3
Boto3 is a Python package that allows information to be stored in S3 (Simple Cloud Storage System). This acts as a database where we can store the inforamtion collected from selenium. 

We can then use Boto3 in our Flask-Ask program to retrieve the stored assignments.

## Cronjob
Cronjob is a Unix utility that can be used to schedule a job to run at periodic intervals. Since assignments are constantly updated, having a separate server that can run the Selenium file on its own would be beneficial.

