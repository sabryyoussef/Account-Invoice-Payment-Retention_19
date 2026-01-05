# Use Case: Project Schedule Management

## Overview
This document covers use cases for creating, managing, and approving project schedules (Gantt charts) which define the official timeline with activity sequence and dependencies.

---

## Use Case 2.1: Create Project Schedule with Activities

### Scenario
A project manager needs to create a detailed project schedule with multiple activities, dependencies, and timelines for a construction project.

### Steps

#### Step 1: Navigate to Project Schedule
1. Go to **TPO Management > Pre-Execution & Planning > Project Schedule**
2. Click **Create**

#### Step 2: Fill Schedule Header
1. **Schedule Name**: Enter name (e.g., `Al-Riyadh Tower - Main Schedule`)
2. **Project**: Select the project
3. **Date**: Set schedule creation date
4. **Project Manager**: Assign project manager
5. **Planner**: Assign person who created the schedule
6. **Baseline Date**: Set baseline date for tracking
7. **Planned Start Date**: Enter project start date
8. **Planned End Date**: Enter project end date
9. **Description**: Add schedule notes

#### Step 3: Add Schedule Activities
1. Click **Activities** tab
2. Click **Add a line**
3. For each activity, fill:
   - **Activity Name**: e.g., `Site Preparation`
   - **Planned Start Date**: Activity start
   - **Planned End Date**: Activity end
   - **Duration**: Auto-calculated in days
   - **Predecessors**: Select preceding activities (if any)
   - **Critical Path**: Check if activity is on critical path
   - **Description**: Activity details

#### Step 4: Save and Submit
1. Click **Save**
2. Review all activities
3. Click **Submit** for approval

### Expected Result
- Complete project schedule with all activities
- Timeline visualization ready
- Schedule ready for approval

---

## Use Case 2.2: Update Schedule Progress

### Scenario
Track actual progress against planned schedule and update activity completion.

### Steps
1. Open approved schedule
2. Update activity **Actual Start Date** and **Actual End Date**
3. Mark activities as completed
4. Compare planned vs actual dates

---

## Related Use Cases
- [Project Setup](../01_project_management/project_setup.md)

