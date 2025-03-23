import streamlit as st

# Initialize session state for tasks if not already set
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Title and description
st.title("Eisenhower Matrix")
st.write("A tool to help you prioritize tasks using the Eisenhower Matrix method.")

# Task input form
st.subheader("Add a Task")
task_name = st.text_input("Task Name")
task_description = st.text_area("Task Description")

# Quadrant selection
quadrant = st.radio(
    "Choose a quadrant for the task:",
    ("Urgent & Important", "Not Urgent & Important", "Urgent & Not Important", "Not Urgent & Not Important")
)

# Button to add task
if st.button("Add Task"):
    if task_name:
        st.session_state.tasks.append({
            "name": task_name,
            "description": task_description,
            "quadrant": quadrant
        })
        st.success(f"Task '{task_name}' added to the '{quadrant}' quadrant!")
    else:
        st.error("Please enter a task name.")

# Display Eisenhower Matrix in a 2x2 grid
st.subheader("Your Eisenhower Matrix")
# Eisenhower Matrix Light System
st.markdown("""
| Quadrant                                    | Color  | Meaning                                                  | Action                                  |
|---------------------------------------------|--------|----------------------------------------------------------|-----------------------------------------|
| 🟢 Urgent & Important         | Green  | Do First - Critical tasks with deadlines or serious consequences.   | **Do these immediately.**              |
| 🔵 Not Urgent & Important     | Blue   | Plan - Important tasks that require planning but aren’t time-sensitive. | **Schedule these for later.**      |
| 🟡 Urgent & Not Important     | Yellow | Delegate - Tasks that feel urgent but don’t require your direct involvement. | **Delegate these to someone else.** |
| 🔴 Not Urgent & Not Important | Red    | Eliminate - Distractions or time-wasting tasks.                      | **Consider eliminating or reducing these.** |
""")

# Define quadrant mappings
quadrants = {
    "Urgent & Important": "🟢",
    "Not Urgent & Important": "🔵",
    "Urgent & Not Important": "🟡",
    "Not Urgent & Not Important": "🔴"
}

# Create a 2x2 grid using Streamlit columns
col1, col2 = st.columns(2)

# Function to display tasks in a styled way
def display_tasks(quadrant_name):
    tasks_in_quadrant = [task for task in st.session_state.tasks if task["quadrant"] == quadrant_name]
    if tasks_in_quadrant:
        for task in tasks_in_quadrant:
            st.markdown(
                f"""
                <div style='border: 1px solid #ccc; border-radius: 10px; padding: 10px; margin: 5px; background-color: #f9f9f9;'>
                    <b>{task['name']}</b><br>
                    <i>{task['description']}</i>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("*No tasks yet.*")

# Display tasks in the appropriate columns
with col1:
    st.markdown(f"### {quadrants['Urgent & Important']}")
    display_tasks("Urgent & Important")

    st.markdown(f"### {quadrants['Urgent & Not Important']}")
    display_tasks("Urgent & Not Important")

with col2:
    st.markdown(f"### {quadrants['Not Urgent & Important']}")
    display_tasks("Not Urgent & Important")

    st.markdown(f"### {quadrants['Not Urgent & Not Important']}")
    display_tasks("Not Urgent & Not Important")
