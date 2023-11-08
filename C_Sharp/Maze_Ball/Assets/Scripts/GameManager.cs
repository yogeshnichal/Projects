using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using TMPro;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{

    public float timeLeft = 20;

    bool gameOver = false;
    bool gameWin = false;

    public GameObject winText;
    public GameObject gameOverText;
    public GameObject ball;
    public PlayerController player;

    public TextMeshProUGUI timerText;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
        if(timeLeft >= 0 && !gameWin)
        {
            timeLeft -= Time.deltaTime;

            timerText.text = timeLeft.ToString("F1");
        }
        if(timeLeft <= 0 && !gameWin)
        {
            GameOver();
        }

    }

    public void GameWin()
    {
        gameWin = true;
        winText.SetActive(true);
        player.enabled = false;
        ball.SetActive(false);
    }

    public void GameOver()
    {
        gameOverText.SetActive(true);
        player.enabled = false;
        gameOver = true;
    }

    public void Restart()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
