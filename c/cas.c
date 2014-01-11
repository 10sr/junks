/* gcc compare and swap test */

/* type __sync_val_compare_and_swap (type *ptr, type oldval, type newval) */
/* pseudo code: <http://en.wikipedia.org/wiki/Compare-and-swap>
   int cas(int* reg, int oldval, int newval) 
   {
       ATOMIC();
       int old_reg_val = *reg;
       if (old_reg_val == oldval)
           *reg = newval;
       END_ATOMIC();
       return old_reg_val;
   }
*/
#define cas __sync_val_compare_and_swap

#include<stdio.h>

int main(int argc, char **argv)
{
    int a;
    int r;

    a = 1;
    r = cas(&a, 1, 0);
    /* swapped. a == 0, r == 1 */
    printf("a == %d, r == %d\n", a, r);

    a = 1;
    r = cas(&a, 0, 2);
    /* not swapped. a == 1, r == 1 */
    printf("a == %d, r == %d\n", a, r);

    return 0;
}
