#include<stdio.h>
#define MAX_LEN 100

int main(void){
    char ch, s[MAX_LEN], sen[MAX_LEN];
    scanf("%c", &ch);
    scanf("%s", s);
    scanf("\n");
    scanf("%[^\n]*c", sen);
    
    printf("%c\n", ch);
    printf("%s\n", s);
    printf("%s\n", sen);

}
