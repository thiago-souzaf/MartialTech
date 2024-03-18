using TMPro;
using UnityEngine;
using UnityEngine.Events;
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
	[SerializeField] TextMeshProUGUI cruzadoCounter;
    [SerializeField] TextMeshProUGUI scoreTracker;

    [SerializeField] Slider socosSlider;
    [SerializeField] Slider cotoveladasSlider;
    [SerializeField] Slider cruzadosSlider;

	public int maxStrikes;

	public UnityEvent OnTrainingFinish;

	private int currentSocos;
	private int currentCotoveladas;
	private int currentCruzados;

	private int currentScore;

    private void Start()
    {
		maxStrikes = PlayerPrefs.GetInt("strikes", 5);

		socosSlider.maxValue = maxStrikes;
		cotoveladasSlider.maxValue = maxStrikes;
		cruzadosSlider.maxValue = maxStrikes;
		UpdateCount();
    }

    public void AddStrike(string strike)
	{

		if (strike == "soco" && currentSocos < maxStrikes)
		{
			currentSocos++;

        }
		else if (strike == "cotovelada" && currentCotoveladas < maxStrikes)
		{
			currentCotoveladas++;
        }
		else if (strike == "cruzado" && currentCruzados < maxStrikes)
        {
			currentCruzados++;
        }

        UpdateCount();
    }

    private void UpdateCount()
	{
		socoCounter.text = currentSocos + "/" + maxStrikes;
		socosSlider.value = currentSocos;

		cotoveladaCounter.text = currentCotoveladas + "/" + maxStrikes;
		cotoveladasSlider.value = currentCotoveladas;

        cruzadoCounter.text = currentCruzados + "/" + maxStrikes;
        cruzadosSlider.value = currentCruzados;

        currentScore = (currentSocos + currentCotoveladas + currentCruzados) * 100 / (3 * maxStrikes);
		scoreTracker.text = currentScore + "%";

		if (currentScore >= 99.9)
		{
			OnTrainingFinish.Invoke();
		}
	}


}
