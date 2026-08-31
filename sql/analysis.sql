create database  NEXUS_IT_OPERATIONS;


USE NEXUS_IT_Operations;
GO

/* =========================================
   NEXUS — IT OPERATIONS ANALYTICS
   ========================================= */


/* 1. Total Tickets */
SELECT 
    COUNT(*) AS TotalTickets
FROM Tickets;


/* 2. Open Tickets */
SELECT 
    COUNT(*) AS OpenTickets
FROM Tickets
WHERE Status = 'Open';


/* 3. Resolved Tickets */
SELECT 
    COUNT(*) AS ResolvedTickets
FROM Tickets
WHERE Status = 'Resolved';


/* 4. Tickets by Category */
SELECT
    Category,
    COUNT(*) AS TicketCount
FROM Tickets
GROUP BY Category
ORDER BY TicketCount DESC;


/* 5. Tickets by Priority */
SELECT
    Priority,
    COUNT(*) AS TicketCount
FROM Tickets
GROUP BY Priority
ORDER BY TicketCount DESC;


/* 6. Tickets by Department */
SELECT
    Department,
    COUNT(*) AS TicketCount
FROM Tickets
GROUP BY Department
ORDER BY TicketCount DESC;


/* 7. Tickets by Status */
SELECT
    Status,
    COUNT(*) AS TicketCount
FROM Tickets
GROUP BY Status
ORDER BY TicketCount DESC;


/* 8. Average Resolution Time */
SELECT
    AVG(ResolutionHours) AS AverageResolutionHours
FROM Tickets
WHERE Status = 'Resolved';


/* 9. SLA Breaches */
SELECT
    COUNT(*) AS SLABreaches
FROM Tickets
WHERE ResolutionHours > 8;


/* 10. SLA Compliance */
SELECT
    CASE
        WHEN ResolutionHours > 8 THEN 'SLA Breach'
        ELSE 'Within SLA'
    END AS SLAStatus,
    COUNT(*) AS TicketCount
FROM Tickets
WHERE ResolutionHours IS NOT NULL
GROUP BY
    CASE
        WHEN ResolutionHours > 8 THEN 'SLA Breach'
        ELSE 'Within SLA'
    END;


/* 11. Technician Performance */
SELECT
    Technician,
    COUNT(*) AS ResolvedTickets,
    AVG(ResolutionHours) AS AvgResolutionHours
FROM Tickets
WHERE Status = 'Resolved'
GROUP BY Technician
ORDER BY ResolvedTickets DESC;


/* 12. Technician Ranking */
SELECT
    Technician,
    COUNT(*) AS ResolvedTickets,
    RANK() OVER (
        ORDER BY COUNT(*) DESC
    ) AS PerformanceRank
FROM Tickets
WHERE Status = 'Resolved'
GROUP BY Technician;


/* 13. Average Satisfaction */
SELECT
    AVG(
        CAST(SatisfactionScore AS DECIMAL(10,2))
    ) AS AverageSatisfaction
FROM Tickets
WHERE SatisfactionScore IS NOT NULL;


/* 14. Category Resolution Performance */
SELECT
    Category,
    COUNT(*) AS TotalTickets,
    AVG(ResolutionHours) AS AvgResolutionHours
FROM Tickets
WHERE ResolutionHours IS NOT NULL
GROUP BY Category
ORDER BY AvgResolutionHours DESC;


/* 15. Critical Tickets */
SELECT
    TicketID,
    EmployeeName,
    Department,
    Category,
    Technician,
    Status
FROM Tickets
WHERE Priority = 'Critical';


/* 16. High Priority Open Tickets */
SELECT
    TicketID,
    EmployeeName,
    Department,
    Category,
    Technician
FROM Tickets
WHERE Priority IN ('Critical', 'High')
AND Status = 'Open';


/* 17. Department Resolution Performance */
SELECT
    Department,
    COUNT(*) AS ResolvedTickets,
    AVG(ResolutionHours) AS AvgResolutionHours
FROM Tickets
WHERE Status = 'Resolved'
GROUP BY Department
ORDER BY AvgResolutionHours;


/* 18. CTE — Technician Performance */
WITH TechnicianStats AS
(
    SELECT
        Technician,
        COUNT(*) AS ResolvedTickets,
        AVG(ResolutionHours) AS AvgResolutionHours
    FROM Tickets
    WHERE Status = 'Resolved'
    GROUP BY Technician
)
SELECT
    Technician,
    ResolvedTickets,
    AvgResolutionHours,
    RANK() OVER (
        ORDER BY ResolvedTickets DESC
    ) AS TechnicianRank
FROM TechnicianStats;


/* 19. Overall Operational Summary */
SELECT
    COUNT(*) AS TotalTickets,
    SUM(CASE WHEN Status = 'Open' THEN 1 ELSE 0 END) AS OpenTickets,
    SUM(CASE WHEN Status = 'In Progress' THEN 1 ELSE 0 END) AS InProgressTickets,
    SUM(CASE WHEN Status = 'Resolved' THEN 1 ELSE 0 END) AS ResolvedTickets,
    AVG(ResolutionHours) AS AvgResolutionHours,
    AVG(
        CAST(SatisfactionScore AS DECIMAL(10,2))
    ) AS AvgSatisfaction
FROM Tickets;


/* 20. Ticket Risk Classification */
SELECT
    TicketID,
    Category,
    Priority,
    Status,
    ResolutionHours,

    CASE
        WHEN Status = 'Open'
             AND Priority = 'Critical'
            THEN 'CRITICAL ACTION REQUIRED'

        WHEN Status = 'Open'
             AND Priority = 'High'
            THEN 'HIGH PRIORITY'

        WHEN ResolutionHours > 8
            THEN 'SLA RISK'

        ELSE 'NORMAL'
    END AS OperationalRisk

FROM Tickets;