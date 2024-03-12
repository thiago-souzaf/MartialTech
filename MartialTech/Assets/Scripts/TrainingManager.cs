using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class TrainingManager : MonoBehaviour
{
	public static TrainingManager Instance { get; private set; }

    private void Awake()
    {
        Instance = this;
    }

    [SerializeField] TextMeshProUGUI socoCounter;
	[SerializeField] TextMeshProUGUI cotoveladaCounter;
	[SerializeField] Slider socosSlider;
	[SerializeField] Slider cotoveladasSlider;

	public int maxSocos;
	public int maxCotoveladas;

	public int currentSocos;
	public int currentCotoveladas;

    private void Start()
    {
		UpdateCount();
    }

    public void AddStrike(string strike)
	{

		if (strike == "soco")
		{
			currentSocos++;
			UpdateCount();

        } else if (strike == "cotovelada")
		{
			currentCotoveladas++;
			UpdateCount();
        }
	}

	private void UpdateCount()
	{
		socoCounter.text = currentSocos + "/" + maxSocos;
		socoCounter.ForceMeshUpdate();
		socosSlider.value = currentSocos;

		cotoveladaCounter.text = currentCotoveladas + "/" + maxCotoveladas;
		cotoveladasSlider.value = currentCotoveladas;
	}

	[ContextMenu("add soco")]
	public void AddSoco()
	{
        currentSocos++;
        UpdateCount();
    }
}
