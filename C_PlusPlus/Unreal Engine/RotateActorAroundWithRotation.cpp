// Include necessary headers
#include "RotateActorAroundWithRotation.h" // Replace with your custom actor class header
#include "Kismet/GameplayStatics.h" // For UGameplayStatics

// Sets default values
ARotateActorAroundWithRotation::ARotateActorAroundWithRotation()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Set default rotation properties
    RotationSpeed = 45.0f;
    RotationAxis = FVector(0.0f, 0.0f, 1.0f); // Rotate around the Z-axis (upward)
    RotationCenter = FVector::ZeroVector; // Center of rotation (can be set in the editor)
}

// Called when the game starts or when spawned
void ARotateActorAroundWithRotation::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ARotateActorAroundWithRotation::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Rotate the actor around the specified axis and center
    RotateAroundAxisAndCenter(DeltaTime);
}

// Function to rotate the actor around the specified axis and center
void ARotateActorAroundWithRotation::RotateAroundAxisAndCenter(float DeltaTime)
{
    // Calculate the new actor rotation based on the desired rotation axis and speed
    FRotator NewRotation = GetActorRotation() + (RotationSpeed * DeltaTime) * RotationAxis;

    // Calculate the new actor location based on the center of rotation
    FVector NewLocation = RotationCenter + (GetActorLocation() - RotationCenter).RotateAngleAxis(
        RotationSpeed * DeltaTime,
        RotationAxis
    );

    // Set the new actor rotation and location
    SetActorRotation(NewRotation);
    SetActorLocation(NewLocation);
}
