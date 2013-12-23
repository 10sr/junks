public class BClass extends AClass{
    public BClass(int b)
    {
        super(b + 1);
        return;
    }

    public BClass()
    {
        super(10);
        return;
    }

    public void seta(int b)
    {
        this.a = b + 1;
        return;
    }
}
