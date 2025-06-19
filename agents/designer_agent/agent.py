from google.adk.agents import LlmAgent
from agents.designer_agent.tools import create_design

DesignerAgent = LlmAgent(
    name="DesignerAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are a graphic designer. Use content to design infographics or social media visuals using Vertex AI's image capabilities.
    """,
    description="Generates visual assets using Vertex AI.",
    tools=[create_design],
    output_key="visual_assets",
)
