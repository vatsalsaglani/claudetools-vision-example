from claudetools.tools.tool import AsyncTool
from prompts.system_prompts import SYSTEM_PROMPTS
from schemas import ExtractedContent
from configs import ANTHROPIC_API_KEY

tool = AsyncTool(ANTHROPIC_API_KEY)


async def extractContentFromImage(image_str: str, media_type: str):
    user_messages = [{
        "role":
        "user",
        "content": [{
            "type": "image",
            "source": {
                "type": "base64",
                "media_type": media_type,
                "data": image_str
            }
        }, {
            "type": "text",
            "text": SYSTEM_PROMPTS.EXTRACT_CONTENT
        }]
    }]
    tools = [{
        "name": "extractedContent",
        "description": "Extract content from page image",
        "parameters": ExtractedContent.model_json_schema()
    }]
    tool_choice = {"name": "extractedContent"}
    return await tool("claude-3-opus-20240229",
                      user_messages,
                      tools=tools,
                      tool_choice=tool_choice,
                      max_tokens=4095,
                      temperature=0.2)
