import java.nio.file.Files;
import java.nio.file.Paths;

/**
 * Author: Hao Gu
 * Course: JC2002
 * Date: 13 November 2025
 * <p>
 * Description: A number of methods to test the implementation of
 *              the Caesar Cipher.
 */
public class Test {

    /**
     *
     * @param message The string to be encrypted.
     */
    public static void testCaesarString(String message) {
        // First, create a new CaesarCipher object with key=23.
        CaesarCipher cc = new CaesarCipher(23);  

        // Encrypt the given String!
        String encrypted = cc.encrypt(message);

        // Print out the encrypted String on the screen!
        System.out.println(encrypted);

    } // End of testCaesarString(message)


    /**
     * @brief 计算两个整数的最大公约数  
     * 
     * Reads a file encrypted with a single key and decrypt its contents,
     * using the CaesarBreaker decrypt() method. After that, the method
     * should print the encrypted message on the screen.
     *
     * @param fileName The name of the file to be encrypted.
     * @throws Exception
     */
    public void testCaesarDecryptFile(String fileName)
            throws Exception {

        // Read a text file and keep the contents in a String called
        // message!
        String message = new String(Files.readAllBytes(Paths.get(fileName)), java.nio.charset.StandardCharsets.UTF_8);//不知道是否正确

        // Create a CaesarBreaker object.
        CaesarBreaker cb = new CaesarBreaker();

        // Decrypt the message!
        String decrypted = cb.decrypt(message);

        // Print out the decrypted file on the screen!
        System.out.println(decrypted);
    } // End of testCaesarDecryptFile(fileName)


    /**
     * This method should read a file and encrypt the complete file using
     * the Caesar Cipher algorithm. After that, the method should print the
     * encrypted message on the screen.
     *
     * @param fileName The name of the file to be encrypted.
     * @throws Exception
     */
    public static void testCaesarFile(String fileName)
            throws Exception {
        // First, create a new CaesarCipher object with key=5.
        CaesarCipher cc = new CaesarCipher(5);

        // Read a text file and keep the contents in a String called
        // message!
        String message = new String(Files.readAllBytes(Paths.get(fileName)), java.nio.charset.StandardCharsets.UTF_8);//不知道是否正确

        // Encrypt the contents of the file!
        String encrypted = cc.encrypt(message);

        // Print out the encrypted file on the screen!
        System.out.println(encrypted);
    } // End of testCaesarFile(fileName)


    /**
     * This method should receive a message as a String parameter, create
     * a new CaesarCipherMultipleKeys object with two keys (23 and 17),
     * and encrypt the message. At the end, the method should print out
     * the result on the screen.
     *
     * @param message The string to be encrypted.
     */
    public static void testCaesarMultipleKeysString(String message) {
        // First, choose your keys.
        int[] keys = {23, 17};

        // Then, create a new CaesarCipherMultipleKeys object with such keys.
        CaesarCipherMultipleKeys ccmk = new CaesarCipherMultipleKeys(keys);

        // Encrypt the given String!
        String encrypted = ccmk.encryptWithMultipleKeys(message);

        // Print out the encrypted String!
        System.out.println(encrypted);

    } // End of testCaesarMultipleKeysString(message)
} // End of class Test
