public class AClass{
    int a;

    // met of same name as class name is constructor
    public AClass(int b)
    {
        a = b;
    }

    public void seta(int b)
    {
        a = b;
        return;
    }

    public int geta()
    {
        return a;
    }

    // many classes have equals method
    public boolean equals(AClass c)
    {
        return a == c.a;
    }
}
