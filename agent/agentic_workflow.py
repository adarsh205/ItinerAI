from langgraph.graph import StateGraph, MessagesState, START, END 
from langgraph.prebuilt import ToolNode, tools_condition
from utils.model_loader import ModelLoader
from tools.weather_info_tool import WeatherInfoTool
from tools.calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConversionTool
from tools.place_search_tool import PlaceSearchTool
from prompt_library.prompt import SYSTEM_PROMPT


class GraphBuilder():

    def __init__(self):
        pass

    def agent_function(self):
        pass

    def build_graph(self):
        pass

    def __call__(self):
        pass