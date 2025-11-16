/**
 *      Author: HAO GU
 *      Course: JC2002
 *        Date: 8 October 2025
 *
 * Description: This is the entry point for our application.
 *              It is where the program begins its execution.
 *              It contains the main method, which allows the
 *              Java Virtual Machine (JVM) to run the code of
 *              our Cryptography coursework.
 */
public class Main {
    public static void main(String[] args) {
        Test tester = new Test();

        tester.testCaesarString("FIRST LEGION ATTACK EAST!");
        System.out.println();

        try {
            tester.testCaesarFile("titus_small_uppercase.txt");
            System.out.println();

            tester.testCaesarDecryptFile("encrypted_text_with_many_es.txt");

        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        tester.testCaesarMultipleKeysString("First Legion");
    } // End of main(String[] args)
} // End of class Main