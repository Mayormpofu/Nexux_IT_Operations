import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="NEXUX | IT Operations",
    page_icon="🖥️",
    layout="wide"
)

st.title("NEXUX")
st.subheader("Enterprise IT Operations Intelligence Platform")

@st.cache_data
def load_data():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "data",
        "tickets.csv"
    )

    return pd.read_csv(
    file_path,
    header=None,
    names=[
        "TicketID",
        "EmployeeName",
        "Department",
        "Category",
        "Priority",
        "Technician",
        "Status",
        "CreatedDate",
        "ResolvedDate",
        "ResolutionHours",
        "SatisfactionScore"
    ]
)


try:

    df = load_data()

    st.success("NEXUX cloud dataset loaded successfully.")
    

    total_tickets = len(df)

    open_tickets = len(
        df[df["Status"] == "Open"]
    )

    resolved_tickets = len(
        df[df["Status"] == "Resolved"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Tickets", total_tickets)
    col2.metric("Open Tickets", open_tickets)
    col3.metric("Resolved Tickets", resolved_tickets)

    st.subheader("Tickets")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

except Exception as error:

    st.error("Unable to load the NEXUX cloud dataset.")

    st.code(str(error))