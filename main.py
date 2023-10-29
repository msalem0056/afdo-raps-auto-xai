import streamlit as st
from streamlit.components.v1 import iframe
import subprocess
import sys
from streamlit_server_state import server_state, server_state_lock, no_rerun


with server_state_lock["ed"]:  # Lock the "count" state for thread-safety
    if "ed" not in server_state:
        with no_rerun:
            subprocess.run([f"{sys.executable}", "explainer-dashboard.py"]) #for streamlit  # This does not trigger re-running of other sessions
            server_state.ed = True


def app(title=None)-> None:
    """Creates the streamlit app

    Args:
        title (string, optional): The App name. Defaults to None.
    """
    st.title('ExplainerDashboard')
    st.write("Developer: Mike Salem")
    st.write("The following is an example showcasing XAI using explainer dashboard and streamlit. The `what-if` section allows users to explore different answers for given / new instances. If the box belows says `unable to connect` please click `try again` and wait for it to refresh")
    st.components.v1.iframe("http://127.0.0.1:8050", width=None, height=900, scrolling=True)
    # if not st.session_state['started']:
    #     #subprocess.run(["python", "explainer-dashboard.py", "&"]) 
    #     subprocess.run([f"{sys.executable}", "explainer-dashboard.py"]) #for streamlit
    #     st.session_state['started'] = True      

# Render the ExplainerDashboard in the Streamlit app
if __name__ == "__main__":
    app('ExplainerDashboard')