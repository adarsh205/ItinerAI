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
        self.tools = [
            WeatherInfoTool(),
            CalculatorTool(),
            PlaceSearchTool(),
            CurrencyConversionTool(),
        ]

    def agent_function(self, state: MessagesState):
        conversation = state['messages']
        ip = [SYSTEM_PROMPT] + conversation
        response = self.llm_with_tools.invoke(ip)
        return {'messages': [response]}

    def build_graph(self):
        graph_builder = StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)

        self.graph = graph_builder.compile()
        return self.graph

    def __call__(self):
        return self.build_graph()