# student-placement-dashboard
Power BI + Python clinical placement optimization dashboard
# Student Placement Optimization Dashboard

## Overview
This project simulates a clinical placement optimization workflow using Python and Power BI.

Students are assigned to clinical sites based on region preference and site capacity constraints. The results are then visualized in an interactive dashboard to monitor placement efficiency, utilization, and remaining capacity.

This mirrors real-world healthcare and operations analytics use cases.

---

## Dashboard Preview

![Dashboard Preview](images/dashboard_preview.png)

---

## Tech Stack
- Python (pandas)
- Power BI
- DAX measures
- CSV datasets
- Git/GitHub

---

## Workflow

### 1. Data Generation (Python)
A Python script assigns students to available clinical sites:
- respects region preference
- checks capacity limits
- outputs placements.csv

File:
scripts/placement_logic.py

### 2. Data Modeling (Power BI)
- students, sites, and placements tables
- relational star schema
- one-to-many relationships

### 3. Dashboard
Includes:
- KPI cards (total students, placed, rate, remaining capacity)
- placements by region
- placements by program
- site-level capacity table
- interactive slicers (filters)

---

## Results
- 150 students
- 141 placed
- 94% placement rate
- 23 seats remaining capacity

---

## Project Structure
student-placement-dashboard
│
├── data/
├── scripts/
├── powerbi/
├── images/
└── README.md

---

## Author
Rich Mansfield
