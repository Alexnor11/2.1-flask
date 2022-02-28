AD_CREATE = {
    "type": "object",
    "properties": {
        "title": {
            "type": "string",
            "description": "The title of advertisement",
        },
        "description": {
            "type": "string",
            "description": "The text describing the advertisement",
        },
    },
    "required": ["title", "description"]
}