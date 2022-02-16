import time
import sys

def method_1(num):
    numbers = set(range(num, 1, -1))    # all numbers in range (sorted backwards)
    primes = []
    start_time = time.time()
    while numbers:
        p = numbers.pop()   # p = the last element in the numbers list
        primes.append(p)    # p add p to the primes list
        numbers.difference_update(set(range(p*2, num+1, p))) # {numbers} - {(p*2 -> num+1) incremented by p}
    execution_time = time.time() - start_time
    total_numbers = len(primes)
    print("\nresults: ")
    print("The number of primes from 0 to %s is: %s " % (num, total_numbers))
    print("The execution time is: %s seconds" % round(execution_time, 4))

def method_2(num):
    lower = 0
    count = 0
    start_time = time.time()
    for n in range( lower, num + 1):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                count +=1
    execution_time = time.time() - start_time
    total_numbers = count
    print("\nresults: ")
    print("The number of primes from 0 to %s is: %s " % (num, total_numbers))
    print("The execution time is: %s seconds" % round(execution_time, 4))


def CheckPrime(i,n):
    if n==i:
        return 0
    else:
        if(n%i==0):
            return 1
        else:
            return CheckPrime(i+1,n)

def method_3(num):
    ("Number of primes are")
    count = 0
    start_time = time.time()
    for i in range(2, num+1):
     if(CheckPrime(2,i)==0):
         count +=1
    execution_time = time.time() - start_time
    total_numbers = count
    print("\nresults: ")
    print("The number of primes from 0 to %s is: %s " % (num, total_numbers))
    print("The execution time is: %s seconds" % round(execution_time, 4))

while(True):
    print("============================================================")
    num = int(input("Enter a number: "))
    print("\n1. using Eratosthenes' Algorithm (fast)\n2. using nested a loop (slow)\n3. using recursion (slowest) (MAX 20,000)")
    option = input("\nChoose a method: ")
    print("\ncalculating...")
    if option == "1":
       method_1(num)
    elif option == "2":
       method_2(num)
    elif option == "3":
        sys.setrecursionlimit(999999)
        method_3(num)
    else:
       print("unknown input, please choose 1 or 2")
print("============================================================")