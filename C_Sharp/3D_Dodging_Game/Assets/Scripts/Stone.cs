using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Stone : MonoBehaviour
{
    // Start is called before the first frame update
    private void OnBecameInvisible()
    {
        Destroy(gameObject);
    }
}