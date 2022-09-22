from collections import deque

"Find the shortest path from start to the target word and print it"
def find_shortest_path(start, goal, neighbors_list):

    frontier = deque([start])  # queue of states/words
    previous_state = {start: None}  # associate each word with his previous
    while (frontier):
        state = frontier.popleft()  # delete the current frontier and return her value
        for state2 in neighbors_list[state]:  # find the neighbors of the current word in the frontier
            if state2 not in previous_state:  # assure that this frontier does not be explored
                frontier.append(state2)  # add the word the frontier queue
                previous_state[state2] = state  # associate the current word with his previous

                if state2 == goal:
                    for word in build_path(previous_state, state2):  # return the path to reach the goal
                        print(word)
                    return
    else :
        print("No solution")

"Return a list of words that to reach the starting word, reccurence to create the list until None "
def build_path(previous_list, state):

    return ([] if (state is None) else build_path(previous_list, previous_list[state]) + [state])

"Return the frontier with the zip function who give us pairs of letter to compare"
def find_frontier(word):
    frontier_list = [w for w in list_of_words if sum(a != b for a, b in zip(word, w)) == 1]
    return (set(frontier_list))

"Return a list of words who have the length of the start word"
def create_list_length(filename, start):
    list_of_words = list()
    with open(filename) as f:
        for word in f:
            w = word[0:len(word) - 1]  # word.rstrip()
            if (len(w) == len(start) and w not in list_of_words):
                list_of_words.append(w)
    return (list_of_words)

filename=input('Enter the path of your dictionnary :')
start=input('Enter the starting word :')
target=input('Enter the target word :')

list_of_words=create_list_length(filename,start)
word_neighbors = {word: find_frontier(word) for word in list_of_words}
find_shortest_path(start, target, word_neighbors)

"This algorithm take time because at each new search we build a dictionnary of each word and his neighbors" \
"To improve this algorithm we may download this neighbours dictionnary and use it for the next search"