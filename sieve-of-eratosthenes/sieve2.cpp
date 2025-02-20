#include <iostream>
#include <stdlib.h>
#include <vector>

const int SIEVE_COUNT = 1000;

//faster version
int main(){
    //sieve of eratosthenes from 1 to 1000
    std::vector<bool> primes(SIEVE_COUNT, true);
    primes[0] = false;
    primes[1] = false;

    //iterate through primes
    for (int i = 2; i*i < SIEVE_COUNT; i++){
        //if the number is prime, set all it's multiples to non-prime(false)
        if (primes[i]){
            //efficient version
            for (int j = i*i; j < SIEVE_COUNT; j += i){
                primes[j] = false;
            }
        }
    }

    return 0;
}