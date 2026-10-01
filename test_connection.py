import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(
    model="qwen2.5:3b-instruct",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model_info={
        "vision": False,
        "function_calling": True,
        "json_output": False,
        "family": "unknown",
        "structured_output": False,
    },
)

agent = AssistantAgent(
    name="test_agent",
    model_client=model_client,
)

async def main():
    response = await agent.on_messages(
        [TextMessage(content="Halo, sebutkan 1 fakta fiksi tentang kerajaan rekaan bernama 'Aldoria'.", source="user")],
        CancellationToken(),
    )
    print(response.chat_message.content)

asyncio.run(main())