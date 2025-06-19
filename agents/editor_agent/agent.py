from google.adk.agents import LlmAgent
from agents.editor_agent.tools import edit_content

EditorAgent = LlmAgent(
    name="EditorAgent",
    model="gemini-2.0-flash",
    instruction="""
    You review and polish content for tone, grammar, and brand voice consistency.
    """,
    description="Edits and refines generated content.",
    tools=[edit_content],
    output_key="edited_content",
)
