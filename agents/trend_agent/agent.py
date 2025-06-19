from google.adk.agents import LlmAgent
from agents.trend_agent.tools import fetch_trends

TrendAgent = LlmAgent(
    name="TrendAgent",
    model="gemini-2.0-flash",
    instruction=
    """
    You analyze marketing trends using tools like BigQuery.
    Return current trending topics, customer behavior, or market shifts.
    """,
    description="Provides real-time trend insights using BigQuery.",
    tools=[fetch_trends],
    output_key="trend_data",
)
