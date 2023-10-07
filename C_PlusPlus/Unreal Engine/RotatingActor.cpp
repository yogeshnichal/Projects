// Include necessary headers
#include "RotatingActor.h" // Replace with your custom actor class header

// Sets default values
ARotatingActor::ARotatingActor()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Set default rotation properties
    RotationSpeed = 45.0f; // Degrees per second
}

// Called when the game starts or when spawned
void ARotatingActor::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ARotatingActor::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Rotate the actor around its own axis
    RotateActor(DeltaTime);
}

// Function to rotate the actor
void ARotatingActor::RotateActor(float DeltaTime)
{
    // Calculate the rotation angle based on the desired rotation speed
    float RotationAngle = RotationSpeed * DeltaTime;

    // Create a rotation quaternion using the actor's current rotation
    FQuat RotationQuat = FQuat(GetActorRotation());

    // Create a delta rotation quaternion based on the rotation angle
    FQuat DeltaRotationQuat(FRotator(0.0f, RotationAngle, 0.0f));

    // Combine the two quaternions to calculate the new rotation
    RotationQuat = DeltaRotationQuat * RotationQuat;

    // Set the new actor rotation
    SetActorRotation(RotationQuat.Rotator());
}
