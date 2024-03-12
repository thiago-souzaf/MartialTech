using UnityEngine;
using System;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using PimDeWitte.UnityMainThreadDispatcher;

public class Listener : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private byte[] receiveBuffer = new byte[1024];

    // Endereco IP e porta do servidor
    private string serverIP = "127.0.0.1";
    private int serverPort = 25002;

    private TrainingManager manager;

    private void Start()
    {
        // Inicia a conexão com o servidor em uma thread separada
        Thread thread = new Thread(new ThreadStart(ConnectToServer));
        thread.Start();

        manager = TrainingManager.Instance;
    }

    private void ConnectToServer()
    {
        try
        {
            client = new TcpClient(serverIP, serverPort);
            stream = client.GetStream();

            // Inicia a recepção de dados
            while (true)
            {
                int bytesRead = stream.Read(receiveBuffer, 0, receiveBuffer.Length);

                if (bytesRead <= 0)
                {
                    // Desconectado do servidor
                    Debug.Log("Desconectado do servidor.");
                    break;
                }

                // Converte os bytes recebidos em uma string
                string receivedMessage = Encoding.UTF8.GetString(receiveBuffer, 0, bytesRead);

                // Imprime a mensagem no console do Unity
                Debug.Log($"Mensagem recebida: {receivedMessage}");


                UnityMainThreadDispatcher.Instance().Enqueue(() =>
                {
                    manager.AddStrike(receivedMessage);
                });
            }
        }
        catch (Exception e)
        {
            Debug.LogError($"Erro ao conectar ao servidor: {e.Message}");
        }
        finally
        {
            // Fecha a conexão quando a thread for encerrada
            if (client != null)
                client.Close();
        }
    }

    // Método para enviar mensagens ao servidor (opcional)
    private void SendMessageToServer(string message)
    {
        try
        {
            byte[] messageBytes = Encoding.UTF8.GetBytes(message);
            stream.Write(messageBytes, 0, messageBytes.Length);
        }
        catch (Exception e)
        {
            Debug.LogError($"Erro ao enviar mensagem: {e.Message}");
        }
    }

    private void OnDestroy()
    {
        // Fecha a conexão quando o objeto for destruído
        if (client != null)
            client.Close();
    }
}
