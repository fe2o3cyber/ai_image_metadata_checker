"""
ai_metadata_checker.py

A lightweight script to scan image files for common AI-generated metadata identifiers (e.g. C2PA, Adobe Content Credentials).

Author: Charles Riley Rust
"""
import os       #Used to check if file is locally on file system
import argparse # Used to handle command-line arguments

# Common AI metadata identifiers in image files.
AI_INDICATORS = [
    b'c2pa', b'claim_generator', b'claim_generator_info',
    b'created_software_agent', b'actions.v2', b'assertions',
    b'urn:c2pa', b'jumd', b'jumb', b'jumdcbor', b'jumdc2ma',
    b'jumdc2as', b'jumdc2cl', b'cbor', b'convertedsfwareagent',b'c2pa.version', 
    b'c2pa.assertions', b'c2pa.actions',
    b'c2pa.thumbnail', b'c2pa.signature', b'c2pa.manifest',
    b'c2pa.manifest_store', b'c2pa.ingredient', b'c2pa.parent',
    b'c2pa.provenance', b'c2pa.claim', b'c2pa.hash', b'c2pa.authority',
    b'jumdc2pn', b'jumdrefs', b'jumdver', b'jumdmeta',
    
    
   'midjourney'.encode('utf-8'),
   'stable-diffusion'.encode('utf-8'),
   'stable diffusion'.encode('utf-8'),
   'stable_diffusion'.encode('utf-8'),
   'artbreeder'.encode('utf-8'),
   'runwayml'.encode('utf-8'),
   'remix.ai'.encode('utf-8'),
   'firefly'.encode('utf-8'),
   'adobe_firefly'.encode('utf-8'),

    # OpenAI / DALL·E indicators (all encoded to bytes)
    'openai'.encode('utf-8'),
    'dalle'.encode('utf-8'),
    'dalle2'.encode('utf-8'),
    'DALL-E'.encode('utf-8'),
    'DALL·E'.encode('utf-8'),
    'created_by: openai'.encode('utf-8'),
    'tool: dalle'.encode('utf-8'),
    'tool: dalle2'.encode('utf-8'),
    'creator: openai'.encode('utf-8'),
    'creator: dalle'.encode('utf-8'),
    'openai.com'.encode('utf-8'),
    'api.openai.com'.encode('utf-8'),
    'openai_model'.encode('utf-8'),
    'openai_gpt'.encode('utf-8'),
    
    #Further possible AI-Generation Indicators
    'generated_by'.encode('utf-8'),
    'model_id'.encode('utf-8'),
    'model_version'.encode('utf-8'),
    'model_info'.encode('utf-8'),
    'tool_name'.encode('utf-8'),
    'tool_creator'.encode('utf-8'),
    'tool_version'.encode('utf-8'),
    'model_signature'.encode('utf-8'),
    'ai_model'.encode('utf-8'),
    'ai_tool'.encode('utf-8'),
    'generator'.encode('utf-8'),
    'generated_by_ai'.encode('utf-8'),
    'ai_generated'.encode('utf-8'),
    'ai_art'.encode('utf-8')
    ]

def check_image_for_ai_metadata(image_path):
    """Scans a file for AI metadata indicators."""
    
    # Check if the file exists at the given path
    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        return
    try:
        with open(image_path, "rb") as img_file:
            data = img_file.read()
        found_indicators = [indicator for indicator in AI_INDICATORS if indicator in data]


 #  Condition whether or not file has AI-generated metadata and if so print indicators into a human-readable string.
        if found_indicators:
            print(f"\nAI metadata indicators were FOUND in: {image_path}\n")
            print("Indicators Found in Metadata:")
            for i, indicator in enumerate(found_indicators, start=1):
                printable = indicator.decode("utf-8", errors="replace")
                print(f" {i:2}. {printable}")
        else:
            print(f"\n No AI metadata indicators found in: {image_path}.")

    except PermissionError:
        print(f" Permission denied: {image_path}")
    except IOError as e:
        print(f" IO Error: {e}")
    except Exception as e:
        print(f" Unexpected error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Detect AI-generated metadata in image files (e.g., C2PA, Adobe Content Credentials)."
    )
    parser.add_argument("image_path", help="Path to the image file to scan.")
    args = parser.parse_args()

    check_image_for_ai_metadata(args.image_path)

if __name__ == "__main__":
    main()
