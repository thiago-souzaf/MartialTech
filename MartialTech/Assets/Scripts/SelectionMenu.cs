using System;
using TMPro;
using UnityEngine;

public class SelectionMenu : MonoBehaviour
{
    [SerializeField] TextMeshProUGUI TMP_time;
    [SerializeField] TextMeshProUGUI TMP_date;

    string currentHour;
    string todayDate;

    private void Start()
    {
        DateTime dt = DateTime.Now;
        Debug.Log(dt.ToString());

        currentHour = string.Format("{0:hh:mm tt}", dt);
        todayDate = dt.ToShortDateString();

        TMP_time.text = currentHour;
        TMP_date.text = todayDate;
    }
}
