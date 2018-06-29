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
AWS (Amazon Web Service) Lambda is a cloud service thatcan be used to host or run code. Zappa is a tool used to deploy various Python related projects into AWS Lambda.

Setting up Zappa and AWS Lambda is demonstarated in this tutorial: https://developer.amazon.com/blogs/post/8e8ad73a-99e9-4c0f-a7b3-60f92287b0bf/New-Alexa-Tutorial-Deploy-Flask-Ask-Skills-to-AWS-Lambda-with-Zappa
## Flask-Ask
Flask-Ask is a python framework used to write Amazon Alexa Skills. The interactions between the user and the Alexa are written using this.
## Amazon Skills Kit Developer Console
The Amazon Skills Kit Developer Console is where you can build, manage, or test newly created skills. This process of creating and uploading a new skill can be done with 4 steps:
1. Invocation Name
2. Intents/Utterances 
3. Build Model
4. Endpoints

Invocation Name: A name for your custom skill. A name for the skill is needed in order for the Alexa to recognize when to trigger such skill.

Intents/Utterances:

