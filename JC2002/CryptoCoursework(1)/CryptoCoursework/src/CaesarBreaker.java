/**
 *      Author: Gu Hao
 *      Course: JC2002
 *        Date: 13 November 2025
 *
 * Description: A class to decrypt a message that was encrypted with one
 *              key, using statistical letter frequencies of English text.
 */
public class CaesarBreaker {

    /**
     * All the characters in the English alphabet (must be 26 characters).
     */
    private String alphabet = "abcdefghijklmnopqrstuvwxyz";

    /**
     * Counts the frequency of each of the letters in the encrypted message.
     *
     * @param message The encrypted message.
     * @return An int array containing the frequency of each letter of
     *         the alphabet.
     */
    public int[] countLettersFrequency(String message) {
        // An array of 26 frequency counters: one for each letter from
        // ‘a’ to ‘z’.
        int[] frequencies = new int[26];

        // Starting from 0, and all the way to the length of the
        // message, count the frequency of the letters.
        for (int i = 0; i < message.length(); ++i) {

            // To make everything simpler, convert all the characters
            // in the encrypted message to lower case as you read them.
            if (Character.isLetter(message.charAt(i))) {
                char ch = Character.toLowerCase(message.charAt(i));

                // Find the index of the character in the alphabet.
                int idx = alphabet.indexOf(ch);

                // Increment the frequency counter for that letter.
                ++frequencies[idx];
            }

        } // End of for (int i = 0...

        // Return the array containing the frequencies!
        return frequencies;
    } // End of countLettersFrequency(message)


    /**
     * Decrypts a message that was encrypted with one key.
     *
     * @param encrypted The encrypted message.
     * @return The decrypted message.
     */
    public String decrypt(String encrypted) {
        // Determine the key. Make use of the getKey() method
        // implemented in this same class.
        int key = getKey(encrypted);

        // Create a new CaesarCipher object with the key retrieved
        // above. Recall that if key was used to encrypt the
        // "original" message, then 26 - key should decrypt the
        // "encrypted" message.
        CaesarCipher cc = new CaesarCipher(26 - key);

        // Decrypt the message.
        String message = cc.encrypt(encrypted);

        // Return the decrypted message!
        return message;
    } // End of decrypt(encrypted)


    /**
     * This method begins by determining the two keys used to encrypt the
     * message, and then uses those keys to decrypt the message.
     *
     * @return The original message encrypted with two keys.
     */
    public String decryptWithTwoKeys(String encrypted) {

        // Calculate a String of every other character starting with the
        // first character of the encrypted String.
		//
		// You may require some extra code here to retrieve the right
		// characters that you will assign to encrypted1.
        String encrypted1 = extractCharacter(encrypted, 0, 2);

        // Calculate a String of every other character starting with the
        // second character of the encrypted String.
		//
		// You may require some extra code here to retrieve the right
		// characters that you will assign to encrypted2.
        String encrypted2 = extractCharacter(encrypted, 1, 2);

        // Then calculate the key used to encrypt each half String.
        int[] keys = new int[2];
        keys[0] = getKey(encrypted1);
        keys[1] = getKey(encrypted2);

        // Create a new Caesar Cipher object capable of encrypting
        // messages with two strings.
        int[] decKeys = new int[] { (26 - keys[0]) % 26, (26 - keys[1]) % 26 };
		CaesarCipherMultipleKeys ccmk = new CaesarCipherMultipleKeys(decKeys);

        // Calculate and return the decrypted String using the
        // encryptWithMultipleKeys method from the CaesarCipher
        // class.
        String message = ccmk.encryptWithMultipleKeys(encrypted);
		
        return message;
    } // End of decryptWithTwoKeys (String encrypted)


    /**
     * This method should call countLetters to get an array of the letter
     * frequencies in String encrypted and then use maxIndex to calculate
     * the index of the largest letter frequency, which is the location
     * of the encrypted letter ‘e’, which leads to the key, which is
     * returned.
     *
     * @param encrypted The encrypted message
     * @return The key used to encrypt the message
     */
    public int getKey(String encrypted) {

        // First, calculate the frequencies for each letter of the
        // alphabet. Assume all letters are lowercase.
        int[] frequencies = countLettersFrequency(encrypted);

        // Now, identify the maximum frequency and call it maximum.
        int maximum = maxIndex(frequencies);

        // Finally, determine the value of the key used for
        // encryption. Recall that the key should be the
        // distance between maxIndex and 4, but you have to
        // consider what happens when maxIndex < 4.
        //
        // The following is an optimised implementation:
        //
        // int key = (maximum - 4 + 26) % 26;//我不知道这里是谁写的
        //
        int key = (4 - maximum + 26) % 26;

        // Return the key!
        return key;
    } // End of getKey(encrypted)


    /**
     * Receives an array containing the frequency for each letter of the
     * alphabet and returns the position of the largest value in such an
     * array. The position returned corresponds to the position of the
     * letter that appears most often in the encrypted text.
     *
     * @param frequencies An array containing the frequency for each
     *                   letter of the alphabet.
     * @return The position of the largest value in the array of
     *         frequencies.
     */
    public static int maxIndex(int[] frequencies) {
        int maximum = 0;

        // Identify the position of the largest value in the array
        // of frequencies. Call that position maximum.
        for (int i = 0; i < frequencies.length; ++i) {
            if (frequencies[i] > frequencies[maximum]) {
                maximum = i;
            }
        }

        // Return maximum (that is, the position of the largest value
        // in the array of frequencies).
        return maximum;
    } // End of maxIndex(frequencies)

    /**
     * Extracts a substring by taking every other character starting from a given index.
     *
     * @param input The original string from which characters will be extracted.
     * @param startIndex The starting index (0 for even-indexed characters, 1 for odd-indexed characters).
     * @param step The step size.
     * @return A new string containing every other character starting from the given index.
     */
    private static String extractCharacter(String input, int startIndex, int step) {
        StringBuilder result = new StringBuilder();
        for (int i = startIndex; i < input.length(); i += step) {
            result.append(input.charAt(i));
        }
        return result.toString();
    }
}
