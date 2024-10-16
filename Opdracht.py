#!/bin/python3
import random
import time

import re


responses = { 
  "Hoe heet je": ["Henk","Klaas","Piet","Hans","Olivier","Oliver","Olievier","Kris","Guo","Zhong"],
  "hoe heet je": ["Henk","Klaas","Piet","Hans","Olivier","Oliver","Olievier","Kris","Guo","Zhong"],
  "Hoe heet je?": ["Henk","Klaas","Piet","Hans","Olivier","Oliver","Olievier","Kris","Guo","Zhong"],
  "hoe heet je?": ["Henk","Klaas","Piet","Hans","Olivier","Oliver","Olievier","Kris","Guo","Zhong"],
  "hallo": ["Hallo", "Hoi", "Bonjour"] ,
  "Hallo": ["Hallo", "Hoi", "Bonjour"] ,
  "Hoe gaat het?": ["Het gaat super en met jouw?","Goed hoor met jouw?"], 
  "hoe gaat het?": ["Het gaat super en met jouw?","Goed hoor met jouw?"], 
  "Hoe gaat het": ["Het gaat super en met jouw?","Goed hoor met jouw?"], 
  "hoe gaat het": ["Het gaat super en met jouw?","Goed hoor met jouw?"], 
  "Goed": ["Mooi zo!", "Fijn om te horen"],
  "Slecht": ["jammer :(", "Balen man"],
  "goed": ["Mooi zo!", "Fijn om te horen"],
  "slecht": ["jammer :(", "Balen"],
  "Prima": ["Oki dokie"],
  "prima": ["Oki dokie"],
  "Stoomlokomotief": ["Kopiëer dit linkje: https://poki.com/nl"],
  "Boe": ["AHHHHHH Ik schrik me dood"],
  "boe": ["AHHHHHH Ik schrik me dood"],
  "BOE": ["AHHHHHH Ik schrik me dood"],
  "BOe": ["AHHHHHH Ik schrik me dood"],
  "BoE": ["AHHHHHH Ik schrik me dood"], 
    }
    
def get_response(message): 
  if message in responses: 
    return(random.choice(responses[message]))
  else: 
    return "Ik snap het je zei " + message 
    
patterns = {
  "ik voel me(.*)":"Waarom voel je je {}?",
  "herinner jij(.*)":"Nutuurlijk hoe kan ik dat vergeten?", 
  "ben je een(.*)":"Ik heb geen identiteit, dus ik ben ook geen {}",
}


while True:
  message = input("Jij:")
  time.sleep(random.randint(1, 4))
  antwoord = get_response(message)
  print(antwoord)

  for pattern in patterns:
    match = re.search(pattern,message)
    if match:
      computer_message = patterns[pattern]
      user_answer = match.group(1)
      print(computer_message.format(user_answer))


