import nltk


'''
print("Read your daily article and press the button when done")
article = scrape_article()
display_article(article)
questions = generate_questions(article, 3)
'''

questions = {
    "Hello, how are you?",
    "Tell me more about {}"
    }

responses = []
i = 0
for question in questions:
    response = input(question)
    responses.append(response)
    # correct_grammar(response)

print(responses)

'''
# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(lines)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 
print nouns
'''

# >>> ['lines', 'string', 'words']
