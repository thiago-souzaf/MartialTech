using UnityEngine;
using System.Text;

public class GolpesListener : Listener
{
    private TrainingManager manager;

    protected override void Start()
    {
        port = 25002;
        base.Start();

        manager = TrainingManager.Instance;
    }

    public override void HandleData(byte[] receiveBuffer, int bytesRead)
    {
        // Converte os bytes recebidos em uma string
        string receivedMessage = Encoding.UTF8.GetString(receiveBuffer, 0, bytesRead);

        // Imprime a mensagem no console do Unity
        Debug.Log($"Mensagem recebida na porta {port}: {receivedMessage}");

        manager.AddStrike(receivedMessage);
    }
    
}
