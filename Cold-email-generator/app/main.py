import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def apply_custom_styles():
    st.markdown(
        """
        <style>
        /* Change background to black */
        .main {
            background-color: #000000;
            color: #ffffff;
        }
        /* Adjust sidebar background */
        [data-testid="stSidebar"] {
            background-color: #1c1c1c;
            color: #ffffff;
        }
        /* Adjust font color for headers and text */
        h1, h2, h3, h4, h5, h6, p, div, span, label {
            color: #ffffff !important;
        }
        /* Adjust code block appearance */
        pre {
            background-color: #333333 !important;
            color: #ffffff !important;
            white-space: pre-wrap !important;
            word-wrap: break-word !important;
            overflow-x: auto !important; /* Allow horizontal scrolling */
            padding: 1rem !important; /* Add padding for better readability */
        }
        /* Button Styling */
        div.stButton > button {
            background-color: #000000 !important;
            color: #ffffff !important;
            border: 1px solid #ffffff !important;
            border-radius: 8px !important;
            padding: 0.5rem 1rem !important;
            font-size: 16px !important;
        }
        div.stButton > button:hover {
            background-color: #333333 !important;
            color: #ffffff !important;
        }
        /* Make the email output container flexible */
        .email-output {
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            align-items: flex-start;
            max-width: 100%;
            width: 100%;
            height: auto;
            overflow-x: auto;
            padding: 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def create_streamlit_app(llm, portfolio, clean_text):
    # Page Configuration
    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧"
    )

    # Apply custom styles
    apply_custom_styles()

    # App Title and Description
    st.title("📧 Cold Email Generator")
    st.markdown(
        """
        Generate personalized cold emails by extracting job details from URLs 
        and matching your portfolio skills.
        """
    )

    # Input Section
    with st.sidebar:
        st.header("App Configuration")
        st.markdown("Provide input details below.")
        url_input = st.text_input(
            "Enter a Job URL:",
            value="https://jobs.nike.com/job/R-45253",
            help="Paste the URL of the job description or opportunity."
        )
        submit_button = st.button("Generate Email")

    # Process Input and Display Results
    if submit_button:
        st.subheader("Generated Cold Email")
        try:
            # Load job data from the URL
            st.info("Loading job details from the provided URL...")
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            # Load portfolio and match skills
            st.info("Matching your portfolio with job requirements...")
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)

            # Generate cold emails for matched jobs
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = llm.write_mail(job, links)

                st.success("Cold Email Generated:")

                # Create a two-column layout for better alignment
                col1, col2 = st.columns([1, 3])  # Adjust proportions for better email space
                with col1:
                    st.empty()  # Empty space in the left column for structure
                with col2:
                    # Display the email in the right column
                    st.markdown(f'<div class="email-output">{email}</div>', unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An Error Occurred: {e}")


if __name__ == "__main__":
    # Initialize Chain and Portfolio
    chain = Chain()
    portfolio = Portfolio()

    # Run Streamlit App
    create_streamlit_app(chain, portfolio, clean_text)
