# -------------------------------------------------------------
# JourneyWeaver AI Agent Travel Planning System
# -------------------------------------------------------------
import logging
from google.adk.agents import Agent, SequentialAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.adk.apps.app import App
from google.genai import types

# -----------------------------------------------------
# LOGGING SETUP
# -----------------------------------------------------
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
logger = logging.getLogger("JourneyWeaver")
logger.info("Initializing JourneyWeaver AI Travel Planning System...")

# -----------------------------------------------------
# RETRY CONFIG
# -----------------------------------------------------
retry_config = types.HttpRetryOptions(
    attempts=5,
    exp_base=7,
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504]
)

# -----------------------------------------------------
# GEMINI MODEL
# -----------------------------------------------------
AGENT_MODEL = Gemini(
    model="gemini-2.5-flash-lite-preview-09-2025",
    retry_options=retry_config
)

# -----------------------------------------------------
# MEMORY SERVICE (VALID ONLY IN RUNNER)
# -----------------------------------------------------
session_service = InMemorySessionService()

# -----------------------------------------------------
# SUB-AGENT 1 — DestinationResearchAgent
# -----------------------------------------------------
destination_research_agent = Agent(
    name="DestinationResearchAgent",
    model=AGENT_MODEL,
    tools=[google_search],
    description="An agent that researches travel destinations and gathers essential information",
    instruction="""
    You are a travel researcher. You will be given a destination and travel preferences, and you will research:
    - Best time to visit and weather patterns
    - Top attractions and must-see locations
    - Local culture, customs, and etiquette tips
    - Transportation options within the destination
    - Safety considerations and travel requirements
    Provide comprehensive destination insights for trip planning.
    """,
    output_key="destination_research",
)

# -----------------------------------------------------
# SUB-AGENT 2 — ItineraryBuilderAgent
# -----------------------------------------------------
itinerary_builder_agent = Agent(
    name="ItineraryBuilderAgent",
    model=AGENT_MODEL,
    description="An agent that creates structured travel itineraries with daily schedules",
    instruction="""
    You are a professional travel planner. Using the research from "destination_research" output, create a detailed itinerary that includes:
    - Day-by-day schedule with recommended activities
    - Suggested accommodation areas or districts
    - Estimated time requirements for each activity
    - Meal recommendations and dining suggestions
    - Budget estimates for major expenses
    Structure it logically for easy following during the trip.
    """,
    output_key="travel_itinerary",
)

# -----------------------------------------------------
# SUB-AGENT 3 — TravelOptimizerAgent
# -----------------------------------------------------
travel_optimizer_agent = Agent(
    name="TravelOptimizerAgent",
    model=AGENT_MODEL,
    description="An agent that optimizes travel plans with practical advice and alternatives",
    instruction="""
    You are a seasoned travel consultant. Using the itinerary from "travel_itinerary" output, optimize it by adding:
    - Money-saving tips and budget alternatives
    - Packing recommendations specific to the destination
    - Backup plans for weather or unexpected situations
    - Local apps, websites, or resources to download
    - Cultural do's and don'ts for respectful travel

    Format the final output as:
    
    ITINERARY: {travel_itinerary}

    OPTIMIZATION TIPS: [your money-saving and practical tips here]

    TRAVEL ESSENTIALS: [packing and preparation advice here]

    BACKUP PLANS: [alternative options and contingencies here]
    """,
)

# -----------------------------------------------------
# ROOT SEQUENTIAL AGENT
# -----------------------------------------------------
root_agent = SequentialAgent(
    name="TravelPlanningSystem",
    description="A comprehensive system that researches destinations, builds itineraries, and optimizes travel plans",
    sub_agents=[
        destination_research_agent,
        itinerary_builder_agent,
        travel_optimizer_agent,
    ],
    
)
# App wrapper required by ADK
app = App(
    name="TravelPlannerAgent",
    root_agent=root_agent
)
# -----------------------------------------------------------
# RUNNER — THIS is where memory is applied in session it self
# -----------------------------------------------------------
runner = Runner(
    app=app,
    session_service=session_service,
)

logger.info("JourneyWeaver AI Agent System initialized successfully.")