using System;
using UnityEngine;

public class ImagesListener : Listener
{
    public DisplayWebcam display;
    protected override void Start()
    {
        port = 25003;
        base.Start();
    }

    public override void HandleData(byte[] receiveBuffer, int bytesRead)
    {
        try
        { 
            // Criar uma Texture2D a partir dos dados decodificados
            Texture2D texture = new Texture2D(2, 2);

            texture.LoadImage(receiveBuffer);
            display.UpdateTexture(texture);

        }
        catch (Exception e)
        {
            Debug.LogError($"Erro ao lidar com os dados recebidos: {e.Message}");
        }
    }
}
