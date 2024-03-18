using System;
using TMPro;
using UnityEngine;
using System.Diagnostics;

public class SelectionMenu : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI TMP_time;
    [SerializeField] TextMeshProUGUI TMP_date;

    private DateTime dt;
    string currentHour;
    string todayDate;

    private void Start()
    {
        InvokeRepeating(nameof(SetCurrentTime), 0, 1);
        StartPython();
    }

    private void SetCurrentTime()
    {
        dt = DateTime.Now;

        currentHour = string.Format("{0:hh:mm tt}", dt);
        TMP_time.text = currentHour;

        todayDate = dt.ToShortDateString();
        TMP_date.text = todayDate;

    }

    private void StartPython()
    {
        string pythonScriptPath = "E:\\Dev\\Unity-projects\\Projeto-RV\\MartialTech\\Assets\\Deteccao\\test.py";

        ProcessStartInfo startInfo = new ProcessStartInfo();
        startInfo.FileName = "python";
        startInfo.Arguments = pythonScriptPath;
        startInfo.UseShellExecute = false;
        startInfo.RedirectStandardOutput = true;

        Process process = new Process();
        process.StartInfo = startInfo;
        process.Start();
    }
}
