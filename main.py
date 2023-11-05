import streamlit as st
import streamlit.components.v1 as components
import sys
from streamlit_server_state import server_state, server_state_lock, no_rerun



def app(title=None)-> None:
    """Creates the streamlit app

    Args:
        title (string, optional): The App name. Defaults to None.
    """
    st.set_page_config(layout="wide")
    st.title('ExplainerDashboard')
    st.markdown("### Developer: Mike Salem [Linked In](https://www.linkedin.com/in/mike-salem)")
    st.write("The following is an example showcasing XAI using explainer dashboard and streamlit. The `what-if` section allows users to explore different answers for given / new instances. If the box belows says `unable to connect` please click `try again` and wait for it to refresh")
    tab_files = ["./explainerhub/dashboard1.html", "./explainerhub/dashboard2.html",]
    t1, t2 = st.tabs(['Breast Cancer Dataset', 'Diabetes Dataset'])
    for tab,name in zip([t1,t2], tab_files):
        with tab:
            HtmlFile = open(name, 'r', encoding='utf-8')
            source_code = HtmlFile.read() 
            print(source_code)
            components.html(source_code, height = 900, width = None, scrolling=True)

# Render the ExplainerDashboard in the Streamlit app
if __name__ == "__main__":
    app('ExplainerDashboard')