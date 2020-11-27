#include <stdio.h>
int mod(int a){
    if (a>=0){
        return a;
    } else {
        return -a;
    }
}
void update(int *a,int *b) {
    int temp = *a;
    (*a) = (*a) + (*b);
    (*b) = mod(temp - (*b));
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
