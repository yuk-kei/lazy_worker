# User Manual

**Name:** **Lazy worker**

**Version:** Demo 1.0.0



## Content

- [Overview](#overview)  
- [Features](#features )  
- [Instructions](#instructions )  
- [Installation](#installation)
- [Usage](#usage)
- [Copyright](#copyright)  
- [Troubleshooting](#troubleshooting)



## Overview 

The program is a simulation of a warehouse where a worker needs to collect carts from designated locations. The program allows users to customize the map size, the number of carts, and the placement of both the worker and carts. Additionally, the program offers two algorithms to optimize the worker's route - random cart generation and brute force. The program also includes an optional "debug" mode to display useful information during execution.

<div style="text-align:center;">
  <img src="screenshot\1_1.png" alt="start-up screen and menu" style="width:45%;">
  <p style="text-align:center;">Start-up screen and menu</p>
</div> 


## Features 

- Command-line menu:

  Upon starting the application, the user will be presented with a command-line interface (CLI) screen that displays a menu with available options.

  <div style="text-align:center;">
    <img src="screenshot\1_2_0.png" alt="Command-line menu" style="width:50%;">
    <p style="text-align:center;">Command-line menu</p>
  </div> 
  
- Command-line settings UI:

  The application provides a user-friendly command-line interface for configuring the settings of the parking lot simulation.

  <div style="text-align:center;">
    <img src="screenshot\1_3.png" alt="Settings UI" style="width:55%;">
    <p style="text-align:center;">Settings UI</p>
  </div> 

- Live grid display:

  The application displays a live grid that updates at each step of the simulation. The grid shows the current positions of workers and carts, as well as the current path and text instructions.
  
  <div style="text-align:center;">
    <img src="screenshot\1_5.png" alt="Live grid display" style="width:55%;">
    <p style="text-align:center;">Live grid display</p>
  </div> 


### Setting features

- Manual or automated path display:

  The application allows the user to choose between manually or automatically displaying each step of the path.

  <table>
    <tr>
      <td>
        <img src="screenshot\1_6_1.png" alt="Auto mode" width="500" height="250"/><br />
         <p style="text-align: center;">Auto mode</p>
      </td>
      <td>
        <img src="screenshot\1_6_2.png" alt="Manual Mode" width="500" height="250"/><br />
         <p style="text-align: center;">Manual Mode</p>
      </td>
    </tr>
  </table>
  
  
- Adjustable map size:

  The user can adjust the size of the parking lot map from 5x5 to 20x20.

  <div style="text-align:center;">
    <img src="screenshot\1_7.png" alt="Adjustable map size" style="width:60%;">
    <p style="text-align:center;">Adjustable map size</p>
  </div> 

- Set number of carts:

  The user can set the number of carts that will be present on the map.

  <div style="text-align:center;">
    <img src="screenshot\1_8.png" alt="Set number of carts" style="width:65%;">
    <p style="text-align:center;">Set number of carts</p>
  </div> 

- Cart placement:

  The user can manually placing workers and carts on the map. The default positions are random.

  <table>
    <tr>
      <td>
        <img src="screenshot\1_9.png" alt="Auto mode" width="400" height="140"/><br />
         <p style="text-align: center;">Worker position</p>
      </td>
      <td>
        <img src="screenshot\1_10.png" alt="Manual Mode" width="600" height="140"/><br />
         <p style="text-align: center;">Carts position</p>
      </td>
    </tr>
  </table>

- Algorithm selection:

  The user can select between two different algorithms: random cart generation or brute force DFS

  <div style="text-align:center;">
    <img src="screenshot\1_11.png" alt="Set algorithm" style="width:80%;">
    <p style="text-align:center;">Set algorithm</p>
  </div> 

  <table>
    <tr>
      <td>
        <img src="screenshot\1_12_1.png" alt="Random selection" width="550" height="320"/><br />
         <p style="text-align: center;">Random selection</p>
      </td>
      <td>
        <img src="screenshot\1_12_2.png" alt="Brute force DFS" width="550" height="320"/><br />
         <p style="text-align: center;">Brute force DFS</p>
      </td>
    </tr>
  </table>

- Debug mode:

  The application provides an optional "debug" mode that displays useful information during execution, including:
  
  - Current status(auto mode, debug mode, current algorithm)
  - Start point of the worker
  - Current carts positions
  - Total number of steps and the current step taken by the algorithm
  - Comparison of both algorithms running
  
  <div style="text-align:center;">
    <img src="screenshot\1_14.png" alt="Debug Mode" style="width:65%;">
    <p style="text-align:center;">Debug Mode</p>
  </div> 



## Instructions 

1. Open the command prompt or terminal and navigate to the directory where the program files are located.

2. Type the following command to start the program.

   ``` shell
   python lazy_worker.py
   ```

   <div style="text-align:center;">
     <img src="screenshot\1_1.png" alt="start-up screen and menu" style="width:50%;">
     <p style="text-align:center;">Welcome page</p>
   </div> 

3. Press `space` to display the menu

   <div style="text-align:center;">
     <img src="screenshot\1_2.png" alt="start-up screen and menu" style="width:60%;">
     <p style="text-align:center;">Start-up screen and menu</p>
   </div> 

4. Press `2` to access the settings page if you want to customize the worker and cart positions or other settings. Press `r` to return to the main menu after configuring the settings.

   <div style="text-align:center;">
     <img src="screenshot\1_16.png" alt="Setting options" style="width:50%;">
     <p style="text-align:center;">Setting options</p>
   </div> 

5. Press `1` to go to the pathfinding simulation page.

   <div style="text-align:center;">
     <img src="screenshot\1_17.png" alt="Simulation page" style="width:45%;">
     <p style="text-align:center;">Simulation page</p>
   </div> 

6. To start the pathfinding process, press `s`. 

   - If the program is in automatic mode, the results will be displayed shortly

     <div style="text-align:center;">
       <img src="screenshot\1_18_1.png" alt="Auto mode" style="width:55%;">
       <p style="text-align:center;">Auto mode</p>
     </div> 

   - If it is in manual mode, press `space` after each step.

     <div style="text-align:center;">
       <img src="screenshot\1_18_1.png" alt="Manual Mode" style="width:60%;">
       <p style="text-align:center;">Manual Mode</p>
     </div> 

   

7. After the pathfinding process is complete, press `r` to reset the map or `q` to return to the main menu.

   <div style="text-align:center;">
     <img src="screenshot\1_19.png" alt="Return to menu" style="width:60%;">
     <p style="text-align:center;">Return to menu</p>
   </div> 

8. To exit the program, press `3`.

   <div style="text-align:center;">
     <img src="screenshot\1_20.png" alt="Exit" style="width:60%;">
     <p style="text-align:center;">Exit</p>
   </div> 



## Installation 

### System Requirements

To use the program, you need to have a working Python 3 environment installed on your computer. This can be downloaded and installed from the official Python website (https://www.python.org/downloads/).



### Setup & config

1. Download the program files from the source.

2. Extract the files to a directory of your choice.

3. Open a terminal or command prompt and navigate to the directory where the program files are located.

4. Run the program by typing the following command:

   ``` powershell
   python lazy_worker.py
   ```



### Uninstalling

- If your computer has a graphical user interface, simply click the `delete` button as you would when deleting a normal file.

- If you do not have a graphical user interface, navigate to the directory where the file is located and execute the following command:

  - For Linux user

    ``` sh
    rm lazy_worker.py
    ```

  - For Windows server

    ``` powershell
    del lazy_worker.py
    ```



## Copyright

© 2024 JYZ Team. Permission is hereby granted, free of charge, to any person obtaining a copy of this document and associated files, to use, copy, modify, and distribute the document, provided that the above copyright notice and this permission notice appear in all copies. The document is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the document or the use or other dealings in the document.



## Troubleshooting

This section provides solutions for common issues that you may encounter while using our program.

###  Error handling 1: Input error handling

The application has built-in error handling to prevent the user from entering invalid input. If invalid input is entered, the application will provide an error message indicating the issue.

  <div style="text-align:center;">
    <img src="screenshot\1_15.png" alt="Debug Mode" style="width:60%;">
    <p style="text-align:center;">Input error handling</p>
  </div> 


### Issue 1: Program is not responding after starting to get carts

This may be due to the efficiency of the brute force algorithm for finding paths. If the number of carts is more than 10, the algorithm may take a long time to find the desired shortest path. To prevent this, you could:

1. Reduce the number of carts to no more than 10.
2. Grab a coffee and wait patiently.
3. Restart the program.



### Issue 2: Program is freezing

If the program is freezing, please try the following:

1. Check that there are not too many other applications running in the background.
2. Restart the program.
3. Try updating the program to the latest version.



### Bug 1:  Allowing the user to enter a cart number over the maximum limit

The program allows the user to manually enter the number of carts beyond the maximum limit. This can cause unexpected behavior in the program.



### Bug 2:  Allowing the user to enter cart positions outside of the grid

The program allows the user to manually enter cart positions outside of the map. This can cause unexpected behavior in the program.



## Glossary Index

- CLI: Command-line interface. 
- UI: User interface. 
- Brute force DFS: An algorithm that gets the shortest path.

