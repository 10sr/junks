public class EnumsTry {
    public enum AEnum {
        E1("abc"), E2("cdf"), E3("eee");

        private String val;
        private AEnum(String arg){
            val = arg;
        }

        public String getVal(){
            return val;
        }
    }
}
