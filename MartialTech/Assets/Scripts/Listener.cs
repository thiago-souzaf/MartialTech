using UnityEngine;
using System;
using System.Net;
using System.Net.Sockets;
using System.Text;

public class Listener : MonoBehaviour
{
	public int port = 25001;

	private TcpListener listener;
	private TcpClient client;
	private NetworkStream stream;
	private byte[] buffer = new byte[1024];

    private void Start()
    {
		StartListening();
    }

	private void StartListening()
	{
		try
		{
			listener = new TcpListener(IPAddress.Any, port);
			listener.Start();

			Debug.Log("Waiting for a connection...");

			listener.BeginAcceptTcpClient(HandleIncomingConnection, null);
		}
		catch (Exception ex)
		{
			Debug.LogError("Error starting TCP listener: "+ ex.Message);
		}
	}

	private void HandleIncomingConnection(IAsyncResult result)
	{
		client = listener.EndAcceptTcpClient(result);
		stream = client.GetStream();

		Debug.Log("Connected");

		ReceiveMessage();
	}


	private void ReceiveMessage()
	{
        Debug.Log("Start Receive Message");

        stream.BeginRead(buffer, 0, buffer.Length, ReceiveCallback, null);
        Debug.Log("End Receive Message");

    }

    private void ReceiveCallback(IAsyncResult result)
	{
		Debug.Log("Start Receive Callback");
		Debug.Log("Start bytesRead");

		int bytesRead = stream.EndRead(result);
        Debug.Log("End bytesRead");

        if (bytesRead > 0)
		{
			string receivedMessage = Encoding.UTF8.GetString(buffer, 0, bytesRead);
			Debug.Log("Received message: " + receivedMessage);

			byte[] response = Encoding.UTF8.GetBytes("Message received");
			stream.Write(response, 0, response.Length);

			// Continue listening for more messages
			ReceiveMessage();

			// Tratar a receivedMessage aqui
			TrainingManager.Instance.AddStrike(receivedMessage);
		}
		else
		{
			Debug.Log("Connection closed");
			stream.Close();
			client.Close();

			StartListening();
		}
        Debug.Log("End Receive Callback");

    }

    private void OnDestroy()
    {
        listener?.Stop();
    }
}
