import streamlit as st
import pandas as pd
import pyodbc

# --------------------------------------------------
# NEXUS — IT OPERATIONS INTELLIGENCE PLATFORM
# --------------------------------------------------

st.set_page_config(
    page_title="NEXUS | IT Operations",
    page_icon="🖥️",
    layout="wide"
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

SERVER = r"DESKTOP-SBQ9F91\SQLDEV2025"
DATABASE = "NEXUS_IT_Operations"

CONNECTION_STRING = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;"
)

@st.cache_resource
def get_connection():
    return pyodbc.connect(CONNECTION_STRING)


@st.cache_data
def load_data():

    connection = get_connection()

    query = """
        SELECT
            TicketID,
            EmployeeName,
            Department,
            Category,
            Priority,
            Technician,
            Status,
            CreatedDate,
            ResolvedDate,
            ResolutionHours,
            SatisfactionScore
        FROM Tickets
    """

    return pd.read_sql(query, connection)


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

try:

    df = load_data()

    # --------------------------------------------------
    # SIDEBAR
    # --------------------------------------------------

    st.sidebar.title("NEXUS")
    st.sidebar.caption("IT Operations Intelligence")

    st.sidebar.divider()

    st.sidebar.subheader("Filters")

    department_filter = st.sidebar.multiselect(
        "Department",
        sorted(df["Department"].unique())
    )

    priority_filter = st.sidebar.multiselect(
        "Priority",
        sorted(df["Priority"].unique())
    )

    status_filter = st.sidebar.multiselect(
        "Status",
        sorted(df["Status"].unique())
    )

    filtered_df = df.copy()

    if department_filter:
        filtered_df = filtered_df[
            filtered_df["Department"].isin(department_filter)
        ]

    if priority_filter:
        filtered_df = filtered_df[
            filtered_df["Priority"].isin(priority_filter)
        ]

    if status_filter:
        filtered_df = filtered_df[
            filtered_df["Status"].isin(status_filter)
        ]

    # --------------------------------------------------
    # HEADER
    # --------------------------------------------------

    st.title("NEXUS")
    st.subheader("Enterprise IT Operations Intelligence Platform")

    st.caption(
        "Real-time service desk monitoring, operational analytics "
        "and technician performance intelligence."
    )

    st.divider()

    # --------------------------------------------------
    # KPIs
    # --------------------------------------------------

    total_tickets = len(filtered_df)

    open_tickets = len(
        filtered_df[filtered_df["Status"] == "Open"]
    )

    resolved_tickets = len(
        filtered_df[filtered_df["Status"] == "Resolved"]
    )

    avg_resolution = filtered_df["ResolutionHours"].mean()

    sla_breaches = len(
        filtered_df[filtered_df["ResolutionHours"] > 8]
    )

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Tickets", total_tickets)

    col2.metric("Open Tickets", open_tickets)

    col3.metric("Resolved Tickets", resolved_tickets)

    col4.metric(
        "Avg Resolution",
        f"{avg_resolution:.1f} hrs"
    )

    col5.metric(
        "SLA Breaches",
        sla_breaches
    )

    st.divider()

    # --------------------------------------------------
    # ANALYTICS
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Tickets by Category")

        category_data = (
            filtered_df["Category"]
            .value_counts()
        )

        st.bar_chart(category_data)

    with col2:

        st.subheader("Tickets by Priority")

        priority_data = (
            filtered_df["Priority"]
            .value_counts()
        )

        st.bar_chart(priority_data)

    # --------------------------------------------------
    # DEPARTMENT
    # --------------------------------------------------

    st.subheader("Tickets by Department")

    department_data = (
        filtered_df["Department"]
        .value_counts()
    )

    st.bar_chart(department_data)

    # --------------------------------------------------
    # TECHNICIAN PERFORMANCE
    # --------------------------------------------------

    st.subheader("Technician Performance")

    technician_data = (
        filtered_df[
            filtered_df["Status"] == "Resolved"
        ]
        .groupby("Technician")
        .agg(
            ResolvedTickets=("TicketID", "count"),
            AvgResolutionHours=(
                "ResolutionHours",
                "mean"
            )
        )
        .sort_values(
            "ResolvedTickets",
            ascending=False
        )
    )

    st.dataframe(
        technician_data,
        use_container_width=True
    )

    # --------------------------------------------------
    # SERVICE DESK
    # --------------------------------------------------

    st.subheader("Service Desk Tickets")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )

    # --------------------------------------------------
    # SYSTEM STATUS
    # --------------------------------------------------

    st.divider()

    st.success(
        "● NEXUS operational — SQL Server connection active"
    )

except Exception as error:

    st.error(
        "Unable to connect to the NEXUS SQL Server database."
    )

    st.code(str(error))