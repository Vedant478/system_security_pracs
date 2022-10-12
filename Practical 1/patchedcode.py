#include <stdio.h>
#include <string.h>
  
// Driver code
int main()
{
    char temp[];
    char str[] = "hello";
    strlcpy(temp, str);
    printf("%s", temp);
    return 0;
}
