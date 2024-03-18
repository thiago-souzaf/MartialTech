using System.Collections.Generic;
using TMPro;
using UnityEngine;

public class DifficultyDropdownHandler : MonoBehaviour
{
	public TMP_Dropdown difficultyDropdown;

	[field:SerializeField] public int amountOfStrikes {  get; private set; }

	private enum Difficulty
	{
		Easy,
		Medium,
		Hard
	}

	private Dictionary<Difficulty, int> _strikesValues = new()
    {
		{Difficulty.Easy, 5},
		{Difficulty.Medium, 10},
		{Difficulty.Hard, 15}
    };

    private void Start()
    {
		difficultyDropdown.onValueChanged.AddListener(OnDropdownValueChanged);
		OnDropdownValueChanged(difficultyDropdown.value);

    }

	private void OnDropdownValueChanged(int selectedIndex)
	{
		Difficulty selectedDifficulty = (Difficulty)selectedIndex;
		amountOfStrikes = _strikesValues[selectedDifficulty];
		PlayerPrefs.SetInt("strikes", amountOfStrikes);
	}
}

