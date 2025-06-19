from google.adk.agents import LlmAgent
from agents.seo_agent.tools import optimize_for_seo

SEOAgent = LlmAgent(
    name="SEOAgent",
    model="gemini-2.0-flash",
    instruction="""
    You optimize content for SEO. Add keywords and structure blog content for ranking.
    """,
    description="Boosts content visibility using SEO techniques.",
    tools=[optimize_for_seo],
    output_key="seo_optimized_content",
)
