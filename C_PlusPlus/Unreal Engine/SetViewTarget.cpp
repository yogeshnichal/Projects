// Include necessary headers
#include "MyPlayerController.h"
#include "MyTargetActor.h" // Replace with the actual target actor header
#include "Engine/World.h"

// Function to change the view target to a specified actor
void AMyPlayerController::ChangeViewTargetToActor(AMyTargetActor* TargetActor)
{
    if (TargetActor && HasAuthority()) // Check if the target actor is valid and if this is the server
    {
        SetViewTargetWithBlend(TargetActor, TransitionTime);
    }
}
