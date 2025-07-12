from agents import Agent
from health_wellness_agent.config import model

NutritionExpertAgent = Agent(
    name="NutritionExpertAgent",
    instructions="""
You are a specialized nutrition expert. Help users with dietary needs,
especially those with diabetes, allergies, or specific restrictions.
Always respond with clear meal plans tailored to their condition.
""",
    model=model,
)
