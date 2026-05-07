# Genetic Network Programming (GNP)

This repository provides a Python implementation of the research paper **“Towards Self-Evolving Agents: A Human-Inspired Adaptive Exploration-Exploitation Framework for Genetic Network Programming”**. The project focuses on enhancing Genetic Network Programming (GNP) by introducing a human-behavior-inspired adaptive mechanism that dynamically balances exploration and exploitation during evolution.

## 📌 Overview

Genetic Network Programming (GNP) is an evolutionary computation method where candidate solutions are represented as directed graph structures rather than linear strings of traditional genetic algorithms or tree structures of genetic programming. GNP’s graph encoding allows for compact representation and reuse of nodes, which enhances the expressiveness and efficiency of solutions in dynamic and complex problem domains.

This project extends standard GNP by integrating adaptive mechanisms that adapt exploration and exploitation during evolution, rather than relying on fixed parameters.


| File / Module                | Description                                                   |
| ---------------------------- | ------------------------------------------------------------- |
| `GNP.py`                     | Standard Genetic Network Programming                                    |
| `AGNP.py`                    | Advanced GNP with dynamic exploration-exploitation adjustment           |
| `SBGNP.py`                   | Situation-Based GNP variant (for comparison)                       |
| `simplifiedGNP.py`           | Simplified GNP with restricted operators (for comparison)               |
| `simplifiedGNP-AGNP.py`      | Simplified GNP integrated with AGNP                                     |
| `SBGNP-AGNP.py`              | SBGNP integrated with AGNP                                              |
| `visualize.py`               | Visualization function to monitor agent behavior on Tileworld benchmark |
| `tile_world_instructions.py` | GNP judgement and processing node functions in Tileworld for visualization                  |
| `GA_tile_world_instructions.py` | GNP judgement and processing node functions in Tileworld for GA            |
| `common_instructions.py`    | Common utility functions used in fitness function and Tileworld for visualization    |
| `GA_common_instructions.py` | Common utility functions used in fitness function and Tileworld for GA      |
| `variables.py`               | constants and configurations                                            |
| `requirements.txt`           | Python dependencies                                                     |


---

## Getting Started

### Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

### Running Algorithm

Example: Run the advanced GNP (AGNP)
```bash
python AGNP.py
```

This executes the adaptive algorithm and prints progress and results to the console. It also generates two Excel files (.xlsx) and a text file (.txt) to log detailed progress and final outputs.
Modify parameters in variables.py to adjust behavior.

### Visualizing the Result on the Tileworld Environment

```bash
python visualize.py
```
## Some Examples


https://github.com/user-attachments/assets/35727baf-2b25-4476-b0c7-aca7cfe8bc61



https://github.com/user-attachments/assets/baf2b9d6-1c73-4d28-8e6a-7c787302da72



https://github.com/user-attachments/assets/a1a7f320-92af-4469-81dc-94721d458085

