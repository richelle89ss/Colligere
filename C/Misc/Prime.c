#include <stdio.h>

int isPrime(int x) {
    if (x == 1)
        return 0;
    if (x % 2 == 0)
        return 0;
    for (int i = 3; i < x; i++) { // May replace x with sqrt(x)
        if (x%i == 0)
            return 0;
    }
    return 1;
    
}

int main() {
    int a;
    printf("Input a number to see if it is a prime number:\n");
    scanf("%d", &a);
    if (isPrime(a))
        printf("%d is a prime number.\n", a);
    else
        printf("%d is not a prime number.\n", a);
    return 0;
}
