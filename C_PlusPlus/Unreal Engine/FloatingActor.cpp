// FloatingActor.h

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "FloatingActor.generated.h"

UCLASS()
class YOURPROJECT_API AFloatingActor : public AActor
{
    GENERATED_BODY()

public:
    // Sets default values for this actor's properties
    AFloatingActor();

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

private:
    // The floating object's mesh
    UPROPERTY(VisibleAnywhere)
    UStaticMeshComponent* MeshComponent;

    // Parameters for floating behavior
    UPROPERTY(EditAnywhere)
    float FloatAmplitude;

    UPROPERTY(EditAnywhere)
    float FloatFrequency;

    FVector InitialLocation;
};
