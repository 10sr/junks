import java.io.*;

class Test{
    public static void main(String arg[])
    {
        AClass c = new AClass(3);
        int a = c.a;
        System.out.println("hello world");
        System.out.println(a);

        c.seta(2);
        System.out.println(c.a);

        AClass c2 = new AClass(4);
        System.out.println(c.equals(c2));

        System.out.println(c.s);
        c.sets(5);
        System.out.println(c2.s);

        // BClass d = new BClass();
        // d.seta(0);
        // System.out.println(d.a);
    }
}
