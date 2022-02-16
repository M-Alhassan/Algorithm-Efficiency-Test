# Sieve-of-Eratosthenes-Algorithm-Test
A small experiment I did with python to test different types of algorithm's effieciency. Algorithm efficiency plays a vital role in any program specially when dealing with Big Data.


Most common Big Data applications:
- **Goverment:**
Proccess efficiencies in terms of cost, productivity, and innovation without its flaws.
- **Inernational development:**
Research on the effective usage of information and communication technologies for development.
- **Healthcare:**
Track people infected with COVID-19 to minimize the virus' spread.
- **Education**
- **Media**
- **Incurance**

    ...

    and lots more


## ⚙️ Technologies

<img src="https://img.icons8.com/color/48/000000/python--v1.png"/>

## ⚡ Features

-   Allows the user to choose 3 different algorithms with different efficiecies.
- Displays the execution time for each run.

## 💻 Supported operations
-   `Sieve of Eratosthenes`: Uses Sieve of Eratosthenes algorithm to find prime numbers.

Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit. It does so by iteratively marking as composite the multiples of each prime, starting with the first prime number, 2. The multiples of a given prime are generated as a sequence of numbers starting from that prime, with constant difference between them that is equal to that prime.


**Flowchart:**

<img src = "img/Flowchart.png">

Time complexity: O(n*log(log n))

  (most efficient)

<br>

- `nested loops`: calcualtes the total prime numbers using nested loops and modular arithmetic.

Time complexity: O(n)^2

 (less efficient but more accurate)

<br>

- `recursion`: calculates the total prime numbers of a set by itrating throught the came function while incrementing the number each time.

    (Least efficient)

[Note: python supports a limited number of recursive calls, so large numbers do not always work]

Recursion is least efficient since the function has to add to the stack memory with each recursive call and keep the values there until the call is finished, the memory allocation is greater than that of an iterative function.

## 🔧 Installation

1. Install newest version of [Python](https://www.python.org/)
2. Run program

## ✒️ Author

| [<img src="https://github.com/M-Alhassan.png?size=115" width="115"><br><sub>@M-Alhassan</sub>](https://github.com/M-Alhassan) |
| :---------------------------------------------------------------------------------------------------------------------------: |