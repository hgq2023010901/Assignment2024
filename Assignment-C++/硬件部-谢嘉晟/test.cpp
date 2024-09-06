#include <iostream>
#include <cmath> // Include the math library

int main() {
    // Define the radius of the circle
    double radius = 5.0;

    // Calculate the area of the circle
    double area = M_PI * std::pow(radius, 2); // M_PI is a constant for PI, pow is used for squaring

    // Output the result
    std::cout << "The area of the circle with radius " << radius << " is " << area << std::endl;

    return 0;
}