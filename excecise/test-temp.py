from temp import AnnoymousSurvey

question='Which language do you speak?'
my_survey=AnnoymousSurvey(question)

my_survey.show_question()
print('Enter "q" at any time to quit\n')
while True:
    response=input("language:")
    if response=="q":
        break
    my_survey.store_response(response)

print('\nThank you to everyone who participated in this survey!')
my_survey.show_results()