#include <iostream>
#include <stdlib.h>
#include <vector>

const int SIEVE_COUNT = 10000;

//slow version
int main(){
    //sieve of eratosthenes from 1 to SIEVE_COUNT
    std::vector<bool> primes(SIEVE_COUNT, true);
    primes[0] = false;
    primes[1] = false;

    //iterate through primes
    for (int i = 2; i*i < SIEVE_COUNT; i++){
        //if the number is prime, set all it's multiples to non-prime(false)
        if (primes[i]){
            //set all multiples to nonprime
            //inefficient version
            for (int j = i; j*i < SIEVE_COUNT; j++){
                primes[j*i] = false;
            }
        }
    }

    //print primes
    for (int i = 0; i < SIEVE_COUNT; i++){
        if (primes[i]){
            std::cout << i << " ";
        }
    }
}