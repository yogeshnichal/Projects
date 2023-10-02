// Include necessary headers
#include "RotateActorAroundPlayer.h" // Replace with your custom actor class header
#include "GameFramework/SpringArmComponent.h"
#include "Camera/CameraComponent.h"
#include "Kismet/GameplayStatics.h" // For UGameplayStatics

// Sets default values
ARotateActorAroundPlayer::ARotateActorAroundPlayer()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Create the root component
    RootComponent = CreateDefaultSubobject<USceneComponent>(TEXT("RootComponent"));

    // Create a spring arm component (for camera)
    SpringArmComponent = CreateDefaultSubobject<USpringArmComponent>(TEXT("SpringArmComponent"));
    SpringArmComponent->SetupAttachment(RootComponent);
    SpringArmComponent->TargetArmLength = 300.0f;

    // Create a camera component
    CameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("CameraComponent"));
    CameraComponent->SetupAttachment(SpringArmComponent);

    // Set default rotation speed
    RotationSpeed = 45.0f;
}

// Called when the game starts or when spawned
void ARotateActorAroundPlayer::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ARotateActorAroundPlayer::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);

    // Rotate the actor around the player's location
    RotateAroundPlayer();
}

// Function to rotate the actor around the player
void ARotateActorAroundPlayer::RotateAroundPlayer()
{
    if (PlayerCharacter)
    {
        // Get the player's location
        FVector PlayerLocation = PlayerCharacter->GetActorLocation();

        // Calculate the new actor location after rotation
        FVector NewLocation = PlayerLocation + (GetActorLocation() - PlayerLocation).RotateAngleAxis(
            RotationSpeed * DeltaTime,
            FVector(0.0f, 0.0f, 1.0f) // Rotate around the Z-axis (upward)
        );

        // Set the new actor location
        SetActorLocation(NewLocation);
    }
}

// Called to bind functionality to input
void ARotateActorAroundPlayer::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    // Bind functions to input actions
    PlayerInputComponent->BindAxis("RotateActor", this, &ARotateActorAroundPlayer::RotateInput);
}

// Function to handle rotation input
void ARotateActorAroundPlayer::RotateInput(float Value)
{
    // Update the rotation speed based on input value (can be used for dynamic speed control)
    RotationSpeed = BaseRotationSpeed + Value * RotationSpeedMultiplier;
}

// Set the player character for rotation reference
void ARotateActorAroundPlayer::SetPlayerCharacter(APawn* NewPlayerCharacter)
{
    PlayerCharacter = NewPlayerCharacter;
}
