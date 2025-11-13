/**
 *      Author: Marco A. Palomino
 *      Course: JC2002
 *        Date: 3 October 2025
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
        // ...

        // Whenever we create a new CaesarCipher object, we will also
        // generate a String containing the standard alphabet.
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Observation: Given that we have multiple keys, we can agree
        // that we also have multiple shifted alphabets. In fact, we
        // should have one shifted alphabet for each key. Thus,
        // shiftedAlphabet should no longer be a String, but an array
        // of shiftedAlphabet’s with as many entries as keys.
        // ...

        // Ensure that the encryption works with all letters (both
        // uppercase and lowercase).
        // ...
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
        StringBuilder encrypted = ...

        // Starting from 0, and all the way to the length of the
        // message, encrypt one by one each character.
        for (int i = 0; i < message.length(); i++) {

            // Consider the i-th character of the message (call it
            // currentChar)
            char currentChar = ...

            // First, check if the following character in the message
            // is an alphabetic character. All other characters
            // (spaces, punctuation, and numbers) will remain the same.
            ...

            // If it is not an alphabetic character, add the character
            // (as it is) to the encrypted message.
            ...
        } // End of for (int i = 0; i < message.length(); i++)

        // The return value is in the String inside the encrypted
        // StringBuilder
        return ...
    } // End of encryptWithMultipleKeys(message)
} // End of class CaesarCipherMultiple
