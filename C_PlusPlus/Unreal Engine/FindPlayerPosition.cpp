// Include necessary headers
#include "MyPlayerController.h"
#include "GameFramework/Actor.h" // Include if not already included
#include "GameFramework/PlayerController.h" // Include if not already included
#include "GameFramework/Character.h" // Include if not already included

// Function to find and return the player's position
FVector AMyPlayerController::FindPlayerPosition() const
{
    // Get a reference to the player controller
    APlayerController* PlayerController = GetWorld()->GetFirstPlayerController();

    if (PlayerController)
    {
        // Get the player character
        ACharacter* PlayerCharacter = Cast<ACharacter>(PlayerController->GetPawn());

        if (PlayerCharacter)
        {
            // Get and return the player character's location
            return PlayerCharacter->GetActorLocation();
        }
    }

    // If the player controller or character is not found, return a default location
    return FVector::ZeroVector;
}
