from google.adk.agents import LlmAgent
from agents.copywriter_agent.tools import generate_copy

CopywriterAgent = LlmAgent(
    name="CopywriterAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are a creative copywriter. Use the trend data to write compelling blog posts, email headlines, and social media content.
    """,
    description="Generates marketing content from trend insights.",
    tools=[generate_copy],
    output_key="written_content",
)
