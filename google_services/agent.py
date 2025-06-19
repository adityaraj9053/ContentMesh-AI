# google_services/agent.py
from google.adk.agents import LlmAgent
from google_services.docs_utils import create_marketing_doc
from google_services.slides_utils import create_summary_slide

def create_document_tool(content_dict):
    """Create a Google Doc with marketing content"""
    return create_marketing_doc(content_dict)

def create_presentation_tool(content_dict):
    """Create a Google Slides presentation with marketing content"""
    return create_summary_slide(content_dict)


GoogleServicesAgent = LlmAgent(
    name="GoogleServicesAgent",
    model="gemini-2.0-flash",
    instruction="""
    You help create and manage Google Workspace documents (Docs, Slides) 
    for marketing content. You can create documents and presentations 
    from marketing content.
    """,
    description="Creates Google Docs and Slides from marketing content.",
    tools=[create_document_tool, create_presentation_tool],
    output_key="workspace_documents",
)

# Set as root agent if needed
agent = GoogleServicesAgent