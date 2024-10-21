# 3D Object Visualization with Pygame

## Description
This project is a Python application for visualizing 3D objects using the Pygame library. The program implements basic 3D geometry, including the rotation and translation of objects like cubes and tori. The graphical output is displayed on a 2D screen, and the rotation of objects can be controlled using the keyboard.

## Features
- **3D Object Rendering**: Supports rendering of various 3D objects such as cubes and tori.
- **Object Rotation**: The objects can be rotated in 3D space using Euler angles (alpha, beta, and gamma) which represent yaw, pitch, and roll.
- **Pygame Integration**: Uses Pygame to display the 3D objects on a 2D screen.
- **Key Controls**: Allows for manual control of object rotation using the `W`, `A`, `S`, `D`, `Q`, and `E` keys.

## Installation
1. Clone the repository or download the files.
2. Install the required dependencies:
   ```bash
   pip install pygame numpy
   ```
3. Run the `main.py` file:
   ```bash
   python main.py
   ```

## File Structure

### 1. `main.py`
The main script that initializes the Pygame window, handles user input, and renders the objects on the screen.

- Initializes a Pygame window of 600x600 pixels.
- Controls object rotation through keyboard inputs.
- Uses Pygame's `display.flip()` to update the screen with each frame.
  
### 2. `objects.py`
Defines the objects to be rendered in 3D space. Key objects include:
- **Object (Base Class)**: Defines the basic properties of an object, such as vertices, edges, and methods for rotating and drawing.
- **Cube**: A subclass of `Object` that defines the vertices and edges for a cube.
- **Torus**: Another subclass representing a torus, with specific vertices and edges generation logic.

### 3. `transformations.py`
Contains the transformation functions applied to the 3D objects, including:
- **Translation**: Moves the object in space.
- **Rotation**: Rotates the object using Euler angles (alpha, beta, gamma).
- **XY Projection**: Projects the 3D object onto a 2D plane for rendering.

## Controls
- `W`/`S`: Rotate around the X-axis (pitch).
- `A`/`D`: Rotate around the Y-axis (yaw).
- `Q`/`E`: Rotate around the Z-axis (roll).

## Future Improvements
- Add more complex 3D objects and shapes.
- Implement object scaling and interactive zooming.
- Include more user interaction and visual effects.

## License
This project is open-source and available under the MIT License.
