from configparser import ConfigParser

config = ConfigParser()
config.read("/Users/Documents/PycharmProjects/SurveyMonkey/configfiles/Config_data_file.cfg")

question1= config.get('Question', 'question1')

question2= config.get('Question', 'question2')
question3= config.get('Question', 'question3')
question4= config.get('Question', 'question4')
question5= config.get('Question', 'question5')
question6= config.get('Question', 'question6')
question7= config.get('Question', 'question7')
question8= config.get('Question', 'question8')
question9= config.get('Question', 'question9')
question10= config.get('Question', 'question10')
















question1 = "Enter your email."

question2 = "How often do you use SurveyMonkey?"
q2_value1 = "Regularly"
q2_value2 = "Sometimes"
q2_value3 = "Never Tried"

question3 = "From When are you using SurveyMonkey?"

question4 = "How will rate the ease of survey creation?"

question5 = "Did you get meaningful data from survey analysis?"
q5_visible_text = "Yes - No"

question6 = "Check the Features you like about SurveyMonkey?"
q6_value1 = "Question Bank"
q6_value2 = "Themes"
q6_value3 = "Graphical Result"
q6_value4 = "Template Re-usability"
q6_value5 = "Collectors"

question7 = "Rate our features."
q7_value1 = "Service"
q7_value2 = "Support"
q7_value3 = "Responsiveness"
q7_column1 = "Very Good"
q7_column2 = "Good"
q7_column3 = "Average"
q7_column4 = "Below Average"

question8 = "List the features you like most."
q8_label1 = "Feature Name"
q8_label2 = "Feature Name"
q8_label3 = "Feature Name"

question9 = "Will recommend SurveyMonkey to your friends / Colleagues?"
q9_visible_text = "Yes - No"

question10 = "Comments / Feedback"
