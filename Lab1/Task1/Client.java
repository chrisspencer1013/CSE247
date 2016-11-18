// Client.java: A simple client program.
import java.net.*;
import java.io.*;
public class Client {
	public static void main(String args[]) throws IOException {
	Socket socket = new Socket("127.0.0.1", 6666);

	//Define read/write from socket
	 InputStream in = socket.getInputStream();
	 DataInputStream in1 = new DataInputStream(in);
	 OutputStream out = socket.getOutputStream();
	 DataOutputStream out1 = new DataOutputStream(out);
	 //Send hello message
	 String msg = "Hello";
	 out1.writeUTF(msg);
	 //Receive a reversed message
	 msg = in1.readUTF();
	 System.out.println("Server : " + msg);
	}
}
//Task 2: Client Server programming in Java using User 