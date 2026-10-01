import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.models.openai import OpenAIChatCompletionClient
from personas import GM_PROMPT, WEI_PROMPT, CHAOS_PROMPT, BALANCER_PROMPT

model_info = {
    "vision": False,
    "function_calling": True,
    "json_output": False,
    "family": "unknown",
    "structured_output": False,
}

def make_client():
    return OpenAIChatCompletionClient(
        model="qwen2.5:3b-instruct",
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        model_info=model_info,
    )

gm = AssistantAgent(name="GameMaster", model_client=make_client(), system_message=GM_PROMPT)
wei = AssistantAgent(name="Wei_Utara", model_client=make_client(), system_message=WEI_PROMPT)
chaos = AssistantAgent(name="Wildcard", model_client=make_client(), system_message=CHAOS_PROMPT)
balancer = AssistantAgent(name="Selatan", model_client=make_client(), system_message=BALANCER_PROMPT)

async def main():
    print("=== Test GM ===")
    r = await gm.on_messages([TextMessage(content="Laporkan status awal: Wei_Utara 50000 pasukan @ Utara, Wildcard 8000 pasukan @ Tengah, Selatan 30000 pasukan @ Selatan.", source="user")], CancellationToken())
    print(r.chat_message.content)

    print("\n=== Test Wei_Utara ===")
    r = await wei.on_messages([TextMessage(content="Apa langkah pertamamu di awal perang ini?", source="user")], CancellationToken())
    print(r.chat_message.content)

    print("\n=== Test Wildcard ===")
    r = await chaos.on_messages([TextMessage(content="Apa langkah pertamamu di awal perang ini?", source="user")], CancellationToken())
    print(r.chat_message.content)

    print("\n=== Test Selatan ===")
    r = await balancer.on_messages([TextMessage(content="Apa langkah pertamamu di awal perang ini?", source="user")], CancellationToken())
    print(r.chat_message.content)

asyncio.run(main())