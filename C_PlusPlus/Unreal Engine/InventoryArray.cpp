// Include necessary headers
#include "InventorySystem.h" // Replace with your project's header file
#include "InventoryItem.h" // Replace with the header for your item class
#include "Engine/World.h"

// Sets default values
AInventorySystem::AInventorySystem()
{
    // Set this actor to call Tick() every frame
    PrimaryActorTick.bCanEverTick = false;
}

// Called when the game starts or when spawned
void AInventorySystem::BeginPlay()
{
    Super::BeginPlay();

    // Initialize the inventory array
    Inventory.Empty();
}

// Function to add an item to the inventory
bool AInventorySystem::AddItemToInventory(AInventoryItem* Item)
{
    if (Item)
    {
        // Check if the item is stackable and if it already exists in the inventory
        if (Item->IsStackable())
        {
            for (FInventorySlot& Slot : Inventory)
            {
                if (Slot.ItemClass == Item->GetClass())
                {
                    Slot.Quantity += 1;
                    return true; // Item added to existing stack
                }
            }
        }

        // If not stackable or not found in inventory, add a new slot
        FInventorySlot NewSlot;
        NewSlot.ItemClass = Item->GetClass();
        NewSlot.Quantity = 1;
        Inventory.Add(NewSlot);

        return true; // Item added to a new slot
    }

    return false; // Item is invalid
}

// Function to remove an item from the inventory
bool AInventorySystem::RemoveItemFromInventory(AInventoryItem* Item, int32 Quantity)
{
    if (Item)
    {
        // Find the item in the inventory
        for (FInventorySlot& Slot : Inventory)
        {
            if (Slot.ItemClass == Item->GetClass())
            {
                // Check if there are enough items to remove
                if (Slot.Quantity >= Quantity)
                {
                    Slot.Quantity -= Quantity;

                    // Remove the slot if the quantity reaches zero
                    if (Slot.Quantity <= 0)
                    {
                        Inventory.Remove(Slot);
                    }

                    return true; // Item removed
                }
                else
                {
                    return false; // Not enough items to remove
                }
            }
        }
    }

    return false; // Item is invalid or not found
}
