//package RSAAlgorithm;

import java.util.Scanner;

public class RSA {

	static Scanner scan; 

	public static void main(String[] args){
		String message;
		int[] plainText = new int[100];
		int[] cipherText = new int[100];
		int n = 253, d = 17, e = 13, p = 0, q = 0, i = 0;

		scan = new Scanner(System.in);

		System.out.println("Enter file name :");
		message = scan.nextLine();
		Scanner fileScanner = new Scanner(new File(message))

		// for (String line : Files.readAllLines(Paths.get(message))) {
  //   		for (String part : line.split("\\s+"){
  //   			plainText[i] = part
  //   		}
		// }


		for (i = 0; i < message.length(); i++){
			plainText[i] = message.charAt(i);
		}

		System.out.println("Cipher Text :");
		for (i = 0; i < message.length(); i++){
			cipherText[i] = mult(plainText[i], e, n);
		}

		for (i = 0; i < message.length(); i++){
			System.out.print(" "+cipherText[i]);
		}

		System.out.println("\nPlain Text :");

		for (i = 0; i < message.length(); i++){
			System.out.print((char)plainText[i]);;
		}

		for (i = 0; i < message.length(); i++){
			plainText[i] = mult(cipherText[i], d, n);
		}
		System.out.println();
	}
	private static int mult(int plainText, int e, int n) {
		int k = 1;
		int j;
		for (j = 0; j <= e; j++){
			k = (k * plainText) % n;
		}
		return k;
	}
}