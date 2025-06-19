from google.adk.agents import LlmAgent
from google_services.docs_utils import create_marketing_doc
from google_services.slides_utils import create_summary_slide
import asyncio

# Import the individual agents
from agents.trend_agent.agent import TrendAgent
from agents.copywriter_agent.agent import CopywriterAgent
from agents.designer_agent.agent import DesignerAgent
from agents.editor_agent.agent import EditorAgent
from agents.seo_agent.agent import SEOAgent


async def orchestrate_campaign(user_query: str = "Create a marketing campaign for AI tools"):
    """
    Orchestrate the entire marketing campaign creation process
    """
    print(f"🚀 Starting campaign orchestration for: {user_query}")

    try:
        # Step 1: Get trend data
        print("📊 Fetching trend data...")
        trend_result = await TrendAgent.run_async(user_query)
        trend_data = trend_result.get("trend_data", {})
        print(f"✅ Trends: {trend_data}")

        # Step 2: Generate copy based on trends
        print("✍️ Generating copy...")
        copy_result = await CopywriterAgent.run_async(trend_data=trend_data)
        written_content = copy_result.get("written_content", {})
        print(f"✅ Copy generated: {written_content}")

        # Step 3: Create visual assets
        print("🎨 Creating visual assets...")
        designer_result = await DesignerAgent.run_async(written_content=written_content)
        visuals = designer_result.get("visual_assets", {})
        print(f"✅ Visuals created: {visuals}")

        # Step 4: Edit content
        print("📝 Editing content...")
        edited_result = await EditorAgent.run_async(written_content=written_content)
        edited_content = edited_result.get("edited_content", {})
        print(f"✅ Content edited: {edited_content}")

        # Step 5: SEO optimization
        print("🔍 Optimizing for SEO...")
        seo_result = await SEOAgent.run_async(edited_content=edited_content)
        seo_content = seo_result.get("seo_optimized_content", {})
        print(f"✅ SEO optimized: {seo_content}")

        return {
            "trends": trend_data,
            "copy": written_content,
            "visuals": visuals,
            "edited": edited_content,
            "seo": seo_content,
            "campaign_summary": f"Complete marketing campaign for: {user_query}"
        }

    except Exception as e:
        print(f"❌ Error in orchestration: {str(e)}")
        return {
            "error": str(e),
            "campaign_summary": f"Failed to create campaign for: {user_query}"
        }


def create_workspace_documents(campaign_data):
    """
    Create Google Workspace documents from campaign data
    """
    try:
        # Prepare content for documents
        doc_content = {
            "Campaign Summary": campaign_data.get("campaign_summary", ""),
            "Trend Analysis": str(campaign_data.get("trends", {})),
            "Content Copy": str(campaign_data.get("copy", {})),
            "Visual Assets": str(campaign_data.get("visuals", {})),
            "Edited Content": str(campaign_data.get("edited", {})),
            "SEO Optimized": str(campaign_data.get("seo", {}))
        }

        # Create Google Doc
        doc_link = create_marketing_doc(doc_content)
        print(f"📄 Google Doc Created: {doc_link}")

        # Prepare slide content (shorter for slides)
        slide_content = {
            "Campaign Overview": campaign_data.get("campaign_summary", ""),
            "Key Trends": str(campaign_data.get("trends", {})[:500]),  # Truncate for slides
            "Main Copy": campaign_data.get("copy", {}).get("blog", "")[:500],
            "SEO Highlights": campaign_data.get("seo", {}).get("blog", "")[:500]
        }

        # Create Google Slides
        slide_link = create_summary_slide(slide_content)
        print(f"📊 Google Slides Created: {slide_link}")

        return {
            "doc_link": doc_link,
            "slide_link": slide_link
        }

    except Exception as e:
        print(f"❌ Error creating workspace documents: {str(e)}")
        return {"error": str(e)}


# Create the main orchestrator agent
OrchestratorAgent = LlmAgent(
    name="OrchestratorAgent",
    model="gemini-2.0-flash",
    instruction="""
    You are a marketing campaign orchestrator. You coordinate multiple specialized agents 
    to create comprehensive marketing campaigns. You manage the workflow between:
    1. Trend analysis
    2. Content creation
    3. Visual design
    4. Content editing
    5. SEO optimization
    6. Document creation

    You ensure all agents work together seamlessly to produce high-quality marketing materials.
    """,
    description="Orchestrates end-to-end marketing campaign creation using specialized agents.",
    tools=[orchestrate_campaign, create_workspace_documents],
    output_key="marketing_campaign",
)

OrchestratorAgent.root_agent = True

# Export the agent
agent = OrchestratorAgent
root_agent = OrchestratorAgent

# For backwards compatibility and direct execution
async def main():
    """
    Main execution function for testing
    """
    print("🚀 Starting Marketing Campaign Orchestrator")

    # Run the orchestration
    final_output = await orchestrate_campaign("AI tools and automation trends")

    print("\n📝 FINAL CAMPAIGN PACKAGE\n")
    print("=" * 50)

    for key, val in final_output.items():
        print(f"\n== {key.upper()} ==")
        print(f"{val}")
        print("-" * 30)

    # Create workspace documents
    if "error" not in final_output:
        print("\n📄 Creating Google Workspace Documents...")
        workspace_links = create_workspace_documents(final_output)

        if "error" not in workspace_links:
            print(f"\n✅ Documents created successfully!")
            print(f"📄 Google Doc: {workspace_links['doc_link']}")
            print(f"📊 Google Slides: {workspace_links['slide_link']}")
        else:
            print(f"❌ Document creation failed: {workspace_links['error']}")
    else:
        print(f"❌ Campaign creation failed: {final_output['error']}")


if __name__ == "__main__":
    # Run the main orchestrator
    asyncio.run(main())