/**
 *      Author: Gu Hao
 *      Course: JC2002
 *        Date: 13 November 2025
 *
 * Description: A class to implement the Caesar Cipher algorithm. It
 *              will require some enhancements to work with all letters
 *              (both uppercase and lowercase) and to make it harder to
 *              decrypt.
 */
public class CaesarCipherMultipleKeys {
    /**
     * All the characters in the English alphabet (must be 26).
     */
    private String alphabet;

    /**
     * Given that we have multiple keys, we can agree that we also have
     * multiple shifted alphabets. In fact, we should have one shifted
     * alphabet for each key. Thus, shiftedAlphabet should no longer
     * be a String, but an array of shiftedAlphabet’s with as many
     * entries as keys.
     */
    private String[] shiftedAlphabet;
    private int[] keys;

    /**
     * Constructor
     *
     * @param keys An array of keys to encrypt messages.
     */
    public CaesarCipherMultipleKeys(int[] keys) {
        // Assign the keys to the instance variable keys.
        this.keys = keys;

        // Whenever we create a new CaesarCipher object, we will also
        // generate a String containing the standard alphabet.
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Observation: Given that we have multiple keys, we can agree
        // that we also have multiple shifted alphabets. In fact, we
        // should have one shifted alphabet for each key. Thus,
        // shiftedAlphabet should no longer be a String, but an array
        // of shiftedAlphabet’s with as many entries as keys.
        shiftedAlphabet = new String[keys.length];

        // Ensure that the encryption works with all letters (both
        // uppercase and lowercase).
        for (int i = 0; i < keys.length; ++i) {
            int key = ((keys[i] % 26) + 26) % 26;
            String shifted = alphabet.substring(26 - key) + 
                            alphabet.substring(0, 26 - key);
            shiftedAlphabet[i] = shifted;
        }
    } // End of CaesarCipherMultiple(keys)

    /**
     * This method returns a String that has been encrypted using the
     * following algorithm:
     *
     * (1) The first key in the array of keys is used to encrypt every
     * other character with the Caesar Cipher algorithm, starting with
     * the first character, and
     *
     * (2) The second key in the array of keys is used to encrypt
     * every other character, starting with the second character.
     *
     * @param message The string to be encrypted.
     * @return The encrypted message.
     */
    public String encryptWithMultipleKeys(String message) {
        // Make a StringBuilder to build the encrypted message.
        StringBuilder encrypted = new StringBuilder(message);

        // Starting from 0, and all the way to the length of the
        // message, encrypt one by one each character.
        for (int i = 0; i < message.length(); ++i) {

            // Consider the i-th character of the message (call it
            // currentChar)
            char currentChar = message.charAt(i);

            // First, check if the following character in the message
            // is an alphabetic character. All other characters
            // (spaces, punctuation, and numbers) will remain the same.
            if (Character.isLetter(currentChar)) {
                // Find the index of the currentChar in the
                // alphabet (regardless of whether it is upper
                // or lowercase).
                char upperChar = Character.toUpperCase(currentChar);
                int idx = alphabet.indexOf(upperChar);

                // Determine which key to use.
                int keyIndex = i % keys.length;

                // Get the shifted alphabet corresponding to
                // the key to be used.
                // Get the encrypted character.
                char newChar = shiftedAlphabet[keyIndex].charAt(idx);

                // Preserve the case of the original character.
                if (Character.isLowerCase(currentChar)) {
                    newChar = Character.toLowerCase(newChar);
                }

                // Replace the i-th character of the encrypted
                // message with newChar.
                encrypted.setCharAt(i, newChar);
            }

            // If it is not an alphabetic character, add the character
            // (as it is) to the encrypted message.
            //这里应该是不需要处理的，因为StringBuilder初始化的时候已经是message的内容了
        } // End of for (int i = 0; i < message.length(); i++)

        // The return value is in the String inside the encrypted
        // StringBuilder
        return encrypted.toString();
    } // End of encryptWithMultipleKeys(message)
} // End of class CaesarCipherMultiple
