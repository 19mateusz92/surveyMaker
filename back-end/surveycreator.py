import status

def create(nodes, links):
    outputHtml = ''

    for questKey in nodes:
        quest = nodes[questKey]
        if status.QUEST == quest.status:
            outputHtml += createQuestion(quest.question)
            outputHtml += createRadio(questKey, 'Tak')
            outputHtml += createRadio(questKey, 'Nie')

            subquests = findSubquests(questKey, nodes, links)
            for subquest in subquests:
                outputHtml += createQuestion(subquest)
                outputHtml += createNumberInput(questKey)
 
            outputHtml += "<br>"

    return outputHtml

def findSubquests(key, nodes, links):
    subquests = []
    try:
        childKeys = links[key]
        for childKey in childKeys:
            childNode = nodes[childKey]
            if status.EXTRA_QUEST == childNode.status:
                subquests.append(childNode.question)
    except:
        pass

    return subquests

def createQuestion(value):
    return "<p>" + value + "</p>"

def createRadio(key, value):
    return '<input name=\"answer%s\" value=\"%s\" type=\"radio\"/>%s <br>' % (key, value, value)

def createNumberInput(key):
    return '<input name=\"answer%s\" type=\"number\"/> <br>' % (key)
