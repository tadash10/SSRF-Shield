from urllib.parse import urlparse

def is_valid_url(url):
    parsed_url = urlparse(url)
    
    if not parsed_url.scheme or not parsed_url.netloc:
        return False
    
    allowed_schemes = ["http", "https"]
    if parsed_url.scheme not in allowed_schemes:
        return False
    
    # You can add more checks here based on your application's needs
    # For example, restrict certain domains, IP ranges, etc.
    
    return True
