// Client.java: A simple client program.
import java.net.*;
import java.io.*;
public class Client {
public static void main(String args[]) throws IOException {
DatagramSocket socket = null;
 DatagramPacket inPacket = null;
 DatagramPacket outPacket = null;
 byte[] inBuf, outBuf;
 final int PORT = 6666;
 String msg = null;
InetAddress address = InetAddress.getByName("127.0.0.1");
 socket = new DatagramSocket();
 //Convert string to byte and send to server
 msg = "Hello";
 outBuf = msg.getBytes();
 outPacket = new DatagramPacket(outBuf, 0, outBuf.length,address,
PORT);
 socket.send(outPacket);
 //Receive reversed message from server
 inBuf = new byte[256];
 inPacket = new DatagramPacket(inBuf, inBuf.length);
 socket.receive(inPacket);
 String data = new String(inPacket.getData(), 0, inPacket.getLength());
 System.out.println("Server : " + data);
}
}