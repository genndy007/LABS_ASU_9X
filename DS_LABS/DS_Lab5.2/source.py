def main():
    algo = input("Choose Bellman-Ford(b) or Johnson(j) algorithm: ")
    while algo != 'b' and algo != 'j':
        print("Try again")
        algo = input("Choose Bellman-Ford(b) or Johnson(j) algorithm: ")
    start_vertex = int(input("Enter your start vertex: "))
    type = input("Display:\n\
    Way to one vertex: 1\n\
    Way to all vertices: 2\n\
    Your choice: ")
    while type != 1 and type != 2:
        print("Try again")
        type = input("Display:\n\
        Way to one vertex: 1\n\
        Way to all vertices: 2\n\
        Your choice: ")
    if 


while input("Enter 'exit' to exit: ") != 'exit':
    main()
