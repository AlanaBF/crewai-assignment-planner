from pydantic import BaseModel, Field
from typing import List

class ResearchFinding(BaseModel):
    title: str = Field(..., description="The title of the research finding")
    summary: str = Field(..., description="A brief summary of the research finding")
    citation: str = Field(..., description="The citation for the research finding")
    topic_area: str = Field(..., description="The topic area this finding relates to")
    source_url: str = Field(..., description="The URL where the research finding can be accessed")

class ResearchFindingsOutput(BaseModel):
    findings: List[ResearchFinding] = Field(..., description="A list of research findings relevant to the assignment")
    overall_summary: str = Field(..., description="An overall summary of the research findings and their relevance to the assignment")

class TopicAnalysisSection(BaseModel):
    topic_area: str = Field(..., description="The topic area being analyzed")
    definition: str = Field(..., description="A clear definition of the concept")
    cloud_relevance: str = Field(..., description="Explanation of how this concept applies to cloud computing")
    key_points: List[str] = Field(..., description="Key points a student must understand")
    common_misconceptions: List[str] = Field(..., description="Common misunderstandings or mistakes")
    citations: List[str] = Field(..., description="Relevant citations supporting the analysis")

class AnalysisOutput(BaseModel):
    sections: List[TopicAnalysisSection] = Field(..., description="Structured analysis across all topic areas")
    overall_summary: str = Field(..., description="Summary of how all concepts relate to cloud computing")

class AssignmentSectionGuidance(BaseModel):
    section_heading: str = Field(..., description="The heading of the assignment section")
    what_to_cover: List[str] = Field(..., description="Key points to include in this section")
    why_it_matters: str = Field(..., description="Why this section is important for marks")
    common_mistakes: List[str] = Field(..., description="Common mistakes to avoid")
    example_suggestions: List[str] = Field(..., description="Examples or diagrams to include")

class AssignmentGuidanceOutput(BaseModel):
    suggested_outline: List[AssignmentSectionGuidance] = Field(..., description="Structured assignment outline with guidance")
    watch_out_for: List[str] = Field(..., description="General pitfalls to avoid")
    further_reading: List[str] = Field(..., description="Additional topics or sources to explore")