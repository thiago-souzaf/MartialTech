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
	[SerializeField] TextMeshProUGUI scoreTracker;

    [SerializeField] Slider socosSlider;
	[SerializeField] Slider cotoveladasSlider;

	public int maxSocos;
	public int maxCotoveladas;

	public int currentSocos;
	public int currentCotoveladas;

	private int currentScore;

    private void Start()
    {
		socosSlider.maxValue = maxSocos;
		cotoveladasSlider.maxValue = maxCotoveladas;

		UpdateCount();
    }

    public void AddStrike(string strike)
	{

		if (strike == "soco" && currentSocos < maxSocos)
		{
			currentSocos++;
			UpdateCount();

        } else if (strike == "cotovelada" && currentCotoveladas < maxCotoveladas)
		{
			currentCotoveladas++;
			UpdateCount();
        }
	}

	private void UpdateCount()
	{
		socoCounter.text = currentSocos + "/" + maxSocos;
		socosSlider.value = currentSocos;

		cotoveladaCounter.text = currentCotoveladas + "/" + maxCotoveladas;
		cotoveladasSlider.value = currentCotoveladas;

		currentScore = (currentSocos + currentCotoveladas) * 100 / (maxSocos + maxCotoveladas);
		scoreTracker.text = currentScore + "%";
	}

}
