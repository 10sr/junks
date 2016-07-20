//import java.io.*;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Map;
import java.util.LinkedHashMap;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Try{
    public static void main(String arg[]) throws Exception
    {
        System.out.println("Hell, world!");

        String str = "abcde";
        char str2 = str.charAt(2);
        System.out.println(str2);

        int[] a = {1,2,3,4,5};
        for (int e: a) {
            System.out.println(e);
        }

        String str3 = "abc def ghe";
        String[] strList = str3.split(" ");
        System.out.println(strList[0]);
        try {
            System.out.println(strList[-1]);
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Out of Range Error Detected:");
            e.printStackTrace();
        }

        // stdout: null:
        System.out.println(null + ":");
        System.out.println(null != null);

        System.out.println(EnumsTry.AEnum.E2.getVal());

        Map<String, String> m1 = new LinkedHashMap();
        Map<String, String> m2 = new LinkedHashMap();
        m1.put("key", "value");
        m2.put("key", "value");
        // stdout: Comparing map: true
        System.out.println("Comparing map: " + m1.equals(m2));

        BufferedReader r = new BufferedReader(new FileReader(new File("./a.txt")));
        String line = null;
        while ((line = r.readLine()) != null) {
            System.out.println("./a.txt: " + line);
        }

        // stdout: ab
        System.out.println("a" + 'b');
        // stdout: b
        System.out.println('b');

        Boolean flag = true;
        // stdout:
        // No output. Why?
        // Compile error on another environment
        // flag ? System.out.println("2") : System.out.println("3");

        Pattern p = Pattern.compile("^[\\?&]");
        System.out.println(p.matcher("hoge").find());
        System.out.println(p.matcher("\\oge").find());
        System.out.println(p.matcher("?oge").find());
        System.out.println(p.matcher("&oge").find());
    }

}
