// Include necessary headers
#include "RotateAngleAxis.h" // Replace with your custom actor class header

// Sets default values
ARotateAngleAxis::ARotateAngleAxis()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Set default rotation properties
    RotationSpeed = 45.0f; // Degrees per second
    RotationAxis = FVector(0.0f, 0.0f, 1.0f); // Rotation axis (Z-axis by default)
}

// Called when the game starts or when spawned
void ARotateAngleAxis::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ARotateAngleAxis::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Rotate the actor using angle-axis rotation
    RotateUsingAngleAxis(DeltaTime);
}

// Function to rotate the actor using angle-axis rotation
void ARotateAngleAxis::RotateUsingAngleAxis(float DeltaTime)
{
    // Calculate the rotation angle based on the desired rotation speed
    float RotationAngle = RotationSpeed * DeltaTime;

    // Create a rotation quaternion using the angle-axis representation
    FQuat RotationQuat = FQuat(RotationAxis, FMath::DegreesToRadians(RotationAngle));

    // Apply the rotation to the actor's current rotation
    AddActorLocalRotation(RotationQuat);
}
