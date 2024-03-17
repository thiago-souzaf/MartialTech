using UnityEngine;
using System;
using System.Net.Sockets;
using System.Threading;
using PimDeWitte.UnityMainThreadDispatcher;

public abstract class Listener : MonoBehaviour
{
    private TcpClient client;
    private NetworkStream stream;
    private byte[] receiveBuffer = new byte[101000];

    // Endereco IP e porta do servidor
    private string serverIP = "127.0.0.1";
    protected int port;
    
    protected virtual void Start()
    {
        // Inicia a conexão com o servidor em uma thread separada
        Thread thread = new Thread(new ThreadStart(ConnectToServer));
        thread.Start();
    }


    protected virtual void ConnectToServer()
    {
        try
        {
            client = new TcpClient(serverIP, port);
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

                UnityMainThreadDispatcher.Instance().Enqueue(() =>
                {
                    HandleData(receiveBuffer, bytesRead);
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

    private void OnDestroy()
    {
        // Fecha a conexão quando o objeto for destruído
        if (client != null)
            client.Close();
    }

    public abstract void HandleData(byte[] receiveBuffer, int bytesRead);

}
