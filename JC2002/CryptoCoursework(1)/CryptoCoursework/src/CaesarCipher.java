/**
 *      Author: Hao Gu
 *      Course: JC2002
 *        Date: 13 November 2025
 *
 * Description: A class to implement the Caesar Cipher algorithm.
 */
public class CaesarCipher {
    /**
     * 26 characters in the English alphabet.
     */
    private String alphabet;

    /**
     * The key for this cipher.
     */
    private int theKey;

    /**
     * The English alphabet after "shifting" it by the given key.
     */
    private String shiftedAlphabet;

    /**
     * Constructor
     *
     * @param key The key for the encryption algorithm.
     */
    public CaesarCipher(int key) {

        theKey = key;//这里我暂时不清楚谁先谁后
        key = ((key % 26) + 26) % 26;

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        shiftedAlphabet = alphabet.substring(26 - key) + alphabet.substring(0, 26 - key);             

        // In Task 4, you will need to make changes to ensure that the
        // encryption works with all letters (both uppercase and
        // lowercase). But do not change anything here until you reach
        // Task 4.
        //我不见得需要改这里，因为我在encrypt方法里处理了大小写问题

    } // End of CaesarCipher(int key)

    /**
     * This method returns a string (message) which has been encrypted
     * using the Caesar Cipher Algorithm.
     *
     * @param message The string to be encrypted.
     * @return The encrypted message.
     */
    public String encrypt(String message) {
        // Make a StringBuilder to build the encrypted message.
        StringBuilder encrypted = new StringBuilder(message);

        // Starting from 0, and all the way to the length of the
        // message, encrypt one by one each character.
        for (int i = 0; i < message.length(); i++) {

            // Consider the i-th character of the message (call it
            // currentChar)
            char currentChar = message.charAt(i);

            // First, check if the following character in the message
            // is an alphabetic character. All other characters
            // (spaces, punctuation, and numbers) will remain the same.
            if (Character.isLetter(currentChar)) {
                // Find the index of currentChar in the alphabet
                int idx = alphabet.indexOf(Character.toUpperCase(currentChar));//这里时间复杂度有点高

                // Get the corresponding encrypted character
                char newChar = shiftedAlphabet.charAt(idx);

                // Preserve the case of the original character
                if (Character.isLowerCase(currentChar)) {
                    newChar = Character.toLowerCase(newChar);
                }

                // Replace the character at position i with newChar
                encrypted.setCharAt(i, newChar);
            }

            // If it is not an alphabetic character, add the character
            // (as it is) to the encrypted message.
            //这里应该是不需要处理的，因为StringBuilder初始化的时候已经是message的内容了
        } // End of for (int i = 0; i < message.length(); i++)

        // Your answer must be the String inside the StringBuilder
        // variable called 'encrypted'.
        return encrypted.toString();
    } // End of encrypt(message)

} // End of CaesarCipher