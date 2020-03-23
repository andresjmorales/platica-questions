import speech_recognition as sr
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')


'''
print("Read your daily article and press the button when done")
article = scrape_article()
display_article(article)
questions = generate_questions(article, 3)
'''

'''
questions = {
    "Hello, how are you? {}",
    "What is the best thing that happened to you today? {} ",
    "Tell me more about {}, that sounds interesting "
    }
'''

questions = open("questions.txt").readlines()
print(questions)

is_noun = lambda pos: pos[:2] == 'NN'
responses = [""]
first_nouns = [""]

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak anything: ")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
    except:
        print("Could not recognize your voice.")
        
        
        
        

i = 0
for question in questions:
    if '{}' in question:
        if not first_nouns:
            question.format(responses[-1])
        else:
            question = question.format(first_nouns[-1])
        
    response = input(question)
    responses.append(response)
    
    tokenized = nltk.word_tokenize(response)
    nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
    if nouns: first_nouns.append(nouns[0])
    
    print(responses)
    print(nouns)
    print(first_nouns)
    
    i += 1
    # correct_grammar(response)

print(responses)
