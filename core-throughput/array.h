#ifndef _ARRAY_H
#define _ARRAY_H

/* Return 0 if two array are same. */
int CheckArray(unsigned char *a1, unsigned char *a2, int len);

/* Print array in a pretty way. */
void PrintArray(unsigned char *array, int len);

/* Initialize array data with random char. */
void InitArray(unsigned char *array, int len);

#endif  /* _ARRAY_H */
