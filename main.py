from rdflib import Graph
import random

# Load RDF data
g = Graph()
g.parse("food.rdf")
ontologie = ""
lista_ontologii = []

# Extract ontology information
for concept1, relatie, concept2 in g:
    if "#" in concept1 and "#" in relatie and "#" in concept2:
        ontologie += concept1.split("#")[1] + "-" + relatie.split("#")[1] + "-" + concept2.split("#")[1] + "\n"
        lista_ontologii.append([concept1.split("#")[1], relatie.split("#")[1], concept2.split("#")[1]])

# Save ontology information to file
with open("ontologie.txt", "w") as w:
    w.write(ontologie)

# Prepare question data
length_list = len(lista_ontologii)
cuvinte_si_relatii = ""
cuvinte_si_relatii_1 = ""
index = 0
while index < length_list:
    cuvinte_si_relatii += lista_ontologii[index][0] + "\n" + lista_ontologii[index][2]
    cuvinte_si_relatii_1 += lista_ontologii[index][2] + "\n" + lista_ontologii[index][0]
    index1 = 0
    while index1 < length_list:
        if index != index1:
            if lista_ontologii[index][0] == lista_ontologii[index1][0]:
                cuvinte_si_relatii += "," + lista_ontologii[index1][2]
            if lista_ontologii[index][0] == lista_ontologii[index1][2]:
                cuvinte_si_relatii += "," + lista_ontologii[index1][0]
            if lista_ontologii[index][2] == lista_ontologii[index1][0]:
                cuvinte_si_relatii_1 += "," + lista_ontologii[index1][2]
            if lista_ontologii[index][2] == lista_ontologii[index1][2]:
                cuvinte_si_relatii_1 += "," + lista_ontologii[index1][0]
        index1 += 1
    cuvinte_si_relatii += "\n"
    cuvinte_si_relatii_1 += "\n"
    index += 1

    #print("Success")

print("Answer the following questions: \n")

# Generate and ask specific questions
while True:
    n = random.randint(0, len(lista_ontologii) - 1)
    index_question = 0
    index_question1 = 2
    
    question = f"What is the relationship between {lista_ontologii[n][index_question]} and {lista_ontologii[n][index_question1]}? \n"
    print(question)

    answer = input("Your answer: ")
    correct_answer = lista_ontologii[n][1]

    if answer.strip() == correct_answer:
        print("The answer is correct")
    else:
        print(f"The answer is not correct. The correct answer is: {correct_answer}")

    answer_next = input("Shall we move to the next question? If you want to exit, type 'exit' \n")
    if answer_next == "exit":
        break
