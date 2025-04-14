from django.shortcuts import render
import validators  
import re

# A more advanced fake link detection function
def is_suspicious(url):
    # Common signs of suspicious links
    suspicious_patterns = [
        # Fake email domains (excluding common ones)
        r"[\w\-\.]+@(?!gmail|yahoo|outlook|protonmail)\.com",  
        # IP addresses in URL instead of domain names
        r"(https?://)?(\d{1,3}\.){3}\d{1,3}",
        # Suspicious domain extensions (.xyz, .info, .top, etc.)
        r"(https?://)?[a-zA-Z0-9\-]+\.(xyz|info|top|loan|club|date|work)",
        # URLs with improper or missing TLD
        r"\.com(?!/)",
        # Very long or oddly formatted URLs that seem off
        r"[\w\.\-]{50,}",  # Unusually long domain names or paths
    ]
    
    # Step 1: Validate URL format
    if not validators.url(url):
        return True, "The URL format appears invalid. Please check the link."
    
    # Step 2: Check for suspicious patterns
    for pattern in suspicious_patterns:
        if re.search(pattern, url):
            return True, "This URL has been flagged as suspicious due to unusual patterns."
    
    return False, "The URL looks safe!"

def check_link(request):
    result = None
    url = None
    feedback = None

    if request.method == "POST":
        url = request.POST.get("url")
        
        if not url:
            feedback = "Please provide a URL to check."
        else:
            suspicious, feedback = is_suspicious(url)
            result = "Suspicious" if suspicious else "Trusted"
    
    # Return the results to the template with a more user-friendly feedback message
    return render(
        request,
        "checker/check_link.html",
        {
            "result": result,
            "url": url,
            "feedback": feedback,
        }
    )
