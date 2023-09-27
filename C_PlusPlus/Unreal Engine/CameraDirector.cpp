// Include necessary headers
#include "CameraDirector.h"
#include "Camera/CameraComponent.h"
#include "Engine/World.h"

// Sets default values
ACameraDirector::ACameraDirector()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;
}

// Called when the game starts or when spawned
void ACameraDirector::BeginPlay()
{
    Super::BeginPlay();

    // Initialize camera switch timer
    SwitchCameraTimer = SwitchInterval;
    CurrentCameraIndex = 0;

    // Get all cameras attached to this actor
    GetAllAttachedCameras();
}

// Called every frame
void ACameraDirector::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Update the camera switch timer
    SwitchCameraTimer -= DeltaTime;

    if (SwitchCameraTimer <= 0)
    {
        // Switch to the next camera in the array
        SwitchToNextCamera();
        SwitchCameraTimer = SwitchInterval;
    }
}

// Get all cameras attached to this actor
void ACameraDirector::GetAllAttachedCameras()
{
    TArray<UCameraComponent*> CameraComponents;
    GetComponents<UCameraComponent>(CameraComponents);

    for (UCameraComponent* CameraComp : CameraComponents)
    {
        Cameras.Add(CameraComp);
    }
}

// Switch to the next camera in the array
void ACameraDirector::SwitchToNextCamera()
{
    // Ensure there are cameras to switch to
    if (Cameras.Num() == 0)
    {
        return;
    }

    // Hide the current camera
    if (CurrentCameraIndex < Cameras.Num())
    {
        Cameras[CurrentCameraIndex]->Deactivate();
    }

    // Increment the camera index and wrap around if needed
    CurrentCameraIndex = (CurrentCameraIndex + 1) % Cameras.Num();

    // Show the next camera
    if (CurrentCameraIndex < Cameras.Num())
    {
        Cameras[CurrentCameraIndex]->Activate();
    }
}
