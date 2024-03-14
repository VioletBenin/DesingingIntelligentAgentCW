# UoN_Graduation_Project

Dissertation and Graduation Design of Master's degree in University of Nottingham, using as many skills as possible to complete it. 

## 🛞Techs

### Compulsory

### Possible

## Phrase A: Coursework of Designing Intelligent Agent - An Intelligent Vehicle-Road System

This project will focus on managing a stream of hundreds of intelligent vehicles within the city. The simulation will take place in a randomly generated 2D environment with numerous roads. The main task is to schedule roads in such a way that each vehicle, guided by my agent, appears at random at the intersection of a boundary and a road. The vehicles must follow the roads until they reach their randomly assigned destinations at other intersections. Should the agent determine that a vehicle cannot reach its destination, it will notify virtual law enforcement to remove the vehicle to prevent traffic congestion at the region's entrances. The initial phase involves building a very simple prototype. Subsequent phases may incorporate additional features such as machine learning, advanced algorithms, and interaction with real traffic patterns. Ultimately, the project could utilize actual urban data, and the representation might evolve into a 3D model to reflect the multi-layered road systems in large cities, which manage vehicle flows at varying speeds. The severe traffic congestion during peak hours in my hometown has inspired me to tackle this challenge. This work may also provide insights for urban-rural planning researchers.

## Phrase B : Graduation Project

### Choices

- Access to real data (Preferance)
- Vehicles with NLP
- 3D modeling in VR world
- Advanced algorithms and machine learning 
- Data visualization at management dashboard

## 🛠️ Installation

Install the remaining dependencies:
```
python -m pip install -r requirements.txt
```
### 🔎 Unit tests 
Run the tests using :
```
pytest tests/
```

While the project will grow, more test will be added and you'll maybe need to just select a subset of tests related to the changes you made by using the `-k` option of `pytest`. Running tests in parallel (in the example 4 processes) with the `-n` option may help :

```
pytest -k "substring-to-match" -n 4 tests/
```
