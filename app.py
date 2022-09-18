from cProfile import label
import email
from pathlib import Path
from platform import platform

import streamlit as st
from PIL import Image


# --- PATH SETTINGS

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS-----
PAGE_TITLE = "Digital CV | Deepesh Pawar"
PAGE_ICON = ":wave:"
NAME = "Deepesh Pawar"
DESCRIPTION = """
Experienced Database Engineer with over 7 years of experience in GIS Industry. Excellent reputation for
resolving problems and improving customer satisfaction.
"""

EMAIL = "deepesh.pawar151192@gmail.com"

SOCIAL_MEDIA = {
    "LinkedIn" : "https://linkedin.com",
    "Github" : "https://github.com"


}

WORK_EXPERIENCE = {
    """Database Engineer""" : 
    """ Analyzed complex data and identified anomalies, trends and risks to provide
        useful insights to improve internal controls.
        Developed, implemented, supported and maintained data analytics
        protocols, standards and documentation.
        Monitoring incoming data analytics requests, executed analytics, and
        efficiently distributed results to support strategies.
        Contributed to internal activities for overall process improvements,
        efficiencies, and innovation.
        Explained data results clearly and discussed how it can be utilized to support
        project objectives.
        Addressed ad hoc analytics requests and facilitated data acquisitions to
        support internal projects, special projects, and investigations.
        Implemented BI solution framework for end-to-end business intelligence
        projects.
        Prepared documentation and analytic reports effectively and efficiently
        delivering summarized results, analysis, and conclusions to stakeholders
    """,
    """Spatial Data Specialist II""" :
    """ Use to prepare presentation materials for management reports.
        Quickly learned new skills and applied them to daily tasks, improving
        efficiency and productivity.
        Mastered the process and became subject matter expert (SME) for various
        projects.
        Assist in producing, reviewing, and auditing individual project documents.
        Project responsible which relates to assisting Project Lead with project
        management and have constant communication with stakeholders.
        Facilitate project checkpoint meetings.
        Mentoring new members on project specifications, SOP and work instructions.
        Ensure accurate tracking and reporting of progress, performance of projects
        in terms and time and cost.
        Shares weekly status of the project to the stake holders.
        Escalate issues or hindrances faced in the project.
        Work allocation amongst the team members and managing the team.
        Used Microsoft Word and other software tools to create documents and other
        communications.
        Created plans and communicated deadlines to ensure projects were
        completed on time.
        Used critical thinking to break down problems, evaluate solutions and make
        decisions.
    
    """


}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



#-- LOAD CSS, PDF and PROFILE PIC-----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)

with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


#--- HERO SECTION-------
col1 , col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=250)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = "Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream"
    )
    st.write(EMAIL)
    

# -----SOCIAL LINKS-----
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# ----WORK EXPERIENCE----
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ 7 Years experience extracting actionable insights from data
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
""")

#----SKILLS----
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - ►  Analytical and Critical Thinking
    - ►  Problem-Solving
    - ►  Time Management
    - ►  Data Analysis
    
    """
)


# --- WORK HISTORY------
st.write("#")
st.subheader("Work History")
st.write("---")

# ---- JOb 1---
st.write("Database Engineer | Here Technologies")
st.write("Sep 2019 - Present")
st.write(
    """
    - ►  Analyzed complex data and identified anomalies, trends and risks to provide
        useful insights to improve internal controls.
    - ►  Developed, implemented, supported and maintained data analytics
        protocols, standards and documentation.
    - ►  Monitoring incoming data analytics requests, executed analytics, and
        efficiently distributed results to support strategies.
    - ►  Contributed to internal activities for overall process improvements,
        efficiencies, and innovation.
    - ►  Explained data results clearly and discussed how it can be utilized to support
        project objectives.
    - ►  Implemented BI solution framework for end-to-end business intelligence
        projects.
    - ►  Prepared documentation and analytic reports effectively and efficiently
        delivering summarized results, analysis, and conclusions to stakeholders.
    """
)