# this file can be called inside app.py file
#it wil take density, avg_sugar_per_gramf from image recognition mode and  volume_liters from volume estimation model


def calculate_sugar_content(density, avg_sugar_per_gram, volume_liters):
    """
    Calculate the sugar content of a food item based on its density, average sugar per gram, and volume.
    
    Parameters:
    density (float): Density of the food item in grams per cubic centimeter.
    avg_sugar_per_gram (float): Average sugar per gram of the food item in grams.
    volume_liters (float): Volume of the food item in liters.

    Returns:
    float: Total sugar content in grams.
    """
    # Convert volume from liters to cubic centimeters
    volume_cc = volume_liters * 1000  # 1 liter = 1000 cubic centimeters

    # Calculate weight
    weight_grams = volume_cc * density

    # Calculate total sugar content
    total_sugar_content = weight_grams * avg_sugar_per_gram

    return total_sugar_content

def main():
    # Get user input
    try:
        # the three below will be take from image recognition and volume estimation model wused in oour model . change can be made acordingly
        density = float(input("Enter the density of the food item (g/cm³): "))
        avg_sugar_per_gram = float(input("Enter the average sugar per gram of the food item (g/g): "))
        volume_liters = float(input("Enter the volume of the food item (liters): "))

        # Calculate sugar content
        total_sugar_content = calculate_sugar_content(density, avg_sugar_per_gram, volume_liters)
        
        # Display result
        print(f"Total sugar content in the food item: {total_sugar_content:.2f} grams")
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
