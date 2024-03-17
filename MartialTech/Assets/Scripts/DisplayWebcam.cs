using UnityEngine;

public class DisplayWebcam : MonoBehaviour
{

    [SerializeField]
    private UnityEngine.UI.RawImage _rawImage;

    public void UpdateTexture(Texture2D receivedTexture)
    {
        _rawImage.texture = receivedTexture;
    }

    [ContextMenu("Show active webcams")]
    public void ShowWebcams()
    {
        WebCamDevice[] devices = WebCamTexture.devices;
        for (int i = 0; i < devices.Length; i++)
        {
            print("Webcam available: " + devices[i].name);
        }
    }

    [ContextMenu("start camera")]
    public void LoadCam()
    {
        WebCamDevice[] devices = WebCamTexture.devices;

        // for debugging purposes, prints available devices to the console
        for (int i = 0; i < devices.Length; i++)
        {
            print("Webcam available: " + devices[i].name);
        }

        // assuming the first available WebCam is desired
        WebCamTexture tex = new WebCamTexture(devices[0].name);
        //rend.material.mainTexture = tex;
        this._rawImage.texture = tex;
        tex.Play();
    }

}
