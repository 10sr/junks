public class AClass{
    int a;
    // static var is shared among instances
    static int s;

    static{
        AClass.s = 1;
    }

    // met of same name as class name is constructor
    public AClass(int b)
    {
        this.a = b;
        return;
    }

    public AClass()
    {
        // call AClass(int b)
        this(9);
        return;
    }

    public static void sets(int b)
    {
        AClass.s = b;
    }

    public void seta(int b)
    {
        this.a = b;
        return;
    }

    public int geta()
    {
        return this.a;
    }

    // many classes have equals method
    public boolean equals(AClass c)
    {
        return this.a == c.a;
    }
}
