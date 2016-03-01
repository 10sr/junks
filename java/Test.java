//import java.io.*;

import java.util.Map;
import java.util.LinkedHashMap;

class Test{
    public static void main(String arg[])
    {
        System.out.println("hello world");

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

        System.out.println(null + ":");
        System.out.println(null != null);

        System.out.println(EnumsTry.AEnum.E2.getVal());

        Map<String, String> m1 = new LinkedHashMap();
        Map<String, String> m2 = new LinkedHashMap();
        m1.put("key", "value");
        m2.put("key", "value");
        System.out.println("Comparing map: " + m1.equals(m2));
    }

}
