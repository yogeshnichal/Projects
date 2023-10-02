// Include necessary headers
#include "MyCharacter.h" // Replace with your character class header
#include "Engine/World.h"
#include "GameFramework/PlayerController.h"
#include "GameFramework/Actor.h"

// Sets default values
AMyCharacter::AMyCharacter()
{
    // Set this character to call Tick() every frame
    PrimaryActorTick.bCanEverTick = true;

    // Initialize variables
    bIsCarryingObject = false;
    CarriedObject = nullptr;
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

    // Rotate the carried object if it exists
    if (bIsCarryingObject && CarriedObject)
    {
        RotateCarriedObject();
    }
}

// Called to bind functionality to input
void AMyCharacter::SetupPlayerInputComponent(UInputComponent* PlayerInputComponent)
{
    Super::SetupPlayerInputComponent(PlayerInputComponent);

    // Bind functions to input actions
    PlayerInputComponent->BindAction("Interact", IE_Pressed, this, &AMyCharacter::InteractWithObject);
    PlayerInputComponent->BindAction("RotateObject", IE_Pressed, this, &AMyCharacter::RotateCarriedObject);
}

// Function to interact with objects
void AMyCharacter::InteractWithObject()
{
    // Check if the character is already carrying an object
    if (bIsCarryingObject)
    {
        // Drop the carried object
        DropCarriedObject();
    }
    else
    {
        // Perform a trace to check for objects to pick up
        FHitResult HitResult;
        FVector StartLocation = GetActorLocation();
        FVector EndLocation = StartLocation + (GetActorForwardVector() * InteractionRange);

        // Perform the trace
        if (GetWorld()->LineTraceSingleByChannel(HitResult, StartLocation, EndLocation, ECC_Visibility))
        {
            // Check if the hit actor is interactable
            AActor* HitActor = HitResult.GetActor();
            if (HitActor && HitActor->FindComponentByClass<UInteractableComponent>())
            {
                // Pick up the object
                PickUpObject(HitActor);
            }
        }
    }
}

// Function to pick up an object
void AMyCharacter::PickUpObject(AActor* ObjectToPickUp)
{
    if (ObjectToPickUp)
    {
        // Attach the object to the character's root component
        ObjectToPickUp->AttachToComponent(GetRootComponent(), FAttachmentTransformRules::SnapToTargetIncludingScale);

        // Set the carried object and update the state
        CarriedObject = ObjectToPickUp;
        bIsCarryingObject = true;
    }
}

// Function to drop the carried object
void AMyCharacter::DropCarriedObject()
{
    if (CarriedObject)
    {
        // Detach the object from the character's root component
        CarriedObject->DetachFromActor(FDetachmentTransformRules::KeepWorldTransform);

        // Clear the carried object and update the state
        CarriedObject = nullptr;
        bIsCarryingObject = false;
    }
}

// Function to rotate the carried object
void AMyCharacter::RotateCarriedObject()
{
    if (bIsCarryingObject && CarriedObject)
    {
        // Rotate the object (you can customize the rotation logic)
        FRotator NewRotation = CarriedObject->GetActorRotation() + FRotator(0.0f, RotationSpeed * GetWorld()->GetDeltaSeconds(), 0.0f);
        CarriedObject->SetActorRotation(NewRotation);
    }
}
