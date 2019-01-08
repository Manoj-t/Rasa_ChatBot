from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

interpreter = RasaNLUInterpreter('models/current/nlu')
agent = Agent.load('models/dialogue', interpreter=interpreter)

print("Your bot is ready to talk! Type your messages here or send 'stop'")

def proc(text):
    st=""
    for word in range(len(text)):
        if word!=len(text)-1:
            st=st+text[word]+" "
        else:
            st=st+text[word]
    print("ok\n")
    return st


while True:
    a = input()
    k=a.split()
    a=proc(k)
    if a == 'stop':
        break
    responses = agent.handle_message(a)
    for response in responses:
        print(response["text"])
        
