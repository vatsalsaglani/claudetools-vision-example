from pydantic import BaseModel, Field
from typing import List, Dict, Union, Literal


class TextContent(BaseModel):
    content_label: Literal["text"]
    content: str = Field(..., description="Text content on the page.")


class TableContent(BaseModel):
    content_label: Literal["table"]
    table_description: Union[str, None] = Field(
        ...,
        description=
        "Table name, table caption, or table description if available.")
    content: List[Dict] = Field(
        ...,
        description=
        "A list of dictionary where every dictionary is a column name row value pair."
    )


class ImageContent(BaseModel):
    content_label: Literal["image"]
    content: str = Field(
        ...,
        description=
        "Explain the content in the image if textual. If not textual content explain what image contains."
    )


class PageMetaInfo(BaseModel):
    meta_info: str = Field(
        ...,
        description=
        "Meta info of the page image content. Write your analysis of the entire document: how many paragraphs of texts, how many tables if any, and how many images if any and where."
    )


class ExtractedContent(BaseModel):
    page_meta_info: PageMetaInfo
    content: List[Union[TextContent, TableContent, ImageContent]] = Field(
        ...,
        description=
        "Content extracted from the page image document in the sequential order they are in."
    )
