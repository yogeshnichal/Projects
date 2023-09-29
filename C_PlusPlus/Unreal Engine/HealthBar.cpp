// Include necessary headers
#include "MyCharacter.h"
#include "GameFramework/SpringArmComponent.h"
#include "Camera/CameraComponent.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/Controller.h"
#include "GameFramework/CharacterMovementComponent.h"
#include "Kismet/GameplayStatics.h" // For UGameplayStatics

// Sets default values
AMyCharacter::AMyCharacter()
{
    // Set this character to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Create SpringArmComponent (for camera)
    SpringArmComponent = CreateDefaultSubobject<USpringArmComponent>(TEXT("SpringArmComponent"));
    SpringArmComponent->SetupAttachment(RootComponent);
    SpringArmComponent->TargetArmLength = 300.0f;

    // Create CameraComponent
    CameraComponent = CreateDefaultSubobject<UCameraComponent>(TEXT("CameraComponent"));
    CameraComponent->SetupAttachment(SpringArmComponent);

    // Set character movement properties
    GetCharacterMovement()->bOrientRotationToMovement = true;
    GetCharacterMovement()->RotationRate = FRotator(0.0f, 540.0f, 0.0f);
    GetCharacterMovement()->JumpZVelocity = 600.0f;
    GetCharacterMovement()->AirControl = 0.2f;

    // Initialize health
    MaxHealth = 100.0f;
    CurrentHealth = MaxHealth;
}

// Called when the game starts or when spawned
void AMyCharacter::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void AMyCharacter::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}

// Called to bind functionality to input
void AMyCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    // Bind functions to input actions
    PlayerInputComponent->BindAxis("MoveForward", this, &AMyCharacter::MoveForward);
    PlayerInputComponent->BindAxis("MoveRight", this, &AMyCharacter::MoveRight);
    PlayerInputComponent->BindAction("Jump", IE_Pressed, this, &AMyCharacter::StartJump);
    PlayerInputComponent->BindAction("Jump", IE_Released, this, &AMyCharacter::StopJump);
}

// Move the character forward/backward
void AMyCharacter::MoveForward(float Value)
{
    const FRotator Rotation = Controller->GetControlRotation();
    const FRotator YawRotation(0.0f, Rotation.Yaw, 0.0f);
    const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
    AddMovementInput(Direction, Value);
}

// Move the character right/left
void AMyCharacter::MoveRight(float Value)
{
    const FRotator Rotation = Controller->GetControlRotation();
    const FRotator YawRotation(0.0f, Rotation.Yaw, 0.0f);
    const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y);
    AddMovementInput(Direction, Value);
}

// Start character jump
void AMyCharacter::StartJump()
{
    bPressedJump = true;
}

// Stop character jump
void AMyCharacter::StopJump()
{
    bPressedJump = false;
}

// Function to apply damage to the character
void AMyCharacter::TakeDamage(float DamageAmount)
{
    if (DamageAmount > 0.0f)
    {
        CurrentHealth -= DamageAmount;

        // Check if the character's health is zero or below
        if (CurrentHealth <= 0.0f)
        {
            CurrentHealth = 0.0f;
            // Implement character death logic here, such as respawning or ending the game
        }

        // Update the health bar UI (you can implement this separately)
        UpdateHealthBarUI();

        // You can also play damage effects or animations here
    }
}

// Function to update the health bar UI (you can implement this separately)
void AMyCharacter::UpdateHealthBarUI()
{
    // Calculate the health percentage
    float HealthPercentage = FMath::Clamp(CurrentHealth / MaxHealth, 0.0f, 1.0f);

    // You can update your health bar UI widget with the HealthPercentage value
    // Example: UMyHealthBarWidget::SetHealthPercentage(HealthPercentage);
}
