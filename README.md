Goal

Create a genetic algroithm that finds a match for a target ASCII text (i.e., a string) starting with a population of
random ASCII characters.

Specifics

When the program starts, the program should prompt the user for the name of a plain text file containing the target
text. The complete text in this file is the target. You are welcome to have the program to use a default textfile if
the user does not enter a filename.
The program should construct a population of random individuals composed of all possible basic ASCII characters
(values 0 to 255). Each individual should have the same number of genes as the target has characters.
Using crossover and mutation, the program should evolve the starting population until the best fit of a generation
matches the text exactly.
While the program is running, the program should print out the fitness value of the best individual from each
generation. At first it might help to print out the actual string so you can see the evolution. In the final version, it
should just print the fitness.
When the program finishes, it should print the final best individual.
All aspects of the program should be written from scratch with the exception of base Python modules.

Fitness function

How will you determine how close an individual is to the target text?

Mutation rate

How often will each gene randomly mutate? And when it does mutate, how does it mutate?

Parents

How many parents come together to create a new child?

Crossover

How are the parent’s genes spliced to create a new child?

Population size

How many individuals are you working with?

Survival rate

How many individuals become parents of the next generation?

Choosing parents

How do you choose parents?

Elitism

Do any parents survive into the next generation?

When to stop.

Genetic algorithms do not cease by themselves. They cease when they have found the global optimum (provided you
know what that is. . . luckily for this problem, we do), when they reach a certain number of generations, or when the
fitness of a population does not improve across enough generations. Consider building in more than one stopping point.