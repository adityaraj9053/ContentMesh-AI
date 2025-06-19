# agents/designer_agent/tools.py
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import base64
import os
from google.cloud import storage
from config import PROJECT_ID, LOCATION


def initialize_vertex_ai():
    """Initialize Vertex AI with your project settings"""
    vertexai.init(project=PROJECT_ID, location=LOCATION)


def create_design_with_vertex_ai(written_content):
    """
    Generate actual images using Vertex AI Imagen
    """
    try:
        # Initialize Vertex AI
        initialize_vertex_ai()

        # Load the Imagen model
        model = ImageGenerationModel.from_pretrained("imagegeneration@006")

        # Extract key information from written content for prompts
        blog_content = written_content.get("blog", "")
        social_content = written_content.get("social", "")

        # Create prompts for different image types
        infographic_prompt = f"""
        Create a professional infographic design about: {blog_content}
        Style: Clean, modern, corporate
        Include: Charts, icons, text overlays
        Color scheme: Blue and white
        Layout: Vertical orientation
        """

        social_banner_prompt = f"""
        Create a social media banner for: {social_content}
        Style: Eye-catching, vibrant, engaging
        Include: Bold text, trendy graphics
        Color scheme: Gradient background
        Layout: 16:9 aspect ratio
        """

        # Generate images
        print("🎨 Generating infographic...")
        infographic_response = model.generate_images(
            prompt=infographic_prompt,
            number_of_images=1,
            aspect_ratio="9:16",  # Vertical for infographic
            safety_filter_level="block_some",
            person_generation="dont_allow"
        )

        print("🎨 Generating social banner...")
        banner_response = model.generate_images(
            prompt=social_banner_prompt,
            number_of_images=1,
            aspect_ratio="16:9",  # Horizontal for banner
            safety_filter_level="block_some",
            person_generation="dont_allow"
        )

        # Save images to Google Cloud Storage (or local storage)
        infographic_url = save_image_to_storage(
            infographic_response.images[0]._image_bytes,
            "infographic.png"
        )

        banner_url = save_image_to_storage(
            banner_response.images[0]._image_bytes,
            "social_banner.png"
        )

        return {
            "infographic_url": infographic_url,
            "social_banner": banner_url,
            "generation_status": "success",
            "prompts_used": {
                "infographic": infographic_prompt,
                "banner": social_banner_prompt
            }
        }

    except Exception as e:
        print(f"❌ Error generating images: {str(e)}")
        # Fallback to placeholder images
        return {
            "infographic_url": "https://via.placeholder.com/600x800/0066CC/FFFFFF?text=Infographic",
            "social_banner": "https://via.placeholder.com/1200x675/FF6B6B/FFFFFF?text=Social+Banner",
            "generation_status": "failed",
            "error": str(e)
        }


def save_image_to_storage(image_bytes, filename):
    """
    Save generated image to Google Cloud Storage
    """
    try:
        # Initialize storage client
        storage_client = storage.Client(project=PROJECT_ID)
        bucket_name = f"{PROJECT_ID}-generated-images"

        # Create bucket if it doesn't exist
        try:
            bucket = storage_client.bucket(bucket_name)
        except:
            bucket = storage_client.create_bucket(bucket_name, location=LOCATION)

        # Upload image
        blob = bucket.blob(f"marketing-assets/{filename}")
        blob.upload_from_string(image_bytes, content_type="image/png")

        # Make it publicly accessible
        blob.make_public()

        return blob.public_url

    except Exception as e:
        print(f"❌ Error saving to storage: {str(e)}")
        # Save locally as fallback
        local_path = f"generated_images/{filename}"
        os.makedirs("generated_images", exist_ok=True)

        with open(local_path, "wb") as f:
            f.write(image_bytes)

        return f"file://{os.path.abspath(local_path)}"


def save_image_locally(image_bytes, filename):
    """
    Save image to local directory (alternative to cloud storage)
    """
    os.makedirs("generated_images", exist_ok=True)
    local_path = f"generated_images/{filename}"

    with open(local_path, "wb") as f:
        f.write(image_bytes)

    return f"file://{os.path.abspath(local_path)}"


# For backwards compatibility, keep the simple version as backup
def create_design(written_content):
    """
    Simple placeholder version (fallback)
    """
    return create_design_with_vertex_ai(written_content)