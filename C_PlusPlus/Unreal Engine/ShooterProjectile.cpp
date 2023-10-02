// Include necessary headers
#include "ShooterCharacter.h" // Replace with your character class header
#include "ShooterProjectile.h" // Replace with your projectile class header
#include "GameFramework/SpringArmComponent.h"
#include "Camera/CameraComponent.h"
#include "GameFramework/PlayerController.h"
#include "Kismet/GameplayStatics.h" // For UGameplayStatics
#include "Engine/World.h"

// Sets default values
AShooterCharacter::AShooterCharacter()
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

    // Set default values for shooting
    FireRate = 0.1f;
    bCanShoot = true;
}

// Called when the game starts or when spawned
void AShooterCharacter::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void AShooterCharacter::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}

// Called to bind functionality to input
void AShooterCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    // Bind functions to input actions
    PlayerInputComponent->BindAxis("MoveForward", this, &AShooterCharacter::MoveForward);
    PlayerInputComponent->BindAxis("MoveRight", this, &AShooterCharacter::MoveRight);
    PlayerInputComponent->BindAction("Jump", IE_Pressed, this, &AShooterCharacter::StartJump);
    PlayerInputComponent->BindAction("Jump", IE_Released, this, &AShooterCharacter::StopJump);
    PlayerInputComponent->BindAction("Shoot", IE_Pressed, this, &AShooterCharacter::StartShooting);
}

// Move the character forward/backward
void AShooterCharacter::MoveForward(float Value)
{
    const FRotator Rotation = Controller->GetControlRotation();
    const FRotator YawRotation(0.0f, Rotation.Yaw, 0.0f);
    const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
    AddMovementInput(Direction, Value);
}

// Move the character right/left
void AShooterCharacter::MoveRight(float Value)
{
    const FRotator Rotation = Controller->GetControlRotation();
    const FRotator YawRotation(0.0f, Rotation.Yaw, 0.0f);
    const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y);
    AddMovementInput(Direction, Value);
}

// Start character jump
void AShooterCharacter::StartJump()
{
    bPressedJump = true;
}

// Stop character jump
void AShooterCharacter::StopJump()
{
    bPressedJump = false;
}

// Start shooting
void AShooterCharacter::StartShooting()
{
    if (bCanShoot)
    {
        // Spawn and fire a projectile
        FireProjectile();

        // Set a delay before allowing another shot
        GetWorld()->GetTimerManager().SetTimer(ShootingCooldownTimerHandle, this, &AShooterCharacter::EnableShooting, FireRate, false);
    }
}

// Fire a projectile
void AShooterCharacter::FireProjectile()
{
    if (ProjectileClass)
    {
        // Get the camera transform to determine the projectile's spawn location and direction
        FTransform CameraTransform = CameraComponent->GetComponentTransform();

        // Offset the spawn location slightly forward to avoid self-collision
        FVector SpawnLocation = CameraTransform.GetLocation() + (CameraTransform.GetRotation().GetForwardVector() * ProjectileSpawnOffset);

        // Spawn the projectile
        AShooterProjectile* Projectile = GetWorld()->SpawnActor<AShooterProjectile>(ProjectileClass, SpawnLocation, CameraTransform.Rotator());

        // Check if the projectile was spawned successfully
        if (Projectile)
        {
            // Customize projectile properties if needed
            // Example: Projectile->SetSpeed(ProjectileSpeed);

            // Play shooting effects or animations if needed
            // Example: PlayShootingEffects();

            // Set the cooldown flag
            bCanShoot = false;
        }
    }
}

// Enable shooting after the cooldown period
void AShooterCharacter::EnableShooting()
{
    bCanShoot = true;
}
