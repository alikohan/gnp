# Genetic Network Programming (GNP)

This repository provides a Python implementation of the research paper **“Towards Self-Evolving Agents: A Human-Inspired Adaptive Exploration-Exploitation Framework for Genetic Network Programming”**. The project focuses on enhancing Genetic Network Programming (GNP) by introducing a human-behavior-inspired adaptive mechanism that dynamically balances exploration and exploitation during evolution.

## 📌 Overview

Genetic Network Programming (GNP) is an evolutionary computation method where candidate solutions are represented as directed graph structures rather than linear strings of traditional genetic algorithms or tree structures of genetic programming. GNP’s graph encoding allows for compact representation and reuse of nodes, which enhances the expressiveness and efficiency of solutions in dynamic and complex problem domains.

This project extends standard GNP by integrating adaptive mechanisms that adapt exploration and exploitation during evolution, rather than relying on fixed parameters.


| File / Module                | Description                                                   |
| ---------------------------- | ------------------------------------------------------------- |
| `GNP.py`                     | Standard Genetic Network Programming                                    |
| `HGNP.py`                    | Human-Inspired GNP with dynamic exploration-exploitation adjustment           |
| `SBGNP.py`                   | Situation-Based GNP variant (for comparison)                       |
| `simplifiedGNP.py`           | Simplified GNP with restricted operators (for comparison)               |
| `simplifiedGNP-HGNP.py`      | Simplified GNP integrated with HGNP                                     |
| `SBGNP-HGNP.py`              | SBGNP integrated with HGNP                                              |
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

Example: Run the Human-Inspired GNP (HGNP)
```bash
python HGNP.py
```

This executes the adaptive algorithm and prints progress and results to the console. It also generates two Excel files (.xlsx) and a text file (.txt) to log detailed progress and final outputs.
Modify parameters in variables.py to adjust behavior.

### Visualizing the Result on the Tileworld Environment

```bash
python visualize.py
```
## Some Examples


https://github.com/user-attachments/assets/e0715785-6256-404f-875b-5212548717a3



https://github.com/user-attachments/assets/8b0e92a6-95e0-465f-896f-9d6a7f7dc893



https://github.com/user-attachments/assets/1c9a632a-a1e7-4664-bfd4-c05e1d03e97d
