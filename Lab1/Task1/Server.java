// Server.java: A simple server program.

import java.net.*;
import java.io.*;

public class Server {
	public static void main(String args[]) throws IOException {

		// Register service on port 6666
		//try {
		ServerSocket server = new ServerSocket(6666);
		//}
		//catch(IOException e){
		//	System.out.println("Error with port 6666");
		//}
		while(true){
			System.out.println("Waiting for client to connect...");
			Socket socket = server.accept();
			//System.out.println("test1");
			//Create read/write from socket
			InputStream in = socket.getInputStream();
			DataInputStream in1 = new DataInputStream(in);
			OutputStream out = socket.getOutputStream();
			DataOutputStream out1 = new DataOutputStream(out);
			//System.out.println("test2");
		 	//client address
		 	InetAddress remoteIp = socket.getInetAddress();

		 	//Receiving from client
		 	String msg = new String(in1.readUTF());
		 	System.out.println("Client " + remoteIp + " : " + msg);

		 	//Sending a reversed string
		 	msg = reverseString(msg.trim());
		 	out1.writeUTF(msg);
		}
	}
	private static String reverseString(String input) {
		StringBuilder buf = new StringBuilder(input);
	 	return buf.reverse().toString();
	}
}