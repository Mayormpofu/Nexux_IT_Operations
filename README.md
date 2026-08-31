# Nexux_IT_Operations
# NEXUS — Enterprise IT Operations Intelligence Platform

NEXUS is an enterprise-style IT Operations Intelligence Platform designed to analyze IT service desk activity, monitor operational performance, identify SLA breaches, and provide actionable insights through a professional analytics dashboard.

## 🎯 Project Overview

NEXUS simulates a real-world IT operations environment where service desk tickets are stored and analyzed using Microsoft SQL Server and presented through a web-based dashboard.

The platform provides insights into:

- IT ticket volumes
- Support categories
- Ticket priorities
- Technician performance
- Resolution times
- SLA compliance
- Department support demand
- User satisfaction

## 🛠️ Technology Stack

- Microsoft SQL Server — Database and data analysis
- SQL — Data querying and analytics
- HTML5 — Dashboard structure
- CSS3 — User interface design
- JavaScript — Dashboard functionality
- Git — Version control
- GitHub — Source code and project management

## 📊 Key Features

### IT Operations Analytics

- Total ticket monitoring
- Open and resolved ticket analysis
- Ticket categorization
- Priority analysis
- Department-level reporting

### SLA Monitoring

- Average resolution time
- SLA breach identification
- SLA performance analysis
- Resolution-time tracking

### Technician Performance

- Tickets resolved by technician
- Average resolution time
- Technician performance ranking

### User Satisfaction

- Average satisfaction score
- Satisfaction analysis by operational performance

### Executive Dashboard

- Key Performance Indicators (KPIs)
- Operational overview
- Ticket distribution
- Technician performance
- SLA monitoring

## 🗄️ Database

NEXUS uses Microsoft SQL Server as its relational database.

### Tickets Table

| Field | Description |
|---|---|
| TicketID | Unique ticket identifier |
| EmployeeName | Employee who submitted the ticket |
| Department | Employee department |
| Category | Type of IT issue |
| Priority | Ticket priority |
| Technician | Assigned IT technician |
| Status | Current ticket status |
| CreatedDate | Ticket creation date |
| ResolvedDate | Resolution date |
| ResolutionHours | Time required to resolve |
| SatisfactionScore | User satisfaction rating |

## 🧠 SQL Techniques Demonstrated

- SELECT statements
- WHERE filtering
- GROUP BY
- ORDER BY
- Aggregate functions
- COUNT()
- AVG()
- CASE statements
- Common Table Expressions (CTEs)
- Window functions
- RANK()
- Date calculations
- Conditional analysis
- KPI calculations
- SLA analysis

## 📈 Business Questions Answered

1. How many IT tickets have been received?
2. How many tickets remain open?
3. Which IT issue category occurs most frequently?
4. Which departments generate the most support requests?
5. Which technician resolves the most tickets?
6. What is the average ticket resolution time?
7. How many tickets breach the SLA?
8. What is the average user satisfaction score?
9. Which ticket categories take the longest to resolve?
10. Which areas of IT operations require the most attention?

## 🔄 Data Flow

```text
IT Service Desk Data
        ↓
Microsoft SQL Server
        ↓
SQL Analysis
        ↓
Operational KPIs
        ↓
NEXUS Dashboard
        ↓
Business Insights
