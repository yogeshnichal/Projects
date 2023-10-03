// Include necessary headers
#include "RotateAroundVector.h" // Replace with your custom actor class header

// Sets default values
ARotateAroundVector::ARotateAroundVector()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Set default rotation properties
    RotationSpeed = 45.0f; // Degrees per second
    RotationVector = FVector(0.0f, 0.0f, 1.0f); // Rotation vector (Z-axis by default)
}

// Called when the game starts or when spawned
void ARotateAroundVector::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ARotateAroundVector::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Rotate the actor around the specified vector
    RotateAroundVector(DeltaTime);
}

// Function to rotate the actor around the specified vector
void ARotateAroundVector::RotateAroundVector(float DeltaTime)
{
    // Calculate the rotation angle based on the desired rotation speed
    float RotationAngle = RotationSpeed * DeltaTime;

    // Calculate the rotation axis using the specified vector
    FVector RotationAxis = RotationVector.GetSafeNormal(); // Normalize the vector

    // Create a rotation quaternion using the axis and angle
    FQuat RotationQuat = FQuat(RotationAxis, FMath::DegreesToRadians(RotationAngle));

    // Apply the rotation to the actor's current rotation
    AddActorLocalRotation(RotationQuat);
}
