# kids-activity-tracker
Modular full-stack activity tracker for kids using Python, SQL, and Tableau

# 🧒 Kids Activity Tracker & Dashboard Suite

A modular full-stack system to help parents and kids track chores and physical activity using Python, SQL, Tableau, and a Raspberry Pi-powered touchscreen interface.

This project was designed to:
- Motivate kids to complete daily tasks and stay active
- Give parents simple visual tools for tracking progress
- Serve as a portfolio-worthy integration of modern data engineering tools

---

## 📁 Project Structure

```plaintext
kids-activity-tracker/
├── chore-collector/         # Python CLI or Web form
│   └── app.py
├── sql-engine/              # SQL schema + queries
│   ├── schema.sql
│   └── queries/reward_summary.sql
├── tableau-dashboard/       # Tableau dashboards (twb/twbx)
│   └── dashboards/
├── automation-engine/       # Python scripts for weekly summaries
│   └── weekly_summary.py
├── touchscreen-ui/          # Streamlit or Flask UI
│   └── main.py
├── data/                    # Sample input and cleaned datasets
│   ├── raw/
│   └── processed/
├── docs/                    # ERD diagram, UI mockups
│   └── erd.png
├── requirements.txt         # Python dependencies
└── README.md                # You're here

