#include<stdio.h>

//LIFO freelist macros
//Reference to the next entry is stored at the head of the entry,
//so entries must be larger than pointer size

//Freelist type definition: an alias of void**
typedef void** freelist_t;
//Initialize
#define freelist_init(fl) \
{fl=NULL;}
//Push "data" in a freelist as a new entry
#define freelist_push(fl,data) \
{\
	void **tmp_ptr=(void**)data;\
	*tmp_ptr=(void*)fl;\
	fl=tmp_ptr;\
}
//Pop one entry and store in "ret", or NULL if the freelist is empty
#define freelist_pop(fl,ret) \
{\
	if (fl){\
		void **tmp;\
		tmp=fl;\
		ret=(void*)fl;\
		fl=*tmp;\
	}\
	else{ret=NULL;}\
}

struct fl_entry {
    void *next;
    void *data;
};

int main()
{
    freelist_t fl;
    freelist_init(fl);

    char *s1 = "abc";
    struct fl_entry e1;
    e1.next = (void *)0;
    e1.data = s1;
    char *s2 = "def";
    struct fl_entry e2;
    e2.next = (void *)0;
    e2.data = s2;
    char *s3 = "ghi";
    struct fl_entry e3;
    e3.next = (void *)0;
    e3.data = s3;

    freelist_push(fl, &e1);
    freelist_push(fl, &e2);
    freelist_push(fl, &e3);

    struct fl_entry *ret;
    freelist_pop(fl, ret);
    printf("%s\n", ret->data);
    freelist_pop(fl, ret);
    printf("%s\n", ret->data);
    freelist_pop(fl, ret);
    printf("%s\n", ret->data);

    return 0;
}
