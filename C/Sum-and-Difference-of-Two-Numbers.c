#include<stdio.h>

int main(void){
    int a, b;
    float c, d;

    scanf("%d %d", &a, &b);
    scanf("%f %f", &c, &d);

    printf("%d %d\n", a+b, a-b);
    printf("%.1f %.1f", c+d, c-d);
}
