// Include necessary headers
#include "MyPlayerController.h"
#include "MyTargetActor.h" // Replace with the actual target actor header
#include "Engine/World.h"

// Function to smoothly change the view target to a specified actor with blending
void AMyPlayerController::SmoothChangeViewTargetToActor(AMyTargetActor* TargetActor)
{
    if (TargetActor && HasAuthority()) // Check if the target actor is valid and if this is the server
    {
        // Define the blend parameters
        FViewTargetTransitionParams TransitionParams;
        TransitionParams.BlendTime = BlendTimeInSeconds;
        TransitionParams.BlendFunction = EViewTargetBlendFunction::VTBlend_EaseInOut;
        TransitionParams.BlendExp = 2.0f;

        // Set the new view target with blending
        SetViewTargetWithBlend(TargetActor, TransitionParams);
    }
}
