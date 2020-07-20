import random

# return responses based on kewords

def chatResponse(userMessage):

  num = random.randint(0, 10)

  responses= {
    "greetings": {
      0: "Hey how are you?",
      1: "Bonjour",
      2: "Ciao",
      3: "Hello",
      4: "Hi",
      5: "Good morning",
      6: "Good afternoon",
      7: "Good evening",
      8: "Nihao",
      9: "Nice to meet you",
      10: "It's a pleasure to meet you"
       
    },
    
    "farewells": {
      0: "Bye",
      1: "Au revoir",
      2: "Goodbye",
      3: "See you later",
      4: "Later",
      5: "See you tomorrow",
      6: "I'm off",
      7: "Have a good day",
      8: "Bye Bye",
      9: "It was nice to meet you",
      10: "Peace out"
    },

    "wasteFacts": {
      0: "About one-third of an average dump is made up of packaging material!",
     1: "Every year, each American throws out about 1,200 pounds of organic garbage that can be composted.",
      2: "The U.S. is the #1 trash-producing country in the world at 1,609 pounds per person per year. This means that 5% of the world's people generate 40% of the world's waste.",
      3: "The highest point in Hamilton County, Ohio (near Cincinnati) is Mount Rumpke. It is actually a mountain of trash at the Rumpke sanitary landfill towering 1045 ft. above sea level.",
      4: "The US population discards each year 16,000,000,000 diapers, 1,600,000,000 pens, 2,000,000,000 razor blades, 220,000,000 car tires, and enough aluminum to rebuild the US commercial air fleet four times over.",
      5: "Out of every $10 spent buying things, $1 (10%) goes for packaging that is thrown away. Packaging represents about 65% of household trash.",
      6: "On average, it costs $30 per ton to recycle trash, $50 to send it to the landfill, and $65 to $75 to incinerate it.",
      7: "At Christmas, as much as 83 square kilometres of wrapping paper will end up in UK bins when it could have been recycled instead. That’s the same size as Sunderland!",
      8: "Humans now buy a million plastic bottles a minute. Most of this plastic ends up in the ocean. By 2050, the ocean will contain more plastic by weight than fish.",
      9: "Waste causes greenhouse gas emissions.",
      10: "A single leaky tap in your house can waste as much as 5,000 litres of water a year. "
    },

    "generalEnviormental": {
      0: "Recycling one aluminum can saves enough energy to run a TV for three hours.",
      1: "An aluminum can may be recycled ad infinitum (forever!)",
      2: "We consume over 80 trillion aluminum cans every year.",
      3: "The amount of water on Earth is constant, and continually recycled over time: some of the water you drink will have passed through a dinosaur.",
      4: "There are more than 1,200 species of bat in the world and not one of them is blind.",
      5: "40 percent of all bottled water sold in the world is bottled tap water.",
      6: "Paper can be recycled only six times. After that, the fibers are too weak to hold together.",
      7: "There is no known scientific way of predicting earthquakes. The most reliable method is to count the number of missing cats in the local paper: if it trebles, an earthquake is imminent.",
      8: "Beavers have transparent eyelids so they can see underwater with their eyes shut.",
      9: "The 100,000 trillion ants in the world weigh about the same as all human beings.",
      10: "As soon as tiger shark embryos develop teeth they attack and eat each other in the womb.",
    }
  }

  # All have to be lowercase for comparison
  greets = ["hello", "hi", "hey"]
  bye = ["bye", "see you", "goodbye"]
  waste = ["fact", "waste", "trash"]
  general = ["fact", "earth", "environment"]
  
  for i in greets:
    if userMessage.find(i) >=0:
      return responses['greetings'][num]
  
  for i in bye:
    if userMessage.find(i) >=0:
      return responses['farewells'][num]

  for i in waste:
    if userMessage.find(i) >=0:
      return responses['wasteFacts'][num]
  
  for i in general:
    if userMessage.find(i) >=0:
      return responses['generalEnviormental'][num]

  return responses['greetings'][num]

