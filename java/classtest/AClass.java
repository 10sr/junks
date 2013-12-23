public class AClass{
    int a;

    // met of same name as class name is constructor
    public AClass(int b)
    {
        a = b;
    }

    public void met1(int b)
    {
        a = b;
        return;
    }

    public int met2()
    {
        return a;
    }
}
