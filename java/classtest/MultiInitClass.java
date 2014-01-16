public class MultiInitClass{
    private int a = 0;
    private double b = 0.0;

    public MultiInitClass()
    {
        return;
    }

    public MultiInitClass(int a)
    {
        this.a = a;
    }

    public MultiInitClass(double b)
    {
        this.b = b;
    }

    private void _print()
    {
        System.out.println("a: " + this.a);
        System.out.println("b: " + this.b);
        return;
    }

    public void print()
    {
        this._print();
        return;
    }
}
