from gradio_client import Client

# Define categories (keeping the same categories for reference)
CATEGORIES = [
    "Anime & Manga",
    "TV Shows & Movies",
    "Video Games",
    "Cartoons & Animated Characters",
    "Pop Culture & Music",
    "K-Pop & Idol Groups",
    "Celebrities & Influencers",
    "Floral & Botanical",
    "Scenery & Landscapes",
    "Abstract & Minimalist",
    "Cats & Dogs",
    "Wildlife & Exotic Animals",
    "Fantasy Creatures",
    "Football & Basketball",
    "Extreme Sports",
    "Fitness & Gym",
    "Motivational & Inspirational",
    "Funny & Meme-Based",
    "Dark & Gothic",
    "Cyberpunk & Sci-Fi",
    "Glitch & Vaporwave",   
    "AI & Robotics",
    "Flags & National Pride",
    "Traditional Art",
    "Astrology & Zodiac Signs"
]

def classify_design(design):
    """
    Classifies a design into a category using the Hugging Face Space API.
    
    Args:
        design (Design): A Design instance containing an image URL.

    Returns:
        str: The category of the design.
    """
    try:
        # Initialize the Gradio client
        client = Client("https://abdelrahmanasdlf-artcase11.hf.space")
        
        print("Sending request to API with URL:", design.image_url)
        
        # Make the prediction using the client
        result = client.predict(
            design.image_url,  # The image URL
            api_name="/predict"  # The API endpoint name
        )
        
        print("API Response:", result)
        
        if result:
            return result
        else:
            print("No result returned from API")
            return "unknown"
            
    except Exception as e:
        print(f"Error in classifying design: {e}")
        import traceback
        print("Full error traceback:")
        print(traceback.format_exc())
        return "unknown"
