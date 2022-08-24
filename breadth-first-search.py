from collections import deque


graph = {}

graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anju","peggy"]
graph["alice"] = ['peggy']
graph["claire"] = ['thom','jonny']
graph["anju"] = []
graph["peggy"] = []
graph["thome"] =[]
graph["jonny"] = []

def person_is_seller(name):
    return name[-1] == 'm'
def search(name):
    search_queue=deque();
    search_queue += graph[name];
    serched = [];
    while search_queue:
        person = search_queue.popleft();
        if not person in serched:
            if person_is_seller(person):
                print(person+" is a seller")
                return True;
            else:
                search_queue += graph[person]
                serched.append(person)
    return False;
search("you");