from typing import Dict, List
import json
import yaml

def format_as_json(analysis_result: Dict) -> str:
    """Format the analysis result as JSON string."""
    return json.dumps(analysis_result, indent=2)

def format_as_yaml(analysis_result: Dict) -> str:
    """Format the analysis result as YAML string."""
    return yaml.dump(analysis_result, sort_keys=False)

def format_as_text(analysis_result: Dict) -> str:
    """Format the analysis result as plain text."""
    output = []
    
    # Word counts section
    output.append("Word Counts:")
    for word, count in analysis_result.get("word_counts", {}).items():
        output.append(f"  {word}: {count}")
    
    # Quick summary
    if "quick_summary" in analysis_result:
        output.append("\nQuick Summary:")
        output.append(f"  {analysis_result['quick_summary']}")
    
    # Bullet points
    if "bullet_point_highlights" in analysis_result:
        output.append("\nHighlights:")
        for point in analysis_result["bullet_point_highlights"]:
            output.append(f"  • {point}")
    
    # Sentiment
    if "sentiment_analysis" in analysis_result:
        output.append("\nSentiment Analysis:")
        output.append(f"  {analysis_result['sentiment_analysis']}")
    
    # Keywords
    if "keywords" in analysis_result:
        output.append("\nKeywords:")
        for keyword in analysis_result["keywords"]:
            output.append(f"  • {keyword}")
    
    return "\n".join(output)

def format_output(analysis_result: Dict, format_type: str = "json") -> str:
    """
    Format the analysis result in the specified format.
    
    Args:
        analysis_result: Dictionary containing analysis results
        format_type: One of "json", "yaml", or "text"
        
    Returns:
        Formatted string in the specified format
    """
    # Ensure all dictionary values exist
    analysis_result = {
        "word_counts": analysis_result.get("word_counts", {}),
        "quick_summary": analysis_result.get("quick_summary", "No summary available"),
        "bullet_point_highlights": analysis_result.get("bullet_point_highlights", []),
        "sentiment_analysis": analysis_result.get("sentiment_analysis", "Neutral"),
        "keywords": analysis_result.get("keywords", [])
    }
    
    formatters = {
        "json": format_as_json,
        "yaml": format_as_yaml,
        "text": format_as_text
    }
    
    if format_type not in formatters:
        raise ValueError(f"Unsupported format type: {format_type}")
        
    return formatters[format_type](analysis_result)
