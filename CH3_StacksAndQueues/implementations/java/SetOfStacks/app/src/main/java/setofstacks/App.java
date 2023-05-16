package setofstacks;

public class App {
    public static void main(String[] args) {
        SetOfStacks sos = new SetOfStacks(5);
        for (int i = 0; i < 30; i++) {
            sos.push(i);
        }

        for (int i = 0; i < 6; i++) {
            int popNum = sos.pop();
            String formatOut = String.format("%s",  Integer.toString(popNum));
            System.out.println(formatOut);
        }
    }
}
